from omamodule import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
while True:
    print(inimesed)
    print(palgad)
    menu=int(input("Valik:\n1-lisa andmed\n2-Kustuta andmed\n3-Suurim palk\n4-Min palk kellel\n5-Sort"))
    if menu==0:
        break
    elif menu==1:
        inimesed, palgad=Lisa_andmed(inimesed,palgad)
    elif menu==2:
        inimesed, palgad=Kustutamine(inimesed,palgad)
    elif menu==3:
        palk,nimi=Suurim_palk(inimesed,palgad) 
        print(f"Suurim palk on {palk} {nimi}´l")
    elif menu==4:
        palk, nimi=vaiksem_palk(inimesed,palgad)
    elif menu==5:
        inimesed,palgad=sorteerimine(inised,palgad)



