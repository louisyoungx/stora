class Reactive(dict):
    def __init__(self, target, func):
        super().__init__(target)
        self.target = target
        self.func = func
        self.react()

    def react(self):
        for key in self.target:
            if type(self.target[key]) == dict:
                self.target[key] = Reactive(self.target[key], self.func)

    def __getitem__(self, key):
        return self.target[key]

    def __setitem__(self, key, value):
        if type(value) == dict:
            self.target[key] = Reactive(value, self.func)
        else:
            self.target[key] = value
        self.func()

    def __str__(self):
        return str(self.target)

    def read(self):
        return self.__str__()
