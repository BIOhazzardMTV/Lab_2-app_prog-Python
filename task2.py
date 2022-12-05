from shutil import rmtree
from os import mkdir
from os.path import isdir
if __name__ == "__main__":
    if not isdir("dataset2"):
        mkdir("dataset2")
    else:
        rmtree('dataset2')
        mkdir('dataset2')
