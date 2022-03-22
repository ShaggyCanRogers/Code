print("""************************

Şekli Bulma Programı

Islemler:
Üçgen
Dörtgen

************************
""")

sekil = input("şekli seçin:")

if(sekil == "dörtgen"):
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    d = int(input("Kenar-4:"))

    if(a==b and a==c and a==d):
        print("Şekil karedir")
    elif((a==c and b==d) or (a==d and b==c) or (a==b and c==d)):
        print("Şekil dikdörtgendir")
    else:
        print("dörtgendir")


elif(sekil == "üçgen"):
    x = int(input("Kenar-1:"))
    y = int(input("Kenar-2:"))
    z = int(input("Kenar-3:"))
    if (abs(x + y) > z and abs(x + z) > y and abs(y + z) > x):
        if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
            print("İkizkenar üçgendir")
        elif(x==y==z):
            print("Eşkenar üçgendir")
        elif((x**2 + y**2 == z**2) or (x**2 + z**2 == y**2) or (y**2 + z**2 == x**2)):
            print("Diküçgendir")
        else:
            print("Çeşitkenar bir üçgendir")
    else:
        print("Bu ölçüler bir üçgen belirtmiyor")

else:
    print("Geçersiz bir şekildir")




























