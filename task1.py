from os import chdir, path, remove
if __name__ == "__main__":
    chdir('dataset')
    if path.isfile("annotation.csv"):
        remove("annotation.csv")
    file_w = open("annotation.csv", "a+")
