#Iterative Approach
def binary_search(list,x):
    first= 0  
    last = len(list)

    while(first < last):
        mid=int((first + last)/2)
        if(list[mid]== x):
            return True  
        else:
            if(list[mid] > x):
                last= mid -1
            else:
                first=mid + 1
    return False

#Recursive Approach
def binary_search_recur(list,elem):
    if(len(list)==0):
        return False
    else:
        first=0
        last= len(list)
        mid= int((first+last)/2)
        if(list[mid]==elem):
            return True
        else:
            if(list[mid] > elem):
                return binary_search(list[:mid-1],elem)
            else:
                return binary_search(list[mid+1:],elem)

#print(binary_search_recur([5,3,6,72,46],56))
# False
#Time Complexity - Worst Case - O(nlogn), Best Case - O(1)