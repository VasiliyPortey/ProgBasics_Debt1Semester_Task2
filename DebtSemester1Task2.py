from random import randint

#Сдача задолженности по дисциплине "Основы программирования", первый семестр,
#задача вторая, вариант 6
#splitListToTwo - функция, которая делит заданный масив на две равные части (пополам)

def splitListToTwo(someList):
    firstHalf = []
    secondHalf = []
    for i in range(0, len(someList)//2):
            firstHalf.append(someList[i])
    if len(someList)%2==1:
        middleNumber = someList[len(someList)//2]
        for i in range(len(someList)//2+1, len(someList)):
            secondHalf.append(someList[i])
        print('Первая половина: ', firstHalf)
        print('Середина (длина массива нечётная): ', middleNumber)
        print('Вторая половина: ', secondHalf)
    else:
        for i in range(len(someList)//2, len(someList)):
            secondHalf.append(someList[i])
        print('Первая половина: ', firstHalf)
        print('Вторая половина: ', secondHalf)

listLength = int(input('Введите длину массива: '))
numbersList = []
for i in range(listLength):
    numbersList.append(randint(-10, 10))
print('Сгенерированный массив: ', numbersList)
splitListToTwo(numbersList)