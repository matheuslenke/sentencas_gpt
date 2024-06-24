import pandas as pd


def extract_sentence_times():
    # Read the CSV file into a dataframe
    df = pd.read_csv('data/datas/datas.csv', sep=';')

    # Loop through each row
    for index, row in df.iterrows():
        years = row[0]
        months = row[1]
        days = row[2]
        final_value = (years * 365) + (months * 30) + days
        print(final_value)