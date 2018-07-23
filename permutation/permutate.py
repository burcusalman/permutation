from random import choice
from random import sample


def head_or_tail():
    """

    :return:
    """
    v0 = ['HEAD','TAIL']
    v1 = choice(v0)
    return v1


def rock_paper_scissors():
    """

    :return:
    """
    v0 = ['ROCK','PAPER','SCISSORS']
    v1 = sample(v0, 2)
    print('1. '+v1[0]+'\n2. ' +v1[1])
    if(v1[0] == 'ROCK' and v1[1] == 'SCISSORS') or (v1[1] == 'ROCK' and v1[0] == 'SCISSORS'):
        return ('ROCK win SCISSORS lose')
    if(v1[0] == 'PAPER' and v1[1] == 'SCISSORS')or (v1[1] == 'PAPER' and v1[2] == 'SCISSORS'):
        return ('SCISSORS win PAPER lose')
    if(v1[0] == 'ROCK' and v1[1] == 'PAPER') or (v1[0] == 'PAPER' and v1[1] == 'ROCK'):
        return ('PAPER win ROCK lose')


def dice_roll(v0):
    """
    :param v0:
    :return:
    """
    v1 = []
    for i in range(int(v0)):
        dice = ['1','2','3','4','5','6']
        v2 = choice(dice)
        v1.append(v2)
    return v1


print(dice_roll(5))
print(rock_paper_scissors())
print(head_or_tail())





