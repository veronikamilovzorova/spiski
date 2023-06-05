import io
from os import *
from gtts import *
from random import *
from io

def loe (file):
    x={}
    x1={}
    with io.open(file,"r",encoding="utf-8-sig") as f:
        for line in f:
            k,v=line.strip().split('-')
            x[k]=v
            x1[v]=k
    return x,x1 

def heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("chinano.mp3") 
    system("chinano.mp3")
