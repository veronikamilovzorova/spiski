from ast import Str
from datetime import date, datetime
from struct import pack
from unicodedata import digit
from random import *
#kahe nimekirja täitmine: taotlejad[], punktid[]
def patsiendid(i:list,v:list):
    """
    funktsioon mis lisab järjendusele nimesid ja teise järjendusele paneb random
    """
    n=int(input("Mitu inimest?"))
    for j in range(n):
        nimi=input("sisesta nimi")
        vitamiini=randint(10,100)
        i.append(nimi)
        v.append(vitamiini)
    return i,v
def suur_vaike(i:list,v:list):
    """
    leiab numbrid mis on <30
    """
    number=30
    for m in v:
        if m < number:
            ind=v.index(m)
            print(f"{m}, {i[ind]}")
def keskmine(i:list,v:list):
    """
    kõik liidetakse ja jagab kogus
    """
    kesk_d=sum(v)/len(v)
    print(f"on keskmine d vitamiini näitleja {kesk_d}")
    return i,v
def suurim_d_vitamiin(i:list,v:list):
    """
    teeb max vitamiini arvu ja pärast leiab palk indexit ja nimi indeksid
    """
    palk=max(v)
    ind=v.index(palk)
    nimi=i[ind]
    return palk,nimi
def search_patients_by_name(nimed, d_vitamiini_sisaldus):
    """
    ==nimi järjendusega
    """
def redact(i:list,v:list):
    """
    tehke loendis kolm esimest tähte suurtähtedega
    """
    ind=i.index[0]
    i[0].isupper()+i[3:]
    return i
