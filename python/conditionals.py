import random 
user_input = int(input("Guess a number: "))
print(user_input)

magic_number = random.randint(0,10)

if user_input == magic_number:
    print("YOU GOT IT!!!")
else:
    print("BZZZZZZZ WRONG!!! It was %d" % (magic_number))
