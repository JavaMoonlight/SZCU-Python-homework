# 寻找bug
import random
guess = ''
while guess not in('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

# 此处应该加上str到int数据的转化，否则下面的if判断一直就是False
# if guess == 'heads':
#     guess = 1
# else:
#     guess = 0

toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()

    # 此处应该加上str到int数据的转化，否则下面的if判断一直就是False
    # if guess == 'heads':
    #     guess = 1
    # else:
    #     guess = 0

    if toss == guess:
        print('You got it!')
    else:
        print('Nope! You are really bad at this game.')