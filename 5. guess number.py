import random
first = 1
second = 99
guess_number = 0
guess = random.randint(first, second)
print("my first guess is:", guess)
answer = input("what is the number in your head(don't enter it, just compare it with the number on the screen)? print c for correct, b for bigger and s for smaller! \n")
while answer != "c":
    if answer == "b":
        first = guess + 1 
        guess = random.randint(first, second)
        print(guess)
        guess_number =guess_number+1
    elif answer == "s":
        second = guess - 1 
        guess = random.randint(first, second)
        print(guess)
        guess_number =guess_number+1
    answer = input("what do you think about the new number? ")  
print("i guess in", guess_number )