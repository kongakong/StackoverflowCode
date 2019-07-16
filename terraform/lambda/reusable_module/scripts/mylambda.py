import os

def handler():
    dummy = os.environ['DUMMY']
    print(dummy)

    return {
      'dummy': dummy
    }
