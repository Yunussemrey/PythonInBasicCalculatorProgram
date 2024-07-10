# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 22:25:47 2024

@author: YUNUS EMRE
"""

print("Basit hesap makinesi: ")

sayi1 = float(input("Lütfen ilk sayıyı giriniz : "))
sayi2 = float(input("Lütfen ikinci sayıyı giriniz : "))

# işlem fonksiyonları 
def top(a,b):
    toplam = a + b
    return print(a,"+",b,"=",toplam)
def carp(a,b):
    carpim = a * b
    return print(a,"*",b,"=",carpim)
def bol(a,b):
    bolum = a / b
    return print(a,"/",b,"=",bolum)
def cikar(a,b):
    cikarma = a - b
    return print(a,"-",b,"=",cikarma)

islem = str(input("Lütfen yapmak istediğiniz işlemi giriniz : "))

if islem == "+":
    top(sayi1,sayi2)
if islem =="-":
    cikar(sayi1, sayi2) 
if islem =="*":
    carp(sayi1, sayi2)
if islem =="/":
    bol(sayi1, sayi2)
