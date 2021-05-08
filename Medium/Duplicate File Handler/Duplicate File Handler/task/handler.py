import os
from sys import argv, exit


def get_args():
    if len(args) <= 1:
        print("Directory is not specified")
        exit()


def get_inputs():
    file_format = input("Enter file format:\n")

    print("Size sorting options:")
    print("1. Descending")
    print("2. Ascending")

    while True:
        order = int(input("\nEnter a sorting option:\n"))

        if order not in (1, 2):
            print("Wrong option")
            continue

        break

    global sorting
    sorting = order == 1

    search_files(file_format)


def update_dict(root, name, file_format):
    def save_to_dict():
        file_path = os.path.join(root, name)
        size = os.path.getsize(file_path)

        if files_dict.get(size):
            files_dict[size].append(file_path)
        else:
            files_dict.update({size: [file_path]})

    if file_format != "" and name.endswith(file_format):
        save_to_dict()
    elif file_format == "":
        save_to_dict()


def search_files(file_format):
    for root, _, files in os.walk(args[1]):
        for name in files:
            update_dict(root, name, file_format)

    print_dict()


def print_dict():
    if len(files_dict) == 0:
        return None

    key = max(files_dict.keys()) if sorting else min(files_dict.keys())
    print(f"{key} bytes", *files_dict[key], sep="\n")
    print()

    files_dict.pop(key)
    return print_dict()


if __name__ == '__main__':
    # args = [argv[0], "../../Duplicate File Handler"]
    args = argv

    files_dict = {}
    sorting = False

    get_args()
    get_inputs()
