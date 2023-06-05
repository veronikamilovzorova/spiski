from module1 import *
palgad=[1200,2500,750,395,3200]
inimesed=["A","B","C","D","E"]
while True:
    menu=int(input("Valik:\n 1-Lisa andmed\n"))
    if menu==0:
        break
    elif menu==1:
        inimesed,palgad=Lisa_andmed(inimesed,palgad)
        print("inimesed")
        print("palgad")
        menu=int(input("Valik:\n1-Lisa andmed\n2-Kustuta andmed\n3-Suurim palk\n4 väikdem\n5 sorteeritud\n"))
        if menu==0:
            break
        elif menu==1:
            inimesed,palgad=Lisa_andmed(inimesed,palgad)
        elif menu==2:
            inimesed,paqlgad=kustutamine(inimesed,palgad)
        elif menu==3:
            palk,nimi=suurim_palk(inimesed, palgad)
            print(f"suurim palk on{palk} {nimi}´l")
        elif menu==4:
            palk,nimi=väike_palk(inimesed,palgad)
            print(f"väiksem palk on{palk} {nimi}´l")
        elif menu==5:
            inimesed,palgad=sorteerimine(inimesed,palgad)
            print(f"sorteeritud palk on {palk} {nimi}")
        elif menu==12:
            palgad, inimesed==Sorteerimine(palgad,inimesed)
            print(inimesed,palgad)
        elif menu==13:
            inimesed, palgad=Kustuta(inimesed, palgad)