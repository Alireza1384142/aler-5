import random

num = int(input ('Adad esm ro bede :'))

listClass = [] 

for z in range(1,num +1) :

    name = input(f'Asme dansh amooz {z} :')

    listClass.append(name)

aler = listClass.pop(random.randrange(len (listClass)))

print(aler,'has died ')