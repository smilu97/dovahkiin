
class Agent:

    def __init__(self, obj):
        self.obj = obj
        obj.agent = self
    
    def make_decision(self):
        pass