#!/usr/bin/python
# coding: utf-8


import sys

from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
from twisted.python import log


class MessageLogger(object):
    def __init__(self, file):
        self.file = file

    def log(self, message):
        timestap = time.strftime("[%H:%M:%S]", time.localtime())
        self.file.write("%s %s\n" % (timestap, message))
        self.file.flush()

    def close(self):
        self.file.close()


class LogBot(irc.IRCClient):
    nickname = 'twistedbot'

    def conectionMade(self):
        iro.IRCClient.connectionMade(self)
        self.logger = MessageLogger(open(self.factory.filename, 'a'))
        self.logger.log("[connected at %s]" %
                        time.asctime())

    def conectionLost(self, reason):
        iro.IRCClient.connectionMade(self, reason)
        self.logger = MessageLogger(open(self.factory.filename, 'a'))
        self.logger.log("[disconnected at %s]" %
                        time.asctime())
        self.logger.close()
    
    def singedOn(self):
        """Called when bot has succesfully signed on to server."""
        self.joined(self.factory.channel)

    def joined(self, channel):
        """This will get called when the bot joins the channel."""
        self.logger.log("[I have joined %s]" % channel)

    def privmsg(self, user, channel, msg):
        user = user.split('!', 1)[0]
        self.loggers.log("<%s> %s" % (user, msg))

        if channel == self.nickname:
            msg = "It isn't nice to whisper! Play nice with the group."
            self.msg(user, msg)
            return

        if msg.startswith(self.nickname + ":"):
            msg = "%s: I am a log bot" % user
            self.msg(channel, msg)
            self.logger.log("<%s> %s" % (user, msg))

    def action(self, user, channel, msg):
        user = user.split("!", 1)[0]
        self.logger.log("* %s %s" %(user, msg))

    def irc_NICK(self, prefix, params):
        old_nick = prefix.split("!")[0]
        new_nick = params[0]
        self.logger.log("%s is now known as %s" % (old_nick, new_nick))

    def alterCollideNick(self, nickname):
        return nickname + '^'
    

class LogBotFactory(protocol.ClientFactory):
    protocol = LogBot
    
    def __init__(self, channel, filename):
        self.channel = channel
        self.filename = filename

    def clientConnectionLost(self, connector, reason):
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "connection failed: ", reason
        reactor.stop()


if __name__ == '__main__':
    log.startLogging(sys.stdout)
    f = LogBotFactory(sys.argv[1], sys.argv[2])
    reactor.connectTCP('127.0.0.1', 8123, f)
    reactor.run()
