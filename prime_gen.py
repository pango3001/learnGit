import math

higher_number = int(input("Highest number to generate list to: ")) + 1
listingNum = 1

for x in range(2, higher_number):
    prime = True
    for y in range(2, int(math.sqrt(x))+1):
        if x % y == 0:
            prime = False
    if prime:
        print(listingNum, ": ", x, sep="")
        listingNum += 1