def u1(p1,p2,p3):
    print("""
Medelpoäng på prov
==================

""")
    print("Medelpoäng på de tre proven blev {0:.1f}".format(p := (p1+p2+p3)/3))
    if p > 90:
        print("Bra jobbat")
        return True
    return False

def u2(kg,meter):
    print("""
Beräkning av BMI
================

""")
    bmi = kg/(meter**2)
    print("BMI är {0:.1f}".format(bmi))
    if (bmi < 18.5):
        print("Undervikt")
        return 1
    elif 18.5 <= bmi and bmi < 25:
        print("Normalvikt")
        return 2
    elif 25 <= bmi and bmi < 30:
        print("Övervikt")
        return 3
    else:
        print("Fetma")
        return 4

def u4(pris):
    if (pris < 10):
        print("Billigt")
    elif(10<=pris<15):
        print("Full tank")
    elif(15<=pris<20):
        print("Tio liter")
    else:
        print("Sälh bil och cykla istället")

def u5(year):
    if year%4==0:
        print("{} är ett skottår".format(year))

def u6(age,inkomst,betalningsanmärkning):
    if (age > 18 and inkomst >= 120 and not betalningsanmärkning):
        print("Fakturabetalning beviljad")
    else:
        print("Tyvärr kan vi inte bevilja fakturabetalning")

def u7(age, inkomst, betalningsanmärkning):    
    deny = lambda: print("Tyvärr kan vi inte bevilja fakturabetalning")
    if (age < 18):
        deny()
        return

    if (inkomst < 120):
        deny()
        return

    if (betalningsanmärkning):
        deny()
        return
        
    print("Fakturabetalning beviljad")

uppgift = {
    1: lambda: u1(float(input("Poäng på första provet: ")),float(input("Poäng på andra provet: ")),float(input("Poäng på tredje provet: "))),
    2: lambda: u2(float(input("Vikt (kg): ")),float(input("Längd (meter): "))),
    4: lambda: u4(int(input("Bensinpris (liter/kr): "))),
    5: lambda: u5(int(input("Årtal: "))),
    6: lambda: u6(int(input("Ålder: ")),int(input("Bruttoinkomst (tusental kronor): ")),input("Betalningsanmärkning (J/N):") == "J"),
    7: lambda: u7(int(input("Ålder: ")),int(input("Bruttoinkomst (tusental kronor): ")),input("Betalningsanmärkning (J/N):") == "J")
}

def chooseUppgift(u):
    if (u not in uppgift):
        print("Ogiltig uppgift")
    else:
        uppgift[u]()

    
#chooseUppgift(int(input("Välj uppgift: ")))