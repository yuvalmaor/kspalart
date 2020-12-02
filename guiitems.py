import sys
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import tkinter as tk
import time
import botprosesors
import botgpu

def main():
    a=botprosesors.getpage()
    b=botgpu.getpage()

    while(botprosesors.upgeade(a)==False and botgpu.upgeade(b)==False):#need to be false
        time.sleep(10)
        a=botprosesors.getpage()
        b=botgpu.getpage()
    
    showfulllist()


def showfulllist():
    #window = tk.Tk()
    a=botprosesors.getpage()
    b=botgpu.getpage()
    p=""
    for i in a:
        p=p+"\n"+i
    p=p+"\n"
    p=p+"\n"
    p=p+"\n"
    for i in b:
        p=p+"\n"+i

    p=p+"\n"
    p=p+"\n"
    p=p+"\n"
    p=p+"can I buy the cpu I want (5600)in ksp:"+str(botprosesors.upgeade(a))+"\n"
    p=p+"can I buy the gpu I want(3060) in ksp:  "+str(botgpu.upgeade(b))

    #print("can I buy the cpu I want (5600)in ksp:"+str(botprosesors.upgeade(a)))
    #print("can I buy the gpu I want(3060) in ksp:  "+str(botgpu.upgeade(b)))
    greeting = tk.Label(text=p)
    #greeting= tk.
    greeting.pack()
    #getpage()
    #print("hello")

    greeting.mainloop()



main()