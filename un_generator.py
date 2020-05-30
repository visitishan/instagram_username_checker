# -*- coding: utf-8 -*-
"""
Created on Sat May 30 02:50:17 2020

@author: ishan.m.jain
"""

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]


f = open("usernames.csv", "a")

for char1 in alpha:
    for char2 in alpha:
        f.write(char1+char2+"\n")
f.close()



###############################################################################
#   for 3 char un
###############################################################################


alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","_","."]

print(alpha[:36])

f = open("usernames3.csv", "a")

for char1 in alpha[:36]:
    for char2 in alpha[:36]:
        for char3 in alpha[:37]:
            f.write(char1+char2+char3+"\n")
f.close()
