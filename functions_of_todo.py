FILEPATH='todos.txt'


def getTodos(filePath=FILEPATH):
    #this is a doc string describing the method and its function
    """ Read a txt file and return the list of
    to-do items
    """
    with open(filePath,'r') as file:
        todos=file.readlines()
    return todos

def writeTodos(todosArg,filePath=FILEPATH):
    """ Writes the to-do items to the file in the filepath"""
    with open(filePath,'w') as file:
        file.writelines(todosArg)


if __name__ == '__main__':
    print("Hello")
    print(getTodos())