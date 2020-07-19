#scores=[100, 100, 50, 40, 40, 20, 10]
scores=[100 ,90 ,90, 80, 75, 60]
#allice_score=[5, 25, 50, 120]
allice_score=[50, 65, 77, 90, 102
]
def climbingLeaderboard(scores,allice_score):
    unique=list(set(scores))
    unique.sort(reverse=True)
    print(unique)
    for i in range(0,len(allice_score)):
        for j in range(0,len(unique)):
            if(allice_score[i]>=unique[j]):
                # if(allice_score[i]==unique[j]):
                #     print(allice_score[i],j+1)
                print (j+1)
                break
        else:print(len(unique)+1)


def climbscore(scores,alice):
    unique_scores = list(reversed(sorted(set(scores))))
    i = len(alice) - 1
    j = 0
    ans = []

    while i >= 0:
        if j >= len(unique_scores) or unique_scores[j] <= alice[i]:
            ans.append(j + 1)
            i -= 1
        else:
            j += 1

    return  reversed(ans)



climbingLeaderboard(scores,allice_score)
print(climbscore(scores,allice_score))