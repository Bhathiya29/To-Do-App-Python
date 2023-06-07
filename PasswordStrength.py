# PASSWORD STRENGTH APPLICATION

password=input('Please Enter A Password :')

def hasNumber(string):
    return any(i.isdigit() for i in string)

def hasUpper(string):
    return any(x.isupper() for x in string)

if len(password)>=8 and hasNumber(password) and hasUpper(password):
    print("PASSWORD IS STRONG")
else:
    print('PASSWORD IS WEAK')