from random import randint


def get_rand():
    return randint(0, 100)


def get_imdb_movies(x):
    x = get_rand()
    if x > 10:
        return x + 5
    return x - 5
