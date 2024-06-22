import os
import pandas as pd
import matplotlib.pyplot as plt

folder_path = './penas_dias'  # Replace with the actual path to the pena_dias folder

def get_data():
    files = os.listdir(folder_path)
    dfs = []
    for file in files:
        if file.endswith('.csv'):
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path, delimiter=';')
            dfs.append(df)
    combined_df = pd.concat(dfs)
    return combined_df

def estimar_bayesiano():
    combined_df = get_data()
    combined_df.describe()

    mean_approximation = combined_df['Pena em Dias'].mean()
    print("Mean of Pena em Dias:")
    print(mean_approximation)

    mean_by_categoria = combined_df.groupby('Crime')['Pena em Dias'].mean()
    print("\nMean of Pena em Dias by Categoria:")
    print(mean_by_categoria)

    std_by_categoria = combined_df.groupby('Crime')['Pena em Dias'].std()
    plt.errorbar(mean_by_categoria.index, mean_by_categoria, yerr=std_by_categoria, fmt='o')
    plt.xlabel('Categoria')
    plt.ylabel('Média de Pena em Dias')
    plt.title('Aproximação das Médias de Pena em Dias por Categoria')
    plt.show()