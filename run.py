
import sys
from app import MyGame as Env
from app.config import Config

def main(argv):
    argc = len(argv)
    config = Config()
    env = Env(config)
    while not env.done:
        env.update()

if __name__ == '__main__':
    main(sys.argv)