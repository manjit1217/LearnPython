import sys
import json
#
# def file():
#     try:
#         f=open("demo.txt","r")
#         print(f.readlines())
#         print(f.read())
#     finally:
#         f.close()
#
#
with open("demo.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
with open('demo.txt','r') as f:
    for i in f:
        print(i)
