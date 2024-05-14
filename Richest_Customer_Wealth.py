#  Richest Customer Wealth  Problem Number : 1672

def  maximumWealth(accounts):
    all_sum = 0
    greater = []
    for i in range(len(accounts)):
        sum = 0
        for j in range(len(accounts[0])):
            sum = sum + accounts[i][j]

        greater.append(sum)
    return (max(greater))


accounts = [[2,8,7],[7,1,3],[1,9,5]]
max_w = maximumWealth(accounts)
print(max_w)

# Solution End


#blow is the test code for developing logic 


# accounts = [[1,5],[7,3],[3,5]]
 
# print()
# print()
# all_sum = 0
# greater = []
# for i in range(len(accounts)):
#     sum = 0
#     for j in range(len(accounts[0])):
#         sum = sum + accounts[i][j]
#     print(sum)
#     greater.append(sum)
# print(max(greater))

       

# print(accounts[1][2])

