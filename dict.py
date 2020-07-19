name='manjittijnam'
name2='manjitmanjit'
dic={}
a=True
for i in name:
    dic[i]=name.count(i)


print(dic.fromkeys('m'))

for j in name2:
    x=name2.count(j)
    if dic[j]==x:
            a=True
    else:
        a=False
        break
print(a)
print(dic)