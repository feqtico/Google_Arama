#!/usr/bin/python
# -*- coding: utf-8 -*-

from googlesearch import search


print("Google Arama Programına Hoş Geldiniz.")
  
word = input(" Aranacak Kelime Girin: ")

arama = word
  
for j in search(arama, tld="com", num=10, stop=10, pause=2):
    print(j)
