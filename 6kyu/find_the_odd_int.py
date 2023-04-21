def find_it(seq):
    #Odd nummer ifra -101 til 101
    #odd = [x for x in seq if seq.count(x)%2 != 0]
    #Odd nummer i seq
    #return odd[0]
    occur = []
    for x in seq:
        if seq.count(x) %2 != 0:
            occur.append(x)
    return occur[0]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))