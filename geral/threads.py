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

# Onde a ordem dos prints sera misturado, pois existe outro thread executando ao msm tempo
threading.Thread(target=task1).start()
task2()