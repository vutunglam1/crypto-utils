from convert_usdt import usdt_to_vnd
from trade_profit import calc_profit
from transaction_fee import fee

if __name__ == "__main__":
    print("10 USDT to VND:", usdt_to_vnd(10))
    print("Trade profit:", calc_profit(20000, 25000, 2))
    print("Fee:", fee(1000))
