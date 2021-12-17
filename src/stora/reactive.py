from typing import Callable


class Reactive(dict):
    def __init__(self, target: dict, func: Callable) -> None:
        super().__init__(target)
        self.target = target
        self.func = func
        self.react()

    def react(self) -> None:
        for key in self.target:
            if type(self.target[key]) == dict:
                self.target[key] = Reactive(self.target[key], self.func)

    def __getitem__(self, key: str) -> str:
        return self.target[key]

    def __setitem__(self, key: str, value: str) -> None:
        if type(value) == dict:
            self.target[key] = Reactive(value, self.func)
        else:
            self.target[key] = value
        self.func()

    def __str__(self) -> str:
        return str(self.target)

    def read(self) -> str:
        return self.__str__()
