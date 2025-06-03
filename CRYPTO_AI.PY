import requests
from datetime import datetime

# --- Bot Info ---
CRYPTO_AI = {
    "Name": "Crypto AI",
    "Description": "A crypto bot that answers questions using static and live data.",
    "Version": "v1.0"
}

# --- Static Dataset ---
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3 / 10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6 / 10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8 / 10
    }
}

# --- Logging ---
def log_interaction(user_input, response):
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("chat_log.txt", "a", encoding="utf-8") as log:
            log.write(f"[{timestamp}]\nUser: {user_input}\nBot: {response}\n\n")
    except Exception as e:
        print(f"⚠️ Logging failed: {e}")

# --- Live Price Fetch ---
def fetch_live_price(coin_id):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        price = data[coin_id]["usd"]
        return f"💰 Live price of {coin_id.capitalize()}: ${price}"
    except Exception as e:
        return "❌ Unable to fetch live price."

# --- Natural Language Handler ---
def handle_natural_query(query):
    query = query.lower()

    if "sustainable" in query or "green" in query:
        coin = max(crypto_db, key=lambda c: crypto_db[c]["sustainability_score"])
        response = f"🌱 {coin} is the most sustainable option!"

    elif "trending" in query or "rising" in query:
        trending = [c for c in crypto_db if crypto_db[c]["price_trend"] == "rising"]
        response = "📈 These coins are trending up: " + ", ".join(trending)

    elif "price" in query and "live" in query:
        if "bitcoin" in query:
            response = fetch_live_price("bitcoin")
        elif "ethereum" in query:
            response = fetch_live_price("ethereum")
        elif "cardano" in query:
            response = fetch_live_price("cardano")
        else:
            response = "Please specify which coin you'd like the live price for."

    elif "tell me about" in query:
        for coin in crypto_db:
            if coin.lower() in query:
                info = crypto_db[coin]
                response = f"{coin} info:\n" + "\n".join(f"{k}: {v}" for k, v in info.items())
                break
        else:
            response = "Sorry, I don't recognize that coin."

    else:
        response = "🤔 Try asking about trends, sustainability, or live prices!"

    print(response)
    log_interaction(query, response)

# --- Direct Info Lookup ---
def get_crypto_info():
    print("\n🪙 Choose from Bitcoin, Ethereum, Cardano or type 'back' to return:")
    crypto_name = input("Crypto: ").strip().capitalize()

    if crypto_name.lower() == "back":
        return

    if crypto_name in crypto_db:
        print("Enter info type (price_trend, market_cap, energy_use, sustainability_score):")
        info_type = input("Info: ").strip().lower()

        if info_type in crypto_db[crypto_name]:
            result = crypto_db[crypto_name][info_type]
            response = f"{info_type.replace('_', ' ').title()} of {crypto_name}: {result}"
        else:
            response = "❌ Invalid info type."
    else:
        response = "❌ Unknown cryptocurrency."

    print(response)
    log_interaction(crypto_name + " - " + info_type, response)

# --- Main Bot Loop ---
def start_bot():
    print("\n🤖 Welcome to Crypto AI!")
    for k, v in CRYPTO_AI.items():
        print(f"{k}: {v}")

    print("\n🔎 You can:")
    print("- Ask natural language questions (e.g., 'Which crypto is trending?')")
    print("- Type 'info' to look up specific crypto data")
    print("- Type 'exit' to quit")

    while True:
        user_input = input("\n🧠 Ask something: ").strip()

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break
        elif user_input.lower() == "info":
            get_crypto_info()
        else:
            handle_natural_query(user_input)

# --- Run Bot ---
if __name__ == "__main__":
    start_bot()

