#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
import random, math, turtle, time, inspect, pickle

turtle_functions = turtle._tg_turtle_functions
##turtle_functions = ['fd', 'bk', 'rt']


class AI_(turtle.Turtle):
    def __init__(self, chance):
        assert ((type(chance) is int) and (chance > 0) and (chance < 100)), "chance must be int, and 0 < chance < 100"
        self.chance = chance
        __turtle_ = turtle.Turtle()
        self.Turtle = __turtle_
        actions = {}
        self.actions = actions
        self._gen_values()
        func_params = {}
        self.func_params = func_params

    def _gen_values(self):
        actions = self.actions
        freq = range(self.chance, 100)
        if not(bool(actions)):
            for i in turtle_functions:
                actions[i] = random.choice(freq)
        options = {}
        for i, k in actions.items():
            options[i] = [0, "UK"]
        self.options = options
        ##print (actions)
        ##print (options)

    def _param_needed(self, fun):
        if not(inspect.getargspec(fun)[0]) is None:
            needed_param = inspect.getargspec(fun)[0]
            return needed_param
        else:
            return False

    def act(self, t):
        options = self.options
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
        ##print (values)
        action = random.choice(range(chance, 100))
        while r_time < t:
            action = random.choice(range(chance, 100))
            if (action in values):
                print (action, values[action])
                action = values[action]
                if not(self._param_needed(getattr(self.Turtle, action)) is False):
                    needed_param = self._param_needed(getattr(self.Turtle, action))
                    options[action][0] += 1
                    options[action][1] = needed_param
                    self._working_param(getattr(self.Turtle, action), needed_param)
            else:
                print (action)
            time.sleep(0.5)
            r_time += 0.5

    def _working_param(self, fun, params):
        func_params = self.func_params
        rnd_value = random.choice(range(100))
        types = ['int', 'str', 'bool']
        values = []
        strings = [i for i in range(int('0x10ffff', base=16))]
        good_type = False
        for i in params:
            for index, i in enumerate(types):
                if index == 0:
                    ##type == int
                    value = random.choice(range(1, 100))
                    values.append(value)
                elif index == 1:
                    ##type == str
                    len_ = random.choice(range(10))
                    value = ""
                    for i in range(len_):
                        value += chr(random.choice(strings))
                        values.append(value)
                else:
                    ##type == bool
                    value = random.choice(range(0,1))
                    ##choose either 1 or 0
                    value = bool(value)
                    ##convert value to bool [i.e. 1 ==> True, 0 ==> False]
                    values.append(value)

        for i in values:
            try:
                fun(i)
                func_params[fun] = i
                return i
            except:
                pass

    def get_prefs(self):
        options = self.options
        ret_values = []
        for i,k in options.values():
            if not('UK' in k):
                 ret_values.append([str(turtle_functions[i]), k])
        return ret_values

    def get_func_params(self):
        return self.func_params


screen = turtle.Screen()
AI = AI_(10)
AI.act(10)
print (AI.get_prefs(), "\n")
print (AI.get_func_params())
