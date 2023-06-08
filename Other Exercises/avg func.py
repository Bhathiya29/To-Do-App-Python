def calculateAvg(fileName):
    with open(fileName, 'r') as file:
        numbers = 0
        iter = 0
        for num in file:
            numbers = numbers + int(num)
            iter += 1

    return numbers / iter


# avg=calculateAvg('numbers.txt')

# print(avg)

def calcAvg(fileName):
    with open(fileName) as file:
        data = file.readlines()

        listOfData = data[1:]
        listOfData = [int(i) for i in listOfData]

    return listOfData


fileN = input("What file would you like to calculate the average of? ")
print(calcAvg(fileN))


def greet(name, age):
    print(f"Hello! {name} Happy Birthday on your {age} Birthday")


greet(name='Steve', age=20)

# multi line strings
text="""
Principles of Success:
1.Focus
2.Good Habits
3.Perseverance
"""

multiLineText="""
This is a
Multi-line 
Text
"""

print(text)
print(multiLineText)