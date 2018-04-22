
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
    if(sorted(w1)==sorted(w2)):
        return True
    else:
        return False

#time complexity - O(nlogn) //the time complexity of sorted()
#print(anagram1("Here comes dots","The Morsse Code"))
#output - True