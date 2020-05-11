def conatinSubstring(s1,s2):
    if(s1[:len(s2)]==s2):
        return True
    elif(len(s1)>0):
        return conatinSubstring(s1[len(s2):],s2)
    else:
        return False

print(conatinSubstring('NETSETOS','SET '))