seq = ['a', 'b', 'c', 'd', 'e']
def first(seq, n): 
    l = []
    for i in range(0,n):
        if n >= len(seq):
            l.append(seq[i]) 
    return l
        
