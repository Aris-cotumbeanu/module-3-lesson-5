import random
playing = True
number = (random.randint(0,9))

print(" i will generate a number between 0 and 9, you have to guess it")
print("the game ends when u win!")
while playing:
    guess = input("give me your best guess: \n")
    if number == guess:
        print("you have won!")
        print (" the number was", number)
        break
    else:
        print("you havent guess right, you lose")
