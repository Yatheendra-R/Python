import random
sel=random.randint(0,3)
animal=['deer','monkey','cow','kangaroo']
for a in animal:
    for aa in range(0,sel):
        print(a,end=" ")
    print()
