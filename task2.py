from shutil import rmtree, copy
from os import mkdir, listdir, remove, chdir
from os.path import isdir, abspath, relpath, isfile
from csv import DictWriter


def dataset_copy(class_label: str, destination: str):
    source = abspath(f"dataset/{class_label}")
    for i in listdir(source):
        copy(f"{source}\\{i}", f"{destination}\\{class_label}_{i}")


def get_csv(destination: str):
    chdir("dataset2")
    if isfile("annotation.csv"):
        remove("annotation.csv")
    file = open("annotation.csv", "a+")
    names = ["Absolute path", "Relative path", "Class label"]
    csv_file = DictWriter(file, lineterminator="\r", fieldnames=names)
    csv_file.writeheader()
    for i in listdir(destination):
        class_label = (i.split("_"))[0]
        csv_file.writerow({
            "Absolute path": f"{abspath(i)}",
            "Relative path": f"{relpath(i,start='C:/Users/Professional/PycharmProjects/pythonProject')}",
            "Class label": class_label
        })


if __name__ == "__main__":
    if not isdir("dataset2"):
        mkdir("dataset2")
    else:
        rmtree('dataset2')
        mkdir('dataset2')
    dest = abspath('dataset2')
    dataset_copy("cat", dest)
    dataset_copy("dog", dest)
