def MaxProfit(prices):
    total_profit = 0
    if len(prices) == 0:
        return 0
    min_buy_price = prices[0]
    max_sold_price = prices[0]
    max_profit = 0
    for i in prices[1:]:
        if i < max_sold_price:
            min_buy_price = i
            max_sold_price = i
            total_profit += max_profit
            max_profit = 0
        elif i >= max_sold_price:
            max_sold_price = i
            max_profit = max(max_profit, i - min_buy_price)
    return total_profit + max_profit
print(MaxProfit([1,2,3,4,5]))