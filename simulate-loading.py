from time import sleep
from random import randint

def make_string(loading):
    return f" Loading... {loading}% "


def simulate1():
    # using \r
    loading = 0
    while loading < 100:
        sleep_time = randint(1, 5)
        increase_loading = randint(1, 8)
        print(make_string(loading), end="")
        print("\r", end="")
        loading += increase_loading
        sleep(sleep_time)
    print(make_string(100))

def simulate2():
    # using \b
    loading = 0
    while loading < 100:
        sleep_time = randint(1, 5)
        increase_loading = randint(1, 8)
        loadstr = make_string(loading)
        print(loadstr, end="")
        print('\b'*len(loadstr), end='', flush=True)
        loading += increase_loading
        sleep(sleep_time)
    print(make_string(100))


def make_str_loading(loading, loading_bar_length):
    size_per_character = 100//loading_bar_length
    filling_character = '#'
    notfilled_character = ' '
    num_of_characters = loading//size_per_character
    loaded =  filling_character*num_of_characters + notfilled_character*((100//size_per_character)-num_of_characters)
    return " |" + loaded + f"| {loading}% "

def simulate_loading(loading_bar_length=50):
    # using \b
    loading = 1
    print(" Loading..")
    while loading < 100:
        sleep_time = randint(1, 3)
        increase_loading = randint(1, 8)
        loadstr = make_str_loading(loading, loading_bar_length)
        print(loadstr, end="")
        print('\b'*len(loadstr), end='', flush=True)
        loading += increase_loading
        sleep(sleep_time)
    print(make_str_loading(100, loading_bar_length))

if __name__ == '__main__':
    simulate_loading()
