prices=[1,2,4]
def maxProfit(prices):
    max_profit= 0
    min_price=prices[0]
    for j in range(1 , len(prices)):
        if prices[j]< min_price:
            min_price= prices[j]
        else:
            profit= (prices[j]- min_price)
            if profit > max_profit:
                max_profit= profit
    return max_profit
    

print(maxProfit(prices))