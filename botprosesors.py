import sys
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os

def main():
    getpage()
    #print("hello")

def getpage():

    r = requests.get('https://ksp.co.il/?select=.1027..2..42..4039.&kg=&list=1&sort=2&glist=1&uin=0&txt_search=&buy=&minprice=0&maxprice=0&intersect=&rintersect=&store_real=')
    #print(type(r.text))
    cardlist=printstuff(r.text)
    ##print(cardlist)
    fixed=fixlist(cardlist)
    #print(fixed)

    ##print("first list len"+str(len(cardlist)))
    #print("secend list len"+str(len(fixed)))
    #printlist(fixed)
    # print("")
    # print("")
    # print("")
    #printlist(fixed)
    fixed=fixlistb(fixed)
    # print("")
    # print("")
    # print("")
    #printlist(fixed)
    #print("can I buy the cpu I want (5600)in ksp:"+str(upgeade(fixed)))
    #os.system('cls')
    #os.system('clear')
    #printlist(fixlistb(fixed))
    #print(r.text.decode('UTF-8'))
    return fixed 

def upgeade(a):
    ret=False
    for i in a:
        if(i.find("5600")!=-1):
            ret=True
    return ret

def printlist(a):
    for i in a:
        print(i)

def fixlistb(a):
    for i in range(len(a)):
        a[i]=a[i][5:]
    return a    

def fixlist(a):
    b=[]
    b.append(a[0])
    add=True
    for i in range(len(a)):
        add=True
        for j in range(len(b)):
            if(b[j].find(a[i][:len(a[i])-7])!=-1):
                add=False
        
        if(add):
            b.append(a[i])
    return b
    



        
def printstuff(r):
    l=r.find("AMD")
    ret=[]
    while(l!=-1):
        a=r[l:].find("<")
        b=l
        while(r[b]!="<"):
            b=b-1
        #print(r[l-b:l+a])
        gpu=r[l-30:l+a]
        if(gpu.find("Box")!=-1):
            #print(r[l-20:l+a])
            #print("the > if in:"+str(gpu.find(">")))
            while(gpu.find(">")!=-1):
                gpu=gpu[gpu.find(">")+1:]
            #print(gpu)
            ret.append(gpu)
        
        r=r[l+20:]
        l=r.find("AMD")
    return ret

def openbrowser():
    print("")
    #browser  = webdriver.Chrome(ChromeDriverManager().install())
    #browser.get('https://ksp.co.il/index.php?select=.35.&kg=&list=1&sort=1&glist=1&uin=0&txt_search=rtx&buy=&minprice=0&maxprice=0&intersect=&rintersect=&store_real=')

    

main()