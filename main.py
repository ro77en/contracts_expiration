import pandas as pd
import pickle


with open('./data/contracts.pkl', 'rb') as f:
    contracts_df = pickle.load(f)

print(contracts_df)