prime_guess = input("Guess a number you think is prime: ")
prime_guess = int(prime_guess)
higher_number = int(prime_guess) + 1

for x in range(2, higher_number):
    prime = True
    for y in range(2, x):
        if x % y == 0:
            prime = False
            y += 1
    if prime:
        if x == prime_guess:
            print("Correct", prime_guess, "is a prime number!")
            break
        else:
            x += 1