def fee(amount, rate=0.001):
    return amount * rate

if __name__ == "__main__":
    print(fee(1000))  # Example: fee for 1000 USDT
