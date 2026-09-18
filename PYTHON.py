n=int(input('enter limit:'))
male=[]
female=[]
for i in range(n):
    name=input('enter your name:')
    gender=input('enter F/M:')
    if gender=='M':
        male.append(name)
    else:
        print(name)
print(male)
