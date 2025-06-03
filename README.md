# AI_ASSIGNMENT

## CRYPTO AI CHATBOT

A simple Python chatbot that answers cryptocurrency-related questions using static data, natural language detection, and live price info from CoinGecko API.  
Includes logging of user interactions.

## Features

- Static crypto info for Bitcoin, Ethereum, and Cardano  
- Natural language question handling (trends, sustainability, live prices)  
- Fetches real-time prices via CoinGecko API  
- Logs all user interactions to `chat_log.txt`  

## Files in this Repo

| File                                      | Description                             |
| ----------------------------------------- | --------------------------------------- |
| `crypto_ai.py`                            | The main chatbot script                 |
| `chatbot_demo.png`                        | Screenshot or text log of a sample chat |
| `README.md`                               | This file                               |
| `chat_log.txt`                            | Stores user-bot chat history            |

## Usage

1. Clone or download this repo
2. Open `crypto_ai.py` in a terminal or IDE
3. Start chatting!
4. Running the bot:

```bash
python crypto_ai.py
```

### Interact via the command line. Type

1. Queries in natural language (e.g., **). Sample Questions You Can Ask:

- “Which crypto is most sustainable?”
- “What’s the energy usage of Bitcoin?”
- “Tell me the market cap of Ethereum.”
- “Is Cardano trending up?”
- "Which crypto is trending?"

2. `"info"` to look up specific crypto data  
3. `"exit"` to quit

## Requirements

- Python 3.x  
- `requests` library (`pip install requests`)

## ⚠️ Disclaimer

Crypto AI chatbot is for educational use only. Always do your own research (DYOR) before investing in any cryptocurrency.

## 📝 License

This project is licensed under the [MIT License](LICENSE).
