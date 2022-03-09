from random import random

def triangle(p):
    [a,b,c] = p
    return (a < b + c) and (b < a + c) and (c < a + b)

def position():
    broken = [random(), random()]
    a = min(broken)
    c = 1 - max(broken)
    b = 1 - a - c
    return [a, b, c]

def execute():
    nb_simul = 100000
    succes = 0
    for k in range(nb_simul):
        succes += triangle(position())
    return succes / nb_simul

if __name__ == '__main__':
    print(execute())

