# -*- coding: utf-8 -*-
"""String methods

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h_6eUmD4dg9IlQHsngwYxaw6weavh9Zx
"""

#Slicing in python
name="Simranjeet Kaur"
print("My name is ",name,"it contains",len(name),"characters")
#here len is used to print the length of the string

color="Yellow"
length=len(color)
print("My dress is of",color,"and it has",length,"characters")
#here print is used to print the length of the string

print(color[0:5])
#here we are printing the string from 0 to 4 and slicing is used with square brackets
print(name[1:7])
#here slicinging is used from 1  to 5 index

print(name[:6])
#here if we skip 0th index,python automatically takes zero value

print(name[0:])
#here if we skip last index,python automatically takes last value

print(name[:])
#here if we just put : colon python automatically takes 0th index and last index

print(name[:-3])
#here python automatically takes len(name)-3, python uses -ve index from end of string
print(name[-4:-1])
#means last character is not included,print last 4 characters except last one(i.e.; -1)

print(name[-4:])
#means last 4 characters of string
#Slicing means:before colon is starting index and after colon is ending index
#-ve index means from end and +ve index means from beginning of string

print(name[0:6])  #including 0 but not 6

print(name[0:6:2])
#here 2 is the jump index, it means it will skip 1 character
print(name[0:11:3])
#similarly 3 is the jump index, it means it will skip 2 character

print(name[0:len(name)-3])
#means print(name[0:18-3]), it will remove last 3 characters

nm="marry"
print(nm[-4:-2])
#last 2 characters are not included from last 4 characters
print(nm[-4:3])
#last 4 and first 3 from marry,means arry and har now  union of  this  means ar, this  will be output
print(nm[3:-2])
#means first 3 and last 2 characters, means har and ry now union=nothing,output=empty