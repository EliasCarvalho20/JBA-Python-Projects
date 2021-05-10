import os
import hashlib
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


def search_files(file_format):
    for root, _, files in os.walk(args[1]):
        for name in files:
            update_dict(root, name, file_format)

    print_dict()


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


def print_dict():
    for key in sorted(files_dict, reverse=sorting):
        print(f"{key} bytes", *files_dict[key], sep="\n", end="\n\n")


def check_dup():
    while True:
        user_input = input("Check for duplicates?\n")

        if "yes" in user_input:
            return True
        elif "no" in user_input:
            exit()
        else:
            print("Wrong option")
            continue


def get_file_hash():
    for k, v in files_dict.items():
        for file in v:
            with open(file, "rb") as f:
                content = f.read()
            save_hash(k, file, hashlib.md5(content).hexdigest())


def save_hash(key, file, hash_value):
    if files_hash.get(key):
        if files_hash[key].get(hash_value):
            files_hash[key][hash_value].append(file)
        else:
            files_hash[key].update({hash_value: [file]})
    else:
        files_hash.update({key: {hash_value: [file]}})


def print_hash():
    counter = 0

    for keys in sorted(files_hash, reverse=sorting):
        print(f"{keys} bytes")
        for k, v in files_hash[keys].items():
            if len(files_hash[keys].get(k)) >= 2:
                print(f"Hash: {k}")
                for file in v:
                    counter += 1
                    print(f"{counter}. {file}", end="\n")

        print()


if __name__ == '__main__':
    args = argv

    files_dict = {}
    files_hash = {}
    sorting = False

    get_args()
    get_inputs()

    if check_dup():
        get_file_hash()
        print_hash()