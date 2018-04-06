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

#print(binary_search([5,3,6,72,46]))
#Time Complexity - Worst Case - O(nlogn), Best Case - O(1)