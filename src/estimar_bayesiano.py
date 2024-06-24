import os
import pandas as pd
import matplotlib.pyplot as plt

folder_path = './results/dados_sentencas.xlsx'  # Replace with the actual path to the pena_dias folder

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