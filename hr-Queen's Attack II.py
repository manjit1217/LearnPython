from pprint import pp
no_size_of_chess=5
k_abstacle=3
r_queen_posi=4
c_queen_posi=3
obstcles=[(5,5),(4,2),(2,3),3,2]
def queensAttack(n, k, r_q, c_q, obstacles):
    chess_dict={}
    for r in range(1,n+1):
        chess_dict[r,c_q]=1
    for c in range(1,n+1):
        chess_dict[r_q,c]=1

    for i in range(1,n+1):
        for j in range(1,n+1):
            if r_q==i and c_q==j:
                chess_dict[i,j]='q'
            elif (i,j) in obstcles:
                chess_dict[i,j]=1






    print(chess_dict)
queensAttack(no_size_of_chess,k_abstacle,r_queen_posi,c_queen_posi,obstcles)


