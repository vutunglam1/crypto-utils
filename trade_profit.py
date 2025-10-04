def calc_profit(buy_price, sell_price, amount):
    return (sell_price - buy_price) * amount

if __name__ == "__main__":
    print(calc_profit(20000, 25000, 2))  # Example profit
