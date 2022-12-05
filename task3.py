from os import listdir, mkdir, chdir, remove
from os.path import abspath, relpath, isfile, isdir
from shutil import rmtree, copy
from random import randint
from csv import DictWriter
import _csv


def rand_num_dataset(class_label: str, destination: str, file: '_csv.writer'):
    source = abspath(f"dataset/{class_label}")
    for i in listdir(source):
        name = randint(0, 10000)
        while isfile(f"dataset3/{name}.jpg"):
            name = randint(1, 10000)
        copy(f"{source}/{i}", f"{destination}/{name}.jpg")
        file.writerow({
            "Absolute path": f"{abspath(f'{name}.jpg')}",
            "Relative path": f"{relpath(f'{name}.jpg', start='C:/Users/Professional/PycharmProjects/pythonProject')}",
            "Class label": class_label
        })


if __name__ == "__main__":
    if not isdir("dataset3"):
        mkdir("dataset3")
    else:
        rmtree('dataset3')
        mkdir('dataset3')
    dest = abspath('dataset3')
    if isfile("dataset3/annotation.csv"):
        remove("dataset3/annotation.csv")
    f = open("dataset3/annotation.csv", "a+")
    names = ["Absolute path", "Relative path", "Class label"]
    csv_file = DictWriter(f, lineterminator="\r", fieldnames=names)
    csv_file.writeheader()
    rand_num_dataset("cat", dest, csv_file)
    rand_num_dataset("dog", dest, csv_file)
