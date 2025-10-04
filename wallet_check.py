def is_valid_wallet(address: str) -> bool:
    return address.startswith("0x") and len(address) == 42

if __name__ == "__main__":
    print(is_valid_wallet("0x1234567890abcdef1234567890abcdef12345678"))
