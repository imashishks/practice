'''
Given an integer array ,Output all unique pairs, that sum upto a specific value k

For example - pair_sum([1,2,3,2],4)
Output - (1,3)(2,2)
'''

#Approach 1
def pair_sum(arr,k):
    occured=set()
    for val1 in arr:
        for val2 in arr:
            if val1 + val2 == k:
                temp="{0}{1}".format(val1,val2)
                temp= ''.join(sorted(temp))
                if temp not in occured:
                    print("({0},{1})".format(val1,val2))
                    occured.add(temp)
                   


# here a set is maintained to keep track of value(which is sorted so both 13 and 31 are same)
# Time complexity - O(n^2) as there are two loops(nested).



