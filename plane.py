from random import random


def arrive_plane(m, p):
    panne = 0
    for i in range(m):
        if random() < p:
            panne += 1
    return panne < m / 2

def choice(p):
    nb_simul = 50000
    a, b = 0, 0
    for v in range(nb_simul):
        a += arrive_plane(4, p)
        b += arrive_plane(2, p)
    if a == b:
        return 'AB'
    return 'A' if a > b  else 'B'

def execute():
    for p in range(0, 101, 1):
        print("if p = {}%, take the plane {}".format(p, choice(p/100)))


if __name__ == '__main__':
    print(execute())