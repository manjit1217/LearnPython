x=[2,1,5,3,4]



def minimumBribes(Q):
    moves = 0
    print(list(enumerate(Q)))
    Q = [P-1 for P in Q]
    print(list(enumerate(Q)))

    for i,P in enumerate(Q):
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1,0),i):
            if Q[j] > P:
                moves += 1
    print(moves)
minimumBribes(x)