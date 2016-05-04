#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
import random, math, turtle, time

##turtle_functions = turtle._tg_turtle_functions
turtle_functions = ['fd', 'bk', 'rt']


class AI_(turtle.Turtle):
    def __init__(self, chance):
        assert ((type(chance) is int) and (chance > 0) and (chance < 100)), "chance must be int, and 0 < chance < 100"
        self.chance = chance
        __turtle_ = turtle.Turtle()
        self.Turtle = __turtle_
        actions = {}
        self.actions = actions
        self._gen_values()

    def _gen_values(self):
        actions = self.actions
        freq = range(self.chance, 100)
        if not(bool(actions)):
            for i in turtle_functions:
                actions[i] = random.choice(freq)
        ##print (actions)

    def act(self, t):
        r_time = 0
        actions = self.actions
        chance = self.chance
        ##print (actions.values())
        ##values = list(actions.values())
        values = dict.fromkeys(actions.values())
        k = 0
        for i in values:
            values[i] = list(actions.keys())[k]
            k += 1
        print (values)
        action = random.choice(range(chance, 100))
        while r_time < t:
            action = random.choice(range(chance, 100))
            if (action in values):
                print (action, values[action])
                action = values[action]
                getattr(self.Turtle, action)(random.choice(range(action, chance)))
            else:
                print (action)
            time.sleep(0.5)
            r_time += 0.5






screen = turtle.Screen()
AI = AI_(10)
AI.act(3)
