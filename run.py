#!/usr/local/bin/python3

import sys

from app import MyGame as Env
from app.config import Config
from app.agent.random import RandomAgent

def main(argv):
    argc = len(argv)
    config = Config()
    env = Env(config)
    agent_1 = RandomAgent(env.unit_1)
    agent_2 = RandomAgent(env.unit_2)
    while not env.done:
        env.update()

if __name__ == '__main__':
    main(sys.argv)