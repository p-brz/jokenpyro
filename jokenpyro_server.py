import os

import Pyro4

from jokenpo_manager import *
from model import *

class JokenpoServer(object):
    def __init__(self):
        self.sessions = {}
        self.jokenpo = JokenpoManager()

    def start(self):
        maxTries = 500
        for i in range(maxTries):
            sessid = os.urandom(4)

            if not sessid in self.sessions:
                self.sessions[sessid] = PlayerState()

                return sessid

        print("Failed to generate session id")

        return None

    def play(self, sessionId, playerChoice):
        serverChoice = self.jokenpo.choiceJokenpo()
        winner = self.jokenpo.compare(playerChoice, serverChoice)

        matchState = self.sessions[sessionId]
        matchState.addResult(winner)

        return MatchResult(winner, matchState, {
            1 : playerChoice,
            2 : serverChoice
        })

def main():
    Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')
    pyroDaemon = Pyro4.Daemon()
    uri = pyroDaemon.register(JokenpoServer)

    print("Started object at uri: ", uri)

    nameServer = Pyro4.locateNS()
    nameServer.register("example.JokenpoServer", uri)

    print("registered on nameServer")

    pyroDaemon.requestLoop()


if __name__=="__main__":
    main()
