import random
def trap ():
    numbers_ = range(3, 21)
    stone_1 = random.choice(numbers_)
    return stone_1

n = stone_1 = trap()
print('Плита: ', stone_1)
print()

def get_key(number):
    password = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password

result = get_key(n)
print('Пароль:', result)



