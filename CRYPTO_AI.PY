CRYPTO_AI = {
    "Name": "Crypto AI",
    "description": "A crypto bot that trades cryptocurrencies using AI algorithms.",
    "Version": "c 1.0"
}

crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": "3/10"  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": "6/10"  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": "8/10"  
    }  
}

# Origin of the bot 
question = "The question includes:\nName\nDescription\nVersion"
print(question)

# Questions the bot answers
questions1 = "The bot answers questions about:\n" \
             "1. Price trend of Bitcoin, Ethereum, or Cardano\n" \
             "2. Market capitalization of Bitcoin, Ethereum, or Cardano\n" \
             "3. Energy usage of Bitcoin, Ethereum, or Cardano\n" \
             "4. Sustainability score of Bitcoin, Ethereum, or Cardano"
print(questions1)


# user input
def get_crypto_info():
    print("Enter the name of the cryptocurrency you want to know about (Bitcoin, Ethereum, Cardano):")
    crypto_name = input().strip().capitalize()
    if crypto_name in crypto_db:
        print("Enter the information you want (price_trend, market_cap, energy_use, sustainability_score):")
        info_type = input().strip().lower()
        if info_type in crypto_db[crypto_name]:
            print(f"{info_type} of {crypto_name}: {crypto_db[crypto_name][info_type]}")
        else:
            print("Invalid information type")
    else:
        print("Invalid cryptocurrency name")

get_crypto_info()
