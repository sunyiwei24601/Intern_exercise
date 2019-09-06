def maxProfit(prices):
    max_profit = 0
    min_buy_price = max(prices) + 1
    for i in prices:
        if i < min_buy_price:
            min_buy_price = i
            continue
        else:
            max_profit = max(max_profit, i-min_buy_price)
    return max_profit
print(maxProfit([7,1,5,3,6,4]))



