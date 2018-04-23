#psuedo code for depth first search . The concept here is to implement a backtracking pattern in which we visit one node and try to traverse all the neighbors of that vertex once it is done come back and follow the same on other vertices untill all the vertices are visited


# Iterative approach using a Stack 

def dfs_interative(G,s):
    let Stck be a stack
    
    Stck.push(s)
    mark s as visited

    while Stck is not empty:
        v = Stck.top()
        Stck.pop() # removing top vertices
        for all neighbors w of v :
             if w is not visited:
               
                S.push(w)
                 mark w as visited
             

# Recursive Approach 

def dfs_recursive(G,s):
    mark s as visited 
    for all neighbors w of s :
        if w is not visited:
            dfs_recursive(G,w)
        


