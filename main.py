from datetime import datetime, timedelta
import pandas as pd
import pickle


with open('./data/contracts.pkl', 'rb') as f:
    contracts_df = pickle.load(f)

def fetch_contracts(contracts_df, search):
    # today = datetime.now().date()
    # using contracts before 2015 for tests
    before_2015_contracts = datetime.strptime('2015-01-01', '%Y-%m-%d').date()
    if search == 1:
        expired = contracts_df[ contracts_df['END_DATE'] < before_2015_contracts ]
        print(expired)

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

