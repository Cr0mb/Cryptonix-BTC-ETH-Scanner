```
These projects are intended solely for educational purposes to help individuals understand the principles of cryptography and blockchain technology. It is important to recognize that attempting to generate Bitcoin wallets in the hope of randomly finding one with a balance is not a feasible strategy. This same logic applies to any tool that tries to work in any way the same as this.

The number of possible Bitcoin wallet combinations exceeds 76 trillion, making the odds of discovering an active wallet astronomically low. To put it into perspective, you are statistically far more likely to win the lottery every day for the rest of your life than to recover even a single wallet with funds—even over the course of a decade.
```


![image](https://github.com/Cr0mb/Cryptonix-BTC-ETH-Scanner/assets/137664526/648e5cd6-6e42-4e35-bf84-8ef2f541d124)

[Video](https://www.youtube.com/watch?v=SUHOJcKalz0&t=91s)

```Direct URL: https://www.youtube.com/watch?v=SUHOJcKalz0&t=91s```

# Cryptonix

Cryptonix is a Python tool for generating Bitcoin and Ethereum addresses along with their corresponding private keys. It scans for balances on these addresses and displays the results. If a balance is found, it saves the successful combinations to a file named btcWin.txt.

## Features

- Generates Bitcoin (BTC) and Ethereum (ETH) addresses
- Scans for balances on generated addresses
- Displays balances along with corresponding addresses and private keys
- Saves successful combinations to btcWin.txt

## Installation
1. Clone the repository:
```
git clone https://github.com/Cr0mb/Cryptonix-BTC-ETH-Scanner.git
```
2. Navigate to the directory
```
cd Cryptonix-BTC-ETH-Scanner
```
3. Install the required dependencies:
```
pip install colorama hdwallet requests pyfiglet
```
## Usage
1. Run the script:
```
python Cryptonix.py
```
2. Wait for the tool to generate addresses, scan for balances, and display results.
3. Successful combinations will be saved to btcWin.txt.

# Notes
- This tool is for educational purposes only. Use it responsibly and at your own risk.
- Ensure you have a stable internet connection for balance scanning.
- Make sure to handle generated private keys securely.


