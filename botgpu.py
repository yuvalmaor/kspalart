import sys
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os

def main():
    #print(getpage())
    getpage()
    #print("hello")

def getpage():

    r = requests.get('https://ksp.co.il/index.php?select=.35.&kg=&list=1&sort=1&glist=1&uin=0&txt_search=rtx&buy=&minprice=0&maxprice=0&intersect=&rintersect=&store_real=')
    #print(type(r.text))
    cardlist=printstuff(r.text)
    #print(cardlist)
    fixed=fixlist(cardlist)
    #print(fixed)

    #print("first list len"+str(len(cardlist)))
    #print("secend list len"+str(len(fixed)))
    #printlist(fixed)
    #print("")
    #print("")
    #print("")
    os.system('cls')
    #os.system('clear')
    #printlist(fixlistb(fixed))
    #print("can I buy the cpu I want(3060) in ksp:  "+str(upgeade(fixed)))
    #print(r.text.decode('UTF-8'))
    fixed=fixlistb(fixed)
    #print(fixed)
    return fixed 

def upgeade(a):
    ret=False
    for i in a:
        if(i.find("3060")!=-1):
            ret=True
    return ret

def printlist(a):
    for i in a:
        print(i)

def fixlistb(a):
    for i in range(len(a)):
        a[i]=a[i][10:]
    return a    

def fixlist(a):
    b=[]
    b.append(a[0])
    add=True
    for i in range(len(a)):
        add=True
        for j in range(len(b)):
            if(b[j].find(a[i][:len(a[i])-1])!=-1):
                add=False
        
        if(add):
            b.append(a[i])
    return b
    



        
def printstuff(r):
    l=r.find("RTX")
    ret=[]
    while(l!=-1):
        a=r[l:].find("<")
        b=l
        while(r[b]!="<"):
            b=b-1
        #print(r[l-b:l+a])
        gpu=r[l-30:l+a]
        if(gpu.find("GB")!=-1):
            #print(r[l-20:l+a])
            #print("the > if in:"+str(gpu.find(">")))
            while(gpu.find(">")!=-1):
                gpu=gpu[gpu.find(">")+1:]
            #print(gpu)
            ret.append(gpu)
        
        r=r[l+20:]
        l=r.find("RTX")
    return ret

def openbrowser():
    print("")
    #browser  = webdriver.Chrome(ChromeDriverManager().install())
    #browser.get('https://ksp.co.il/index.php?select=.35.&kg=&list=1&sort=1&glist=1&uin=0&txt_search=rtx&buy=&minprice=0&maxprice=0&intersect=&rintersect=&store_real=')

    

main()