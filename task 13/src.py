import requests

def fetch_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def format_report(data, keyword=None):
    lines = ["📊 Bitcoin Price Report", "--------------------------"]
    # Coindesk format
    if "bpi" in data:
        bpi = data.get("bpi", {})
        for code, info in bpi.items():
            if keyword and keyword.lower() not in code.lower() and keyword.lower() not in info.get("description", "").lower():
                continue
            symbol = info.get("symbol", "")
            rate = info.get("rate", "")
            lines.append(f"{code}: {symbol}{rate}")
    # Exchangerate format
    elif "rates" in data:
        rates = data.get("rates", {})
        for code, rate in rates.items():
            if keyword and keyword.lower() not in code.lower():
                continue
            lines.append(f"{code}: {rate}")
    else:
        lines.append("No currency data found.")
    return "\n".join(lines)

def save_report(report, filename="btc_price_report.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)

def main():
    url = input("Enter API URL (or press Enter for default): ").strip()
    if not url:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = fetch_data(url)
    if not data:
        return
    keyword = input("Filter by keyword (optional): ").strip()
    report = format_report(data, keyword if keyword else None)
    print(report)
    save_report(report)
    print("\nReport saved to btc_price_report.txt")
if __name__ == "__main__":
    main()