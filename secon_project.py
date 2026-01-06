import os
os.system ("cls")

set1 = {"Artel","Alif","Yandex","Google","Meta"}
set2 = {"Google","Apple","Amazon","Meta"}
set3 = {"Alibaba","Uzum","Meta","Google","Amazon"}

set5 = set1.intersection(set2,set3)
set4 = set1.difference(set2,set3)
print(set5)

print(set4)


import os
os.system("cls")

set1={2,3,4,5,6}
set2={4,5,6,7,8,9}

set3=set1.symmetric_difference(set2)
print(set3)

summa=0
for i in set3:
    summa+=i
print(summa)


import os
os.system("cls")

set1={100, 20, 45, 80, 70, 50}
set2={30, 55, 70, 60, 20, 100}

set3= set1.intersection(set2)


for i in set3.copy():
    if i<60:
        set3.discard(i)

summa=0
sanash=0
for i in set3:
    summa+=i
    sanash+=1

print(summa/sanash)