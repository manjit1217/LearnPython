scores=[3 ,4 ,21, 36, 10, 28, 35, 5 ,24, 42
]
def breaking_record(scores):

    max_score=scores[0]
    min_score=scores[0]
    no_of_max=0
    no_of_min=0
    for i in range(1,len(scores)):
        if scores[i]>max_score:
            max_score=scores[i]
            no_of_max=no_of_max+1
        elif scores[i]<min_score:
            min_score=scores[i]
            no_of_min=no_of_min+1
    print(no_of_max,no_of_min)


def nonRepetiveChar(s):
    count=0
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if (s[i]==s[j]):
                count=count+1
        if(count<=1):
            print(s[i])
        count = 0

nonRepetiveChar('aabccd')