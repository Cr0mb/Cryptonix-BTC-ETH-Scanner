from colorama import Fore, init  
from hdwallet import HDWallet  
from hdwallet.symbols import BTC, ETH
import random  
import requests  
import os  
import time  
import platform  
from pyfiglet import Figlet  

init(autoreset=True)

def title():
    f = Figlet(font='standard')  
    print(Fore.LIGHTCYAN_EX + f.renderText("Cryptonix") + Fore.RESET)

def get_clear():
    if 'win' in platform.platform() or 'Windows' in platform.platform():
        os.system('cls')
    elif 'linux' in platform.platform() or 'Linux' in platform.platform():
        os.system('clear')
    elif 'darwin' in platform.platform():
        os.system('clear')
    elif 'mac' in platform.platform() or 'Mac' in platform.platform():
        os.system('clear')
    else:
        raise ValueError('Not Supported Platform: "%s"' % platform.platform())

def eth_balance(addr: str) -> str:
    url = f"https://ethereum.atomicwallet.io/api/v2/address/{addr}"
    try:
        req = requests.get(url).json()
        ret = dict(req)['balance']
        return int(ret) / 1000000000000000000
    except KeyError:
        print("Error: Failed to fetch Ethereum balance.")
        return 0

def get_balance(addr):
    rl = f"https://bitcoin.atomicwallet.io/api/v2/address/{addr}"
    try:
        req = requests.get(rl).json()
        ret = dict(req)['balance']
        return int(ret) / 10000000000
    except KeyError:
        print("Error: Failed to fetch Bitcoin balance.")
        return 0


def main():
    get_clear()  
    print(Fore.GREEN, "Starting...", Fore.RESET)  
    time.sleep(2)  

    z = 1  
    ff = 0  
    while True:
        try:
            private_key = "".join(random.choice("0123456789abcdef") for _ in range(64))
            hd_btc: HDWallet = HDWallet(BTC)
            hd_eth: HDWallet = HDWallet(ETH)
            hd_btc.from_private_key(private_key)
            hd_eth.from_private_key(private_key)

            eth_addr = hd_eth.p2pkh_address()
            btc_addr1 = hd_btc.p2pkh_address()
            btc_addr2 = hd_btc.p2wpkh_address()
            btc_addr3 = hd_btc.p2wpkh_in_p2sh_address()
            btc_addr4 = hd_btc.p2wsh_in_p2sh_address()
            btc_addr5 = hd_btc.p2sh_address()

            value5 = get_balance(btc_addr5)
            value4 = get_balance(btc_addr4)
            value3 = get_balance(btc_addr3)
            value2 = get_balance(btc_addr2)
            value1 = get_balance(btc_addr1)
            val_et = eth_balance(eth_addr)

            get_clear()
            title()

            print(Fore.YELLOW, "Discord: cr0mbleonthegame", Fore.RESET)
            print(f"Scan: {z} Found: {ff}")

            print(f"{Fore.WHITE}BTC Address (P2PKH)  | BAL: {Fore.MAGENTA}{value1} | {Fore.YELLOW}{btc_addr1}")
            print(f"{Fore.WHITE}BTC Address (BECH32) | BAL: {Fore.MAGENTA}{value2} | {Fore.YELLOW}{btc_addr2}")
            print(f"{Fore.WHITE}BTC Address (P2WPKH) | BAL: {Fore.MAGENTA}{value3} | {Fore.YELLOW}{btc_addr3}")
            print(f"{Fore.WHITE}BTC Address (P2WSH)  | BAL: {Fore.MAGENTA}{value4} | {Fore.YELLOW}{btc_addr4}")
            print(f"{Fore.WHITE}BTC Address (P2SH)   | BAL: {Fore.MAGENTA}{value5} | {Fore.YELLOW}{btc_addr5}")
            print(f"{Fore.WHITE}ETH Address (ETH)    | BAL: {Fore.MAGENTA}{val_et} | {Fore.YELLOW}{eth_addr}")
            print(f"{Fore.WHITE}Private Key (HEX)    | {Fore.MAGENTA}{private_key}")
            print("=" * 70)

            z += 1  

            if value1 > 0:
                ff += 1
                open('btcWin.txt', 'a').write(f'{btc_addr1}\n{private_key}\n')
            elif value2 > 0:
                ff += 1
                open('btcWin.txt', 'a').write(f'{btc_addr2}\n{private_key}\n')
            elif value3 > 0:
                ff += 1
                open('btcWin.txt', 'a').write(f'{btc_addr3}\n{private_key}\n')
            elif value4 > 0:
                ff += 1
                open('btcWin.txt', 'a').write(f'{btc_addr4}\n{private_key}\n')
            elif value5 > 0:
                ff += 1
                open('btcWin.txt', 'a').write(f'{btc_addr5}\n{private_key}\n')
            elif val_et > 0:
                ff += 1
                open('btcWin.txt', 'a').write(f'{eth_addr}\n{private_key}\n')
            else:
                continue
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Restarting...")
            time.sleep(5)
            main()

if __name__ == "__main__":
    main()
