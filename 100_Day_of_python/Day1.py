import random
""" print("what is your name?")
name_obj =input("=> :")
print("hello" , name_obj)
print(len(input("what is your name?"))) """
def guess_number():
    number = random.randrange(1,24,1)
    print("guess a number between 1 and 10")
    guess = int(input("=> :"))
    if guess == number :
        print("you win" +" The correct answer is " + " " + str(number))
    else:
        print("you lose" +" The correct answer is " + " " + str(number))

guess_number()
fruit = ["apple", "orange", "pineapple", "cucumber"]
fruit_len = len(fruit)
for i in range(fruit_len):
    print(fruit[i])



