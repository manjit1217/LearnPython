from collections import Counter
#find the longest NOn repetive character in string
string="youasomez"
nonRepetiveString={}
i=0
maxlen=0
def allString(str):
    for i in range(0,len(str)+1):
        for j in range(0,len(str)+1):
         x=(str[i:j])
         print(x)
         checkNonrepetiveString(x)


def checkNonrepetiveString(singleString):
    x=Counter(singleString)
    global maxlen
    if((list(x.values()).__contains__(0 or 2 or 3)) ):
        pass
    else:
        if ((x.__len__())>maxlen ):
            maxlen=x.__len__()

            # print(maxlen)

allString('abhjdbajcc')

def solve(meal_cost, tip_percent, tax_percent):
    tip=meal_cost*(tip_percent/100)
    tax=meal_cost*(tax_percent/100)
    result=meal_cost+tip+tax
    print(result)
    print( round(result))
#
# solve(float(10.25),17,5)
#
#
# even=[]
# odd=[]
# def odd_even(s):
#     print(s[::2])
#     print(s[1::2])
#     for i in range(0,len(s),2):
#         even.append(s[i])
#     for j in range(1,len(s),2):
#         odd.append(s[j])
#     od=''.join(even)
#     ev=''.join(odd)
#     print(f'{od} {ev}')
#
#
# odd_even('hacker')

# arr=[1,2,3,4]
# rev=arr[::-1]
# print(rev)
# print(''.join(str(rev)))
# newl=[]
# for i in range(len(arr)-1, -1,-1):
#     newl.append(arr[i])
# print(*newl)
#
# print(" ".join(map(str, arr[::-1])))
#
# d={
#     'sam':21321,
#     'name2':4153,
#     'name3':452412
# }
# n=int(input())
# d=[input().split() for _ in range(n)]
# phonbook={k:v for k,v in d}

# print(d)
# for _ in range(n):
#     name,no=map(str,input().split())
#     if d.get(name) is None:
#         d[name] = no
#     else:
#         pass
# while True:
#     name=input()
#     if d.get(name) is None:
#         print('Not found')
#     else:
#         print(f'{name}={d.get(name)}')

#
#
# n=int(input())
# d=[input().split() for _ in range(n)]
# phonbook={k:v for k,v in d}
#
# while True:
#     try:
#         name=input()
#         if phonbook.get(name) is None:
#             print('Not found')
#         else:
#             print(f'{name}={phonbook.get(name)}')
#     except Exception as e:
#         print(e)
#         break



# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
#
