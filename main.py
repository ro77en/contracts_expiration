from datetime import datetime, timedelta
import pandas as pd
import pickle


with open('./data/contracts.pkl', 'rb') as f:
    contracts_df = pickle.load(f)

def fetch_contracts(contracts_df, search):
    today = datetime.now().date()
    if search == 1:
        print(today)

def send_email():
    pass

def main():
    print("""Search for:
          1 - Expired contracts\n
Type the corresponding number.""")
    search = int(input())
    fetch_contracts(contracts_df, search)

if __name__ == '__main__':
    main()

