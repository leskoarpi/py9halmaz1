'''
1. Feladat
Adott két függvény (y=2x+3 és y=3x+1), mindkettő értelmezési tartománya az egész számok [0;10] intervallumon. 
A program készítsen egy-egy halmazt a függvények értékkészleteivel, írja ki ezeket a képernyőre, majd jelenítse meg a halmazok metszetét, unióját és különbségét!
'''
x = [int(i) for i in range(11)] 
y = set()
y1 = set()

for szam in x:
    yy = (2 * int(szam) ) + 3
    y.add(yy)
    
    yy1 = (3 * int(szam) ) + 1
    y1.add(yy1)

print(y)
print(y1)
print()
print(y & y1)
print(y | y1)
print(y - y1)