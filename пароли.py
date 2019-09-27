#!/usr/bin/env python
import random
 
Big_S=list('QWERTYUIOPASDFGHJKLZXCVBNM')
Low_S=list('qwertyuiopasdfghjklzxcvbnm')
Num_S=list('1234567890')
#Spe_S=list('!@#$%^&amp;*()')
 
lb=1 #Количество символов с верхним регистром
ll=3 #Количество символов с нижним регистром
ln=2 #Количество цифр
ls=0 #Количество спец символов
 
Pass=""
PassA=""
 
def Big():
    for i in range(lb):
        global Pass
        n=random.randrange(len(Big_S))
        Pass=Pass+Big_S[n]
    return Pass
 
def Low():
    for i in range(ll):
        global Pass
        n=random.randrange(len(Low_S))
        Pass=Pass+Low_S[n]
    return Pass
 
def Num():
    for i in range(ln):
        global Pass
        n=random.randrange(len(Num_S))
        Pass=Pass+Num_S[n]
    return Pass
 
def Spe():
    for i in range(ls):
        global Pass
        n=random.randrange(len(Spe_S))
        Pass=Pass+Spe_S[n]
    return Pass
 
def All():
    global PassA
    if lb>0:
        PassA=Big()
    if ll>0:
        PassA=Low()
    if ln>0:
        PassA=Num()
    if ls>0:
        PassA=Spe()
    PassR=list(PassA)
    random.shuffle(PassR)
    PassEnd=""
    for i in range(len(PassR)):
        PassEnd=PassEnd+PassR[i]
    return PassEnd
 
print (All())

