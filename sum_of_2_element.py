no = [1, 1, 4, 4,6,2]
sum = 8



def sum_of_array_ele(list,sum):
    length=len(list)-1
    no1=0
    no2=length
    while no1<no2:
        s=list[no1]+list[no2]
        if s == sum:
         print(list[no1],list[no2])
         break
        elif(s>sum):
            no2=no2-1
        elif s<sum:
            no1=no1+1

    print(list[no1],list[no2])



sum_of_array_ele(no,sum)