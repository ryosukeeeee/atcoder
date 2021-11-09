s = input() 
charcters = set(s)

size = len(charcters)
if size == 3:
    print(6)
elif size == 2:
    print(3)
else:
    print(1)