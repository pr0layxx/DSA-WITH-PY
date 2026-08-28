prices=[7,1,5,3,9,4]
def maxProfit(prices):    
    max_profit=  0
    buy_index= 0
    best_buy_index =0
    best_sell_index = 0
    for i in range(len(prices)):
        if prices[i] < prices[buy_index]:
            buy_index = i
        else:
            profit = prices[i]- prices[buy_index]
            if profit > max_profit:
                max_profit= profit
                best_buy_index = buy_index
                best_sell_index= i
                
    return (best_buy_index + best_sell_index)
        

print(maxProfit(prices))