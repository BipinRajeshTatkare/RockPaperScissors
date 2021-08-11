# Project of Rock-Paper-Scissors

import random

print('''
        1. Rock
        2. Paper
        3. Scissor\n''')
person_1 = int(input('Enter Number For Side: '))
p_side = ""

if person_1 == 1:
    p_side = "Rock"
elif person_1 == 2:
    p_side = "Paper"
elif person_1 == 3:
    p_side = 'Scissor'
else:
    print("Invalid Number . Game is going to exit ...")
    exit()

comp_1 = random.randint(1, 3)
c_side = ""

if comp_1 == 1:
    c_side = "Rock"
elif comp_1 == 2:
    c_side = "Paper"
elif comp_1 == 3:
    c_side = 'Scissor'

if p_side == "Rock" and c_side == "Rock":
    print("your dice is : {} & comp dice is : {} , Tied !!".format(p_side, c_side))

if p_side == "Rock" and c_side == "Paper":
    print("your dice is : {} & comp dice is : {} , Computer Win !!".format(p_side, c_side))

if p_side == "Rock" and c_side == "Scissor":
    print("your dice is : {} & comp dice is : {} , You Win !!".format(p_side, c_side))

if p_side == "Paper" and c_side == "Rock":
    print("your dice is : {} & comp dice is : {} , You Win !!".format(p_side, c_side))

if p_side == "Paper" and c_side == "Paper":
    print("your dice is : {} & comp dice is : {} , Tied !!".format(p_side, c_side))

if p_side == "Paper" and c_side == "Scissor":
    print("your dice is : {} & comp dice is : {} , Computer Win !!".format(p_side, c_side))

if p_side == "Scissor" and c_side == "Rock":
    print("your dice is : {} & comp dice is : {} , Computer Win !!".format(p_side, c_side))

if p_side == "Scissor" and c_side == "Paper":
    print("your dice is : {} & comp dice is : {} , You Win !!".format(p_side, c_side))

if p_side == "Scissor" and c_side == "Scissor":
    print("your dice is : {} & comp dice is : {} , Tied !!".format(p_side, c_side))