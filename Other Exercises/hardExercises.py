# Coin flip Program


sideInput=input('Throw the coin and enter head or tails here :').upper() +'\n'

with open('results.txt', 'w') as file:
    file.writelines(sideInput)

with open('results.txt', 'r') as file:
    sideResults=file.readlines()

print('Test 1', sideResults)

run=True

while run:

    input1 = input('Do you want to enter more entries ?').upper()


    match input1:
        case 'YES':
            sideInput = input('Throw the coin and enter head or tails here :').upper() + '\n'
            with open('results.txt', 'a') as file:
                file.writelines(sideInput)
            run=True
        case 'NO':
            run=False
            with open('results.txt', 'r') as file:
                sideResults=file.readlines()
            for index,result in enumerate(sideResults):
                print(f"{index}-{result}")

        case whatever:
            break

with open('results.txt', 'r') as file:
    for line in file:
        temp=line.strip('\n')
        sideResults.append(temp)
    #sideResults.strip('\n')
    #print(sideResults)
    percentage=int((sideResults.count('HEAD')/len(sideResults))*100)
    print(len(sideResults))
    print(f"{percentage}%")
