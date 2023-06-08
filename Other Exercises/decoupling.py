feetInches=input('Enter feet and inches :')

def parse(feet_inches):
    input =feet_inches.split(' ')
    feet =int(input[0])
    inches=int(input[1])
    return feet,inches # you get two values in a tuple returned or you can use a dictionary {'feet':feet,'inches':inches}


def convert(feetInches):
    inputs=feetInches.split(' ')
    feet=int(inputs[0])
    inches=int(inputs[1])

    meters=feet*0.3048 + inches*0.0254
    return f"{feet} feet and {inches} inches is equal to {meters} meters"

print(convert(feetInches))