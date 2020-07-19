sam_s=7
sam_t=11
apple_a=5
orange_b=15
apple_no_m=3
orange_no_n=2
apples=[-2,2,1]
oranges=[5,-6]

def appleOrange():

    apple_position=[i+apple_a for i in apples if i+apple_a<=sam_t and i+apple_a>=sam_s]
    print(apple_position)
    orange_position = [i + orange_b for i in oranges if i + orange_b <= sam_t and i + orange_b >= sam_s ]
    print(len(orange_position),len(apple_position))

appleOrange()