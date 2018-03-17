#!/usr/local/bin/python3

import sys

from . import MyGame as Env
from .config import Config
from .agent.random import RandomAgent
from .agent.simple import SimpleAgent

def main(argv):
    argc = len(argv)
    config = Config()
    env = Env(config)

    for i in range(3):
        RandomAgent(env.red[i])
        SimpleAgent(env.blue[i])
        
    while not env.done:
        env.update()

if __name__ == '__main__':
    main(sys.argv)