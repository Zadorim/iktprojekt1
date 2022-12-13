#Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a
#felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi
#a megadott szám értéke! 

#def feladat0():
    #szam=int(input("Kérek egy számot 1 és 20 között: "))
    #print(szam*" "+ "START")

#feladat0
#Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
#képernyőre azt a számot, amely az ennél a számnál nem nagyobb pozitív egész számok
#összege! 

#def feladat1():
    #szam=int(input("Adj meg egy pozitív egész számot!"))
    #tomb=[]
    #for i in range(szam):
        #tomb.append(szam)
        #szam-=1
    #print(sum(tomb))

#feladat1()

#Írj egy Python programot, amely bekér egy szót (sztringet) a felhasználótól és kiírja a
#képernyőre a szó betűit, úgy, hogy minden betű egy új sorba kerüljön! 
    
#def feladat2():
    #szo=(input("Adj meg egy szót! "))
    #for i in range(len(szo)):
        #print(szo[i])

#feladat2()

#Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
#képernyőre felváltva a 0 és 1 számjegyeket úgy, hogy a számjegyek együttes darabszáma
#pontosan a megadott szám legyen! 

#def feladat3():
    #szam=int(input("Adj meg egy pozitív egész számot! "))
    #e = False
    #for i in range(szam):       
        #print(int(e), end="")
        #e = not e

#feladat3()

#Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós
#számot a felhasználótól és kiírja a képernyőre azokat az egész számokat, amelyek a megadott
#értékek között helyezkednek el! 

#def feladat4():
    #szam1 = float(input("Adj meg egy számot! "))
    #szam2 =float(input("Adj meg egy újabb számot! "))

    #szam1 = int(szam1)
    #szam2 = int(szam2)

    #print("Számok, amelyek a megadott érékek között helyezkednek el.")
    #for i in range(min(szam1, szam2)+1, max(szam1, szam2)):
        #print(i)

#feladat4()

#Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre
#a csillag (*) karaktereket M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy
#téglalap alakú képernyőrészre)! A programodban hívd is meg ezt az alprogramot!

#def feladat5():
    #N=int(input("Adj meg egy egész számot! "))
    #M=int(input("Adj meg egy  újabb egész számot! "))
    #for i in range(M):
        #print(N*"*")

#feladat5()


feladat5()

