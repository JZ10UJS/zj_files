#!/usr/bin/python
# coding: utf-8


from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver


class Echo(Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols += 1
        print 'now numProtocol is %s' % self.factory.numProtocols
        self.transport.write(
            "Welcome! There are currently %d open connectinos.\n" %
            self.factory.numProtocols)

    def connectinoLost(self, reason):
        self.factory.numProtocols -= 1
        print 'now numProtocol is %s' % self.factory.numProtocols

    def dataReceived(self, data):
        self.transport.write(data)


class QOTD(Protocol):
    
    def connectionMade(self):
        print 'make a connect.!'
        # self.factory was set by the factory's default buildProtocol:
        self.transport.write(self.factory.quote + '\r\n')
        self.transport.loseConnection()


class QOTDFactory(Factory):
    
    # This will be used by the default buildProtocol to create new protocols:
    protocol = QOTD

    def __init__(self, quote=None):
        self.quote = quote or 'An apple a day keeps the doctor away'


class Answer(LineReceiver):

    answers = {'How are you?': 'Fine', None: "I don't know what you mean"}

    def lineReceived(self, line):
        if slef.answers.has_key(line):
            self.sendLine(self.answers[line])
        else:
            self.sendLine(self.answers[None])
            

class LoggingProtocol(LineReceiver):

    def lineReceived(self, line):
        self.factory.fp.write(line + '\n')
        self.transport.loseConnection()


class LogfileFactory(Factory):

    protocol = LoggingProtocol

    def __init__(self, filename):
        self.filename = filename

    def startFactory(self):
        self.fp = open(self.filename, 'a')

    def stopFactory(self):
        self.fp.close()


class Chat(LineReceiver):

    def __init__(self, users):
        self.users = users
        self.name = None
        self.state = "GETNAME"

    def connectionMade(self):
        self.sendLine("What's your name?")

    def connectionLost(self, reason):
        if self.name in self.users:
            del self.users[self.name]

    def lineReceived(self, line):
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        else:
            self.handle_CHAT(line)

    def handle_GETNAME(self, name):
        if name in self.users:
            self.sendLine("Name taken, please choose another.")
            return
        self.sendLine("Welcome, %s!" % (name,))
        self.name = name
        self.users[name] = self
        self.state = "CHAT"

    def handle_CHAT(self, message):
        message = "<%s> %s" % (self.name, message)
        # 当某一用户发送消息时，将该信息发送给users中的除该用户之外的所有人
        for name, protocol in self.users.iteritems():
            if protocol != self:
                protocol.sendLine(message)


class ChatFactory(Factory):

    def __init__(self):
        self.users = {} # maps user names to Chat instances

    def buildProtocol(self, addr):
        return Chat(self.users)


if __name__ == '__main__':
    reactor.listenTCP(8123, QOTDFactory())
    print 'wait for connect...'
    reactor.run()
    
