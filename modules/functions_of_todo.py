def getTodos(filePath='todos.txt'):
    #this is a doc string describing the method and its function
    """ Read a txt file and return the list of
    to-do items
    """
    with open(filePath,'r') as file:
        todos=file.readlines()
    return todos

def writeTodos(todosArg,filePath='todos.txt'):
    """ Writes the to-do items to the file in the filepath"""
    with open(filePath,'w') as file:
        file.writelines(todosArg)


print(__name__)