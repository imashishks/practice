'''
Given a non negative  integer array, an element is deleted and the array is reshuffled.Find the missing element


'''

def missingelement(arr1,arr2):
    counter={}
   
    for val in arr1:
        if val in counter:
            counter[val]+=1
        else:
            counter[val]=1
    
    for v in arr2:
        if v in counter:
            counter[v]-=1

    
    for val in counter:
        if counter[val]:
            return val

    return "No missing element"

# print(missingelement([1,2,3,4,5],[3,1,4,5]))
# time compelxity - O(n)
        