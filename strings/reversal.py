'''
Reverse a sentence 
Input - This is the best
Output - best the is This

'''

#Approach 1
def reversal(strr):
    # strr=strr.strip()
    words=[]
    temp=""
    for i in range(0,len(strr)):
        if strr[i] == " ":
            words.append(temp)
            temp = ""
        else:
            temp+=strr[i]

        if i == len(strr) -1:
            words.append(temp)
    print(words)
    print(' '.join(words[::-1]))

#print(reversal("   This is the best"))

#Approach 2

def reversal2(strr):
    words=[]
    start=0
    i=0
    while i <len(strr):
        if strr[i] != " ":
            start= i
            while i <len(strr) and strr[i] != " " :
                i+=1
            words.append(strr[start:i])
        i+=1
    return words

#print(reversal2("   This is the best"))
