def usdt_to_vnd(amount, rate=25000):
    return amount * rate

if __name__ == "__main__":
    print(usdt_to_vnd(10))  # Example: 10 USDT -> VND
