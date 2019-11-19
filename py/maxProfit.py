# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

# Example 2:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

def maxProfit(prices):
    # linear - maintain hill and peak and running max profit
    rMax = 0
    curi = 0

    while curi + 1 < len(prices) and  prices[curi] > prices[curi+1]:
        curi += 1

    if curi == len(prices):
        return 0
    
    hill = prices[curi]
    peak = hill
    # now hill = peak = 1        

    for i in range(curi, len(prices)):
        if prices[i] < hill:
            hill = prices[i]
            # since hill is reset, also reset the peak
            peak = prices[i]
        if prices[i] > peak:
            peak = prices[i]
        rMax = max(rMax, peak - hill)

    return rMax


result = maxProfit([2, 4, 1])
print('hi')