import _csv
from csv import DictWriter
from os import chdir, remove, listdir
from os.path import abspath, relpath, isfile


def get_csv(file: '_csv.writer', class_label: str):
    """Принимает открытый для дозаписи csv-файл и метку класса, записывает в csv-файл данные"""
    chdir(class_label)
    for i in listdir():
        file.writerow({
         "Absolute path": f"{abspath(i)}",
         "Relative path": f"{relpath(i,start='C:/Users/Professional/PycharmProjects/pythonProject')}",
         "Class label": class_label
        })
    chdir("..")


if __name__ == "__main__":
    chdir('dataset')
    if isfile("annotation.csv"):
        remove("annotation.csv")
    file_w = open("annotation.csv", "a+")
    names = ["Absolute path", "Relative path", "Class label"]
    csv_file = DictWriter(file_w, lineterminator="\r", fieldnames=names)
    csv_file.writeheader()
