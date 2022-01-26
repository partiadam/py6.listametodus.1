'''
1.1 Feladat
A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!
paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

1.2 Feladat
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást, hogy pontosan hányszor szerepel a felhasználó által megadott szín a listában!

1.3 Feladat
Egészítsük ki az előbbi programot úgy, hogy a kiértékelést követően a felhasználó által megadott szín kerüljön felvételre a listába, és csak ezután történjen meg a lista tartalmának kiírása!
------
Adj meg egy színt!
A megadott szín szerepel a listában.
A megadott szín nem szerepel a listában.
A lista színei:
'''

paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

megkerd = input('Adj meg egy színt: ')
if megkerd in paletta:
    print('A szín szerepel a listában: ')
    for szin in paletta:
        print(szin + ', ', end="")
    szamlalo = 0
    for szin in paletta:
        if megkerd == szin:
            szamlalo += 1
    print(f'A megadott szín {szamlalo}-szor szerepel a listában.') 
else:
    print('A szín nem található a listában.')
    paletta.append(megkerd)
    for szin in paletta:
        print(szin + ', ', end="") 
    for szin in paletta:
        print(szin + ', ', end="")
    szamlalo = 0
    for szin in paletta:
        if megkerd == szin:
            szamlalo += 1
    print(f'A megadott szín {szamlalo}-szor szerepel a listában.')