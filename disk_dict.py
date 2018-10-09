import json


class DiskDict(dict):

    def __init__(self, name):
        self.filename = name
        super().__init__(self)

    def __str__(self):

        return f"Stored Dict @ {self.filename}"

    def load(self):
        try:
            with open(self.filename) as f:
                self.update(json.load(f))
        except FileNotFoundError:
            print("File not Found Compadre, try saving one first, ya feel?")
        else:
            print(f"Loaded from file, dict now has {len(self)} items")

    def save(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump(self, f)
        except Exception as exc:
            print("Sorry this happened while saving {}".format(exc))
        else:
            print("Dictionary successfully written to disk.")
