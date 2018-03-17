#!/usr/local/bin/python3

import sys

from dovahkiin import MyGame as Env
from dovahkiin.config import Config
from dovahkiin.agent.random import RandomAgent
from dovahkiin.agent.simple import SimpleAgent

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