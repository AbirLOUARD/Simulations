from random import randint

def succes(n):
    day = []
    for i in range(n):
        d = randint(1, 366)
        if d in day:
            return 1
        day.append(d)
    return 0

def simul(n):
    total = 0
    nb_simul = 5000
    for k in range(nb_simul):
        total += succes(n)
    return total / nb_simul

def execute():
    mini, maxi = 2, 367
    while maxi - mini > 1:
        n = (mini + maxi) // 2
        p = simul(n)
        print("{} person : {:03.2f} %".format(n, 100*p))
        if p > .5:
            maxi = n
        elif p > .5:
            mini = n
        else:
            break

if __name__ == '__main__':
    print(execute())