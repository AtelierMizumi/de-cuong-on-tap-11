# Bài 5

from posixpath import split


f=open("So.txt","r")
x=f.read()
so=x.split()
f.close
f=open("output.txt","a+")
f.write((so[0]) + (so[-1]))
f.close
