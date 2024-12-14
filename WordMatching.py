def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr=ctr+1
            lst.append(word)
    print("List of words with first and last characters same:", lst)
    return ctr
count=match_words(["abc","xyz","919","ghg"])
print("Numbers of words having the first and last characters same:", count)