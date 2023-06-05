from module1 import *
nimed=[]
d_vitamiini_sisaldus=[]
while True:
    menu=int(input("Valik:\n1-lisa andmed\n"))
    if menu==0:
        break
    elif menu==1:
        nimed,d_vitamiini_sisaldus=patsiendid(nimed,d_vitamiini_sisaldus)
        print(nimed)
        print(d_vitamiini_sisaldus)
        menu=int(input("Valik:\n1-lisa andmed\n2 soretterib bolnih\n3 keskmine d vitamiini näitleja\n4 suurim_d_vitamiin\n"))
        if menu==0:
            break
        elif menu==1:
            nimed,d_vitamiini_sisaldus=patsiendid(nimed,d_vitamiini_sisaldus)
            print(nimed)
            print(d_vitamiini_sisaldus)
        elif menu==2:
            suur_vaike(nimed,d_vitamiini_sisaldus)
        elif menu==3:
            keskmine(nimed,d_vitamiini_sisaldus)
        elif menu==4 :
            palk,nimi=suurim_d_vitamiin(nimed, d_vitamiini_sisaldus)
            print(f"suurim vitamii d {palk} {nimi}")
        elif menu==5:
            search_patients_by_name(nimed,d_vitamiini_sisaldus)
        elif menu==6:
            nimed,d_vitamiini_sisaldus=redact(nimed,d_vitamiini_sisaldus)
            print(f"{nimed} {d_vitamiini_sisaldus}")
               
