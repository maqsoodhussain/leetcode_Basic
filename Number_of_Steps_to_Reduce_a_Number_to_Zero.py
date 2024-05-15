
# Number of Steps to Reduce a Number to Zero Problem Number : 1342
def fun(num):
    count = 0
    while (num != 0):
        if num % 2 == 0:
            num = num / 2  
        else:
             num = num-1

        count += 1
    print(count)
     
fun(8)
#print(123//2)