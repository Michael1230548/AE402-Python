# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:18:12 2020

@author: user
"""
import random
counter=0
answer = int(intput())
while True:
    a=int(input('請從1~20猜一個數字:'))
    if a==answer:
        print("恭喜猜對了")  
    else:
        print("猜錯了")
        counter=counter+1
        if counter >4:
            break