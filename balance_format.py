def format_balance(amount):
    return f"{amount:,.2f} USDT"

if __name__ == "__main__":
    print(format_balance(1234567.89))
