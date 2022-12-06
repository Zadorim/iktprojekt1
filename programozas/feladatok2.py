#Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a legkisebb értéket ezek közül!
def feladat1():
    tomb =[]

    for i in range(3):
        tomb.append(int(input("Kérek egy számot")))
    
    print(f"A legkisebb elem: {min(tomb)} ")
    print(f"A legnagyobb elem: {max(tomb)} ")

    print("A legkisebb elem: "+str(min(tomb)))
    print("A legnagyobb elem: "+str(max(tomb)))

        
    #print(min(tomb))

    #tomb.sort()

    #print(tomb[0])

#feladat1()

# 2. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
# legnagyobb értéket ezek közül!
def feladat2():
    tomb =[]
    
    for i in range(3):
        tomb.append(int(input("Kérek egy számot")))
    

    #print(max(tomb))

    tomb.reverse()

    print(tomb[0])

#feladat2()


# 3. Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy
# érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.
def feladat3():

    while pontszam < 0 or pontszam > 100:
        pontszam = int(input("Kérem a dolgozatod pontszámát:"))

        if pontszam< 50:
            print("Elégtelen")
        elif pontszam < 60:
            print("Elégséges")
        elif pontszam < 70:
            print("Közepes")
        elif pontszam < 85:
            print("Jó")
        else:
            print("Jeles")

#feladat3()

# 4. Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre,
# hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!
def feladat4():
    oszthato = False

    szam = int(input("Kérek egy egész számot: "))

    if szam % 3 == 0 or szam % 5 == 0:
        oszthato = True

    if oszthato == True:
        print("Igen.")
    else:
        print("Nem.")
    
    #print(oszthato)

    #if szam%3 == 0:
        #print("A megadott szám osztható hárommal")
    #if szam%5 == 0:
       # print("A megadott szám osztható öttel")

#feladat4()

# 5. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre,
# hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!
def feladat5():
    a = int(input("Kérem a értékét:"))
    b = int(input("Kérem b értékét:")) 
    c = int(input("Kérem c értékét:"))  

    van = False
    if (a+b) == c:
        van=True
           
    if (a+c) == b:
        van=True 

    if (c+b) == a:
        van=True 
    
    if van:
        print("Van ilyen szám!")
    else:
        print("Nincs ilyen szám!")

#feladat5()

# 6. Írj egy Python programot, amely bekér három egész számot a felhasználótól és kiírja a
# képernyőre, hogy mind a három páros szám-e (igen/nem)!
def feladat6():
    #szam1,szam2,szam3 = input("Adj meg három számot: ").split()
    #szam1=int(szam1)
    #szam2=int(szam2)
    #szam3=int(szam3)

    #if szam1%2==0 and szam2%2==0 and szam3==0:
        #print("Igen,  mindhárom páros.")
    #else:
        #print("Nem mind páros szám.")

    a = int(input("Kérem a értékét:"))
    b = int(input("Kérem b értékét:")) 
    c = int(input("Kérem c értékét:")) 

    van = False
    if a%2 == 0 and b%2 == 0 and c%2 == 0:
        van = True

    if van:
        print("Az összes páros!")
    else:
        print("Van köztük páratlan!")        
         
#feladat6()

# 7. Írj egy Python programot, amely bekér két szót (sztringet) a felhasználótól és ABC sorrendben
# kiírja őket a képernyőre!
def feladat7():
    szavak=input("Adj meg két szót: ").split()

    print("A megadott szavak abc sorrendben: ")
    szavak.sort()
    for a in szavak:
        print(a)

#feladat7()



      











