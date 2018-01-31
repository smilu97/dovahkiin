#!/usr/local/bin/python3

import sys

from app import MyGame as Env
from app.config import Config
from app.agent.random import RandomAgent

def main(argv):
    argc = len(argv)
    config = Config()
    env = Env(config)

    for i in range(3):
        RandomAgent(env.red[i])
        RandomAgent(env.blue[i])
        
    while not env.done:
        env.update()

if __name__ == '__main__':
    main(sys.argv)