from os.path import abspath, isfile
from os import listdir


class Iterator:
    def __init__(self, limit, class_label, path):
        self.limit = limit
        self.counter = -1
        self.class_label = ""
        self.path = ""

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit and isfile(f"{self.path}/{self.counter:04}.jpg"):
            self.counter += 1
            return abspath(f"{self.path}/{self.counter:04}.jpg")
        else:
            raise StopIteration


if __name__ == "__main__":
    s_iter1 = Iterator(len(listdir(f"dataset/dog")), "dog", "dataset/dog")
    for val in s_iter1:
        print(val)
