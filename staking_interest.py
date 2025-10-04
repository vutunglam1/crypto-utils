def staking(amount, rate, days):
    return amount * (rate/100) * (days/365)

if __name__ == "__main__":
    print(staking(1000, 12, 30))  # 1000 USDT, 12% APR, 30 days
