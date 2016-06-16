import time
from datetime import timedelta

from BeautifulSoup import BeautifulSoup
from urlparse import urljoin, urldefrag

from tornado import httpclient, gen, ioloop, queues


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    
}
URLS = {
    'HX':'http://www.huxiu.com/whatsnew.html?f=nav_article_whatsnew',
}

base_url = 'http://www.huxiu.com/whatsnew.html?f=nav_article_whatsnew'
concurrency = 10

@gen.coroutine
def get_links_from_url(url):
    """Download the page at `url` and parse it for links.

    Returned links have had the fragment after `#` removed, and have been made
    absolute so, e.g. the URL 'gen.html#tornado.gen.coroutine' becomes
    'http://www.tornadoweb.org/en/stable/gen.html'.
    """
    try:
        response = yield httpclient.AsyncHTTPClient().fetch(url, headers=HEADERS)
        print('fetched %s' % url)

        html = response.body if isinstance(response.body, str) \
            else response.body.decode()
        urls = [urljoin(url, remove_fragment(new_url))
                for new_url in get_links(html)]
    except Exception as e:
        print('Exception: %s %s' % (e, url))
        raise gen.Return([])
    
    raise gen.Return(urls)

def remove_fragment(url):
    pure_url, frag = urldefrag(url)
    return pure_url

def get_links(html):
    soup = BeautifulSoup(html)
    a_tags = soup.findAll('a')
    urls = [a_tag.get('href') for a_tag in a_tags]    
    return urls


@gen.coroutine
def main():
    q = queues.Queue()
    start = time.time()
    fetching, fetched = set(), set()

    @gen.coroutine
    def fetch_url():
        current_url = yield q.get()
        try:
            if current_url in fetching:
                return

            print 'fetching %s %d' % (current_url, q.qsize())
            fetching.add(current_url)
            urls = yield get_links_from_url(current_url)
            fetched.add(current_url)

            for new_url in urls:
                # Only follow links beneath the base URL
                if new_url.startswith(base_url):
                    yield q.put(new_url)

        finally:
            q.task_done()

    @gen.coroutine
    def worker():
        while True:
            yield fetch_url()

    q.put(base_url)

    # Start workers, then wait for the work queue to be empty.
    for _ in range(concurrency):
        worker()
    yield q.join(timeout=timedelta(seconds=300))
    assert fetching == fetched
    print('Done in %d seconds, fetched %s URLs.' % (
        time.time() - start, len(fetched)))



if __name__ == '__main__':
    import logging
    logging.basicConfig()
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(main)
