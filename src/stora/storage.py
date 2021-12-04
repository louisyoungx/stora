import os
import json
from .reactive import Reactive


class Storage(object):
    def __init__(self, state={}, filename="state.json", filepath=os.getcwd()):
        self.path = filepath
        self.file = f'{filepath}/{filename}'

        if state == {} and not self.load():
            self.state = Reactive(state, self.save)
            self.save()

    def load(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as storage:
                data = json.load(storage)
                if data == "":
                    self.state = Reactive({}, self.save)
                else:
                    self.state = Reactive(data, self.save)
                return True
        else:
            return False

    def save(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        with open(self.file, "w") as storage:
            storage.seek(0)
            storage.truncate()  # clear file
            data = self.state.read().replace("'", '"')
            data = json.loads(data)
            data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
            storage.write(data)