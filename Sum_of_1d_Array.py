
#leetcode problem : 1480

def suma(li):
    sum = 0 
    l2 = []
    for i in range(len(li)):
        sum =  sum + li[i]
        l2.append(sum)
    print(l2)
        

l = [1,2,3,4]
suma(l)