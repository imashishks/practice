
'''
Two words are anagrams of one another if their letters can be rearranged to form the other word.

Example - 
Dormitory = Dirty room
The Morse Code = Here comes dots
'''

#Approach 1 - Sort the words and compare


def anagram1(w1,w2):
    w1= w1.replace(' ','').lower()
    w2= w2.replace(' ','').lower()
    if(len(w1) != len(w2)):
        return False
    if(sorted(w1)==sorted(w2)):
        return True
    else:
        return False

#time complexity - O(nlogn) //the time complexity of sorted()
#print(anagram1("Here comes dots","The Morsse Code"))
#output - True

def anagram2(w1,w2):
    w1= w1.replace(' ','').lower()
    w2= w2.replace(' ','').lower()
    # if(len(w1) != len(w2)):
    #     return False
    counter={}
    for letter in w1:
        if letter in counter:
            counter[letter]+=1
        else:
            counter[letter]=1

    for letter in w2:
        if letter in counter:
            counter[letter]-=1
        else:
            counter[letter]=1

    for key in counter:
        if counter[key]!=0:
            return False 
    return True   


# print(anagram2("god","dog"))
# Time complexity - O(n) where n is length of trimmed string