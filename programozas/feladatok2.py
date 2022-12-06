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

def feladat2():
    tomb =[]
    
    for i in range(3):
        tomb.append(int(input("Kérek egy számot")))
    

    #print(max(tomb))

    tomb.reverse()

    print(tomb[0])

#feladat2()

def feladat3()








