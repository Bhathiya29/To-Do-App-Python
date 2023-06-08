# CLI To-Do APP
#from functions_of_todo import getTodos, writeTodos

import time

print('-------------------------------------- To-Do APP -----------------------------------------')
print('\n')



run=True
#todo=[]

#userInput = input('Please Enter the To-Do Item :')
#todo.append(userInput)

now=time.strftime('%b %d, %Y %H:%M:%S')
print("It is ", now)

#Option Logic Of the App
while(run):

    response=input('Type Add,Show,Edit,Complete or Stop:')
    response=response.strip().upper()


    if 'ADD'in response or 'NEW' in response:
        try:
                # using list slicing from the index 4 to get the todo item after add
                userInput = response[4:]+'\n' #input('Please Enter the To-Do Item :') +"\n"

                #file=open('todos.txt','r')
                #todo=file.readlines() #readlines will return a list .read() is the method to read a single string
                #file.close()

                with open('todos.txt','r') as file:
                    todo=file.readlines()

                todo.append(userInput)

                #file=open('todos.txt','w') #creating a file object and writing to it with 'w'
                #file.writelines(todo) #method writelines is used to put a list if you want to write a string file.write() is the method
                #file.close()

                #with context manager is simple and safer than manually opening and closing
                with open('todos.txt','w') as file:
                    file.writelines(todo)
        except :
            print('There was a problem with the program, Please Re run ')

    elif 'SHOW'in response or 'DISPLAY' in response:
        try:
               #listno=1
                #for index,item in enumerate(todo):
                    #print('List Item ',listno,' is ',i)
                    #listno+=1
                    #print(f"{index +1}-{item}")
                file=open('todos.txt','r')
                new_todos=[]
                for item in file:
                    new_item=item.strip('\n') #removing the space of each item
                    new_todos.append(new_item)

                #list comprehension
                # new_todos=[item.strip('\n') for item in file]

                for index,item in enumerate(new_todos):
                    print(f"{index}-{item}")
                file.close()
        except:
            print(' There was a problem with the program, Please Re run ')


    elif 'EDIT' in response or 'CHANGE' in response:
        editResponse=input('Select the Element You want to Edit or Index of it')
        editResponse1=input('Enter the Changed Item you want to add:')

        todo=[]

        with open('todos.txt','r') as file:
            for item in file:
                strippedItem=item.strip('\n')
                todo.append(strippedItem)


        index = todo.index(editResponse)
        print('Testing index ', index)
        todo[index] = editResponse1

        with open('todos.txt','w') as file:
            for i in todo:
                file.write(i+'\n')

        print('Your Change is Done')

    elif 'COMPLETE' in response or 'DONE' in response:
        completedInput=input('Please Enter the Completed Task :')
        dummyList=[]
        with open('todos.txt','r') as file:
            for item in file:
                dummy=item.strip('\n')
                dummyList.append(dummy)


        #print('input ',completedInput) working
        #print('list',dummyList) working
        #print(dummyList.index(completedInput)) working
        dummyList.remove(completedInput)
        with open('todos.txt','w') as file:
            for item in dummyList:
                file.write(item +'\n')

        print('Successfully Removed ', completedInput)

    elif 'STOP' in response or 'EXIT' in response:
        run=False
        break

    else:
        print('The Command Entered is Not Valid, Please Try Again')

print('\n')
print('Thank you for using the APP')





print('\n')
print('-------------------------------------- To-Do APP -----------------------------------------')

