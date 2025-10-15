import threading


def task1():
    x = 0
    while x < 5:
        print('task 1')
        x += 1

def task2():
    x = 0
    while x < 5:
        print('task 2')
        x += 1

# A ordem dependera da disponibilidade do hardware, assim tendo ordens diferentes
threading.Thread(target=task1).start()
task2()