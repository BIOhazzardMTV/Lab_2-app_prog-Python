from shutil import rmtree, copy
from os import mkdir, listdir
from os.path import isdir, abspath


def dataset_copy(class_label: str, destination: str):
    source = abspath(f"dataset/{class_label}")
    for i in listdir(source):
        copy(f"{source}\\{i}", f"{destination}\\{class_label}_{i}")


if __name__ == "__main__":
    if not isdir("dataset2"):
        mkdir("dataset2")
    else:
        rmtree('dataset2')
        mkdir('dataset2')
    dest = abspath('dataset2')
    dataset_copy("cat", dest)
    dataset_copy("dog", dest)
