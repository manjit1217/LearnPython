#no_of_element_list=int(input('Enter the no of list'))
#=int(input('Enter the No of Left operation'))
no_of_element_list_rotation=list(map(int,input().split()))
array=list(map(int,input().split()))
left_roated_array=[None]*len(array)

def left_rotation(array,no_of_left_rotation,):
    for i in range(0,len(array)):
        new_index=(i+no_of_left_rotation)%len(array)
        left_roated_array[i]=array[new_index]
    print(left_roated_array)

left_rotation(array,no_of_element_list_rotation[1])
