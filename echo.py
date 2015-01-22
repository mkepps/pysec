#!/usr/bin/python
#twisted echo server

from twisted.internet import protocol,reactor

class EchoProtocol(protocol.Protocol):
    def dataReceived(self,data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    protocol = EchoProtocol

reactor.listenTCP(8080,EchoFactory())
print "listening on port 8080"
reactor.run()
