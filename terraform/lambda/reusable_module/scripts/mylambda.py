import os

def handler(event, context):
    dummy = os.environ['DUMMY']
    print(dummy)

    return {
      'dummy': dummy
    }
