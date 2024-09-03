# Print Max profit from the given array of stock prices - Leetcode Problem: Best Time to Buy and Sell Stock II


# prices = [5,7,2,9]
# prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
prices = [1,2,3,4,5] # This test case only not work well with my code

n = len(prices)
profit = []
i = 0
while i < n-1:
    print(f"Index: {i}")
    print(f"Price: {prices[i]}")
    if prices[i]<prices[i+1]:
        profit.append(prices[i+1] - prices[i]) 
        print(f"Profit: {profit}")    
        i = i+1  # Skip the next index since we made a profit
    else:
        print(f"Loop exited because buy:{prices[i]} > sell:{prices[i+1]} ")
        i+=1 # Move to the next element

print(f"Final Profit list: {profit}")
print(f"Max Profit: {sum(profit)}")


# prices = [7,6,4,3,1]
# n = len(prices)
# profit = 0

# for i in range(n - 1):
#     if prices[i] < prices[i + 1]:
#         profit += prices[i + 1] - prices[i]

# print(f"Max Profit: {profit}")
