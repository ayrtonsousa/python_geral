# NORMAL 5 segundos

# import time

# def sleep():
#     print(f'Time: {time.time() - start:.2f}')
#     time.sleep(1)

# def sum(name, numbers):
#     total = 0
#     for number in numbers:
#         print(f'Task {name}: Computing {total}+{number}')
#         sleep()
#         total += number
#     print(f'Task {name}: Sum = {total}\n')

# start = time.time()
# tasks = [
#     sum("A", [1, 2]),
#     sum("B", [1, 2, 3]),
# ]
# end = time.time()
# print(f'Time: {end-start:.2f} sec')


# ASYNC ERRADO E CERTO 

import asyncio
import time

# ERRADO 5 segundos
# async def sleep():
#     print(f'Time: {time.time() - start:.2f}')
#     time.sleep(1)

# CERTO 3 segundos
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')


# No caso 1 e no caso 2, eles são "iguais": "dormem" sem permitir que outros usem os recursos. Já no caso 3, 
# permite o acesso aos recursos quando está adormecido.

# No caso 2, adicionamos asyncà função normal. No entanto, o loop de eventos o executará sem interrupção . 
# Por quê? Porque não dissemos onde o loop pode interromper sua função para executar outra tarefa.

# No caso 3, informamos ao loop de eventos exatamente onde interromper a função para executar outra tarefa. 
# Onde exatamente? Bem aqui!: await asyncio.sleep(1)

