# TDD with python - TAFT

'''
regras

1 - se for multiplo de 3 retorna fizz
2 - se for multiplo de 5 retorna buzz
3 - se for multiplo de 3 e de 5: fizzbuzz
4 - se não: retorna o número

'''
from functools import partial


def multiple_of(base, num): return num % base == 0


multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def robot(number):
    anum = str(number)

    if multiple_of_5(number) and multiple_of_3(number):
        anum = 'fizzbuzz'
    elif multiple_of_3(number):
        anum = 'fizz'
    elif multiple_of_5(number):
        anum = 'buzz'

    return anum
