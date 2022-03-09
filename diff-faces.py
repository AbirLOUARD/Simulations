from random import randint


def throw(n):
    draw = []
    for i in range(n):
        d = randint(1, 6)
        if d not in draw:
            draw.append(d)
    return len(draw)


def execute(n = 5):
    nb_simul = 50000
    faces = 0
    for i in range(nb_simul):
        faces += throw(n)
    return faces / nb_simul

if __name__ == '__main__':
    print(execute())

