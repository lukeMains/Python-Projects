size = int(input('Get the Lucky Numbers from 1 to: '))

luckyNum = []
for i in range(0, size):
    luckyNum.append(i + 1)
    
notDone = True
sieveNumIndex = 1
count = 1
sieveNum = luckyNum[sieveNumIndex]

while(notDone):
    j = 0
    count = 1
    while(j < len(luckyNum)):
        if(count == sieveNum):
            count = 1
            del(luckyNum[j])
        
        j += 1
        count += 1

    sieveNumIndex = 0
    while(sieveNumIndex < len(luckyNum)): 
        if(luckyNum[sieveNumIndex] > sieveNum):
            sieveNum = luckyNum[sieveNumIndex]
            sieveNumIndex = len(luckyNum)
        else:
            sieveNumIndex += 1

    if(sieveNum == luckyNum[len(luckyNum)-1]):
        notDone = False

print(luckyNum);
