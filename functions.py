def get_todos(filepath='todos.txt'):
    # open and read a file using 'with' context manager
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_list, filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_list)





if __name__ == "__main__":
    print("This is a module")