def reverse_words_order_and_swap_cases(sentence):
    word=sentence.split(' ')
    newRevList=[]
    for j in range(0,len(word)):
        x=word[j]
        # newStr = []
        newStr1=[a.lower() if a.isupper() else a.upper() for a in x]
            # if(x[i].islower()):
            #     newStr.append((x[i]).upper())
            # elif(x[i].isupper()):
            #     newStr.append(x[i].lower())
        newRevList.append(''.join(newStr1))
    newRevList.reverse()
    print (' '.join(newRevList))


reverse_words_order_and_swap_cases('aWESOME is cODING')