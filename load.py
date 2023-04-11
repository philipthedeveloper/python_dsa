def load_numubers(file_path):
    list = []
    with open(file_path, "r") as file:
        for line in file:
            list.append(int(line))
    return list
