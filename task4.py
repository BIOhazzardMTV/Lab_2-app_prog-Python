from os import chdir
from os.path import isfile, abspath


def next_instance(class_label: str) -> str:
    chdir(f"C:/Users/Professional/PycharmProjects/pythonProject/dataset")
    if not isfile(f"helper-{class_label}.txt"):
        index = 0
    else:
        file = open(f"helper-{class_label}.txt", "r")
        index = int(file.readline())
    if isfile(f"{class_label}/{index:04}.jpg"):
        open(f"helper-{class_label}.txt", "w+").write(f"{index + 1}")
        return abspath(f"{index:04}.jpg")


if __name__ == "__main__":
    print(next_instance("dog"))
