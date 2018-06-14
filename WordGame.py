import random
word_guess =' '
word_list = ['LONG', 'CAR', 'HOUSE', 'HORSE', 'MONEY']
word_result = random.choice(word_list)
correct = word_result
print(word_result)
while word_result:
    posit = random.randrange(len(word_result))
    word_guess += word_result[posit]
    word_result = word_result[:posit] + word_result[(posit + 1):]
print("Tip:",word_guess)
answer = input("Your answer?").upper()
if answer == correct:
    print("Hura")
else:
    print(":(")

