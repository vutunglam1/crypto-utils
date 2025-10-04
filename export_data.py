import json

def export_to_json(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    sample = {"wallet": "0xabc123", "balance": 500}
    export_to_json(sample)
