import argparse
import asyncio
import pandas as pd
import matplotlib.pyplot as plt

from src.extract_data import extract_data
from src.json_to_csv import load_all_jsons
from src.run_llms import change_category, run_llms
from src.calculate_date import calculate_dates, date_to_csv
from src.extract_sentences_time import extract_sentence_times

folder_path = './dados_sentencas.xlsx'  # Replace with the actual path to the pena_dias folder

def get_data():
    df = pd.read_excel(folder_path, sheet_name=None)
    combined_df = pd.concat(df.values(), ignore_index=True)
    return combined_df

def clean_data(df: pd.DataFrame):
    df = df[df['tempo_preso'] != 0]
    return df

def estimar_bayesiano():
    combined_df = get_data()
    combined_df.describe()
    combined_df = clean_data(combined_df)

    unique_crimes = combined_df['tipo_crime'].unique()
    fig, ax = plt.subplots(len(unique_crimes), 1, figsize=(10, 8))

    for i, crime in enumerate(unique_crimes):
        ax[i].hist(combined_df[combined_df['tipo_crime'] == crime]['tempo_preso'], bins=10)
        ax[i].set_xlabel('Pena em Dias')
        ax[i].set_ylabel('Frequência')
        ax[i].set_title(f'Histograma da Distribuição de Pena em Dias para o Crime: {crime}')

    plt.tight_layout()
    plt.show()
    fig, ax = plt.subplots(figsize=(10, 8))
    for i, crime in enumerate(unique_crimes):
        ax.hist(combined_df[combined_df['tipo_crime'] == crime]['tempo_preso'], bins=10, alpha=0.5, label=crime)
    ax.set_xlabel('Pena em Dias')
    ax.set_ylabel('Frequência')
    ax.set_title('Histograma da Distribuição de Pena em Dias para Diferentes Crimes')
    ax.legend()
    plt.tight_layout()
    plt.show()


def main():
    '''
        This is a CLI application that allows the user to download data, run the LLM model, and convert the JSON files to CSV.
        The data is related to criminal sentences and the LLM model is used to extract some information from each sentence.
    '''
    parser = argparse.ArgumentParser(description='CLI App')
    parser.add_argument('command', choices=['download-data', 'run-llms', 'json-to-csv', 'get-dates', 'extract-sentence-time', 'infer'], help='Choose a function to run')
    parser.add_argument('-t', '--type', choices=['furto_simples', 'furto_qualificado', 'roubo_simples', 'roubo_majorado'], help='Specify the crime type')
    args = parser.parse_args()

    if args.command == 'download-data':
        asyncio.run(extract_data())

    elif args.command == 'run-llms':
        if args.type:
            change_category(args.type)

            asyncio.run(run_llms())
        else:
            print("Please provide the -t argument for crime type.")
            
    elif args.command == 'json-to-csv':
        if args.type:
            load_all_jsons(args.type)
        else:
            print("Please provide the -t argument for crime type.")

    elif args.command == 'get-dates':
        if args.type:
            # calculate_dates(args.type)
            date_to_csv(args.type)
        else:
            print("Please provide the -t argument for crime type.")
    
    elif args.command == 'extract-sentence-time':
        extract_sentence_times()

    elif args.command == 'infer':
        estimar_bayesiano()

if __name__ == '__main__':
    main()