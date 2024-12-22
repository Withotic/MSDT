import asyncio
import random as rnd
import os

#показывает занятость заказом соответственно: плиты, фритюра и чайника
busy = [-1,-1,-1]

#длительность цикла
cycle = 2

async def burger():
    await asyncio.sleep(cycle*3.8)
    task=tasks[busy[0]]
    if(not task[0] and not task[1] and not task[2]):
        task[3]=False
    busy[0]=-1

async def free():
    await asyncio.sleep(cycle*2.8)
    task=tasks[busy[1]]
    if(not task[0] and not task[1] and not task[2]):
        task[3]=False
    busy[1]=-1

async def dosh():
    await asyncio.sleep(cycle*1.8)
    task=tasks[busy[2]]
    if(not task[0] and not task[1] and not task[2]):
        task[3]=False
    busy[2]=-1

async def main(tasks):
    
    while True:
        os.system('cls')
        # генерация заказа
        task=[rnd.randint(0,3)==0,rnd.randint(0,2)==0,rnd.randint(0,1)==0,True]
        if(not task[0] and not task[1] and not task[2]):
            task[3]=False
        tasks.append(task)
    
        print("Плита: "+("свободна" if busy[0]==-1 else "занята заказом "+str(busy[0])))
        print("Фритюр: "+("свободен" if busy[1]==-1 else "занят заказом "+str(busy[1])))
        print("Чайник: "+("свободен" if busy[2]==-1 else "занят заказом "+str(busy[2])))
        
        i=0
        print("┌заказы─────────────────────────┐")
        for task in tasks:
            if(not task[0] and not task[1] and not task[2]):
                if(task[3]):
                    print("|"+str(i)+" заказ выполняется")
                else:
                    print("|"+str(i)+"----------------")
            else:
                print("|"+str(i)+" заказ:"+" бургер"*task[0]+" картошка"*task[1]+" дошик"*task[2])
                
            if task[0] and busy[0]==-1:
                task[0]=False
                busy[0]=i
                asyncio.create_task(burger())
            if task[1] and busy[1]==-1:
                task[1]=False
                busy[1]=i
                asyncio.create_task(free())
            if task[2] and busy[2]==-1:
                task[2]=False
                busy[2]=i
                asyncio.create_task(dosh())
            i+=1
        print("└───────────────────────────────┘")
        i=0
        

        await asyncio.sleep(cycle)


print("Добро пожаловать в Бургерную дяди Никиты!\n")

print("В меню есть блюда:")
print("  0: бургер - занимает плиту, готовится 4 цикла")
print("  1: картошка - занимает фритюр, готовится 3 цикла")
print("  2: дошик - занимает чайник, готовится 2 цикла\n")

print("Каждый цикл случайно генерируется заказ")

print("Enter чтобы продолжить")

input()
tasks=[]
# Запускаем event loop
asyncio.run(main(tasks))