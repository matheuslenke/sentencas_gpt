import csv
from src.generate_gemini import generate
from src.prompt import get_calculate_date_prompt
from src.run_llms import save_to_file
import pandas as pd
from string import Template
import json

class Crime:
    '''
        This class is used to store the data extracted from the CSV file.
    '''
    tipo_crime: str
    numero_processo: str
    sentenca_base: str
    sentenca_definitiva: str
    conclusao: str
    nome_juiz: str

    def __init__(self, tipo_crime, numero_processo, sentenca_base, sentenca_definitiva, conclusao, nome_suspeito, nome_juiz):
        self.tipo_crime = tipo_crime
        self.numero_processo = numero_processo
        self.sentenca_base = sentenca_base
        self.sentenca_definitiva = sentenca_definitiva
        self.conclusao = conclusao
        self.nome_suspeito = nome_suspeito
        self.nome_juiz = nome_juiz

def date_to_csv(crime_type):
    json_path = f"results/date/{crime_type}.json"
    csv_path = f"results/date/{crime_type}.csv"

    with open(json_path, "r") as json_file:
        data = json.load(json_file)

    with open(csv_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["tempo_prisao"])  # Header

        for item in data:
            tempo_prisao = item.get("tempo_prisao")
            writer.writerow([tempo_prisao])


def calculate_dates(crime_type):
    '''
        This function reads the data from a CSV file and creates a Crime object for each row.
    '''

    all_crimes: list[Crime] = []
    json_path = f'results/gemini/{crime_type}/{crime_type}.json'

    with open(json_path, 'r') as file:
        data = pd.read_csv(file, sep=";", header=0, decimal=",")

        for row in data.values:
            tipo_crime = row[0]
            numero_processo = row[1]
            sentenca_base = row[2]
            sentenca_definitiva = row[3]
            conclusao = row[4]
            nome_suspeito = row[5]
            nome_juiz = row[6]
            
            crime = Crime(tipo_crime, numero_processo, sentenca_base, sentenca_definitiva, conclusao, nome_suspeito, nome_juiz)
            all_crimes.append(crime)

    final_json = "[ "
    for crime in all_crimes:
        template = Template("""
        {
            "sentença_base": "$base",
            "sentenca_definitiva": "$def"
        },
        """)
        final = template.substitute({
            'base': crime.sentenca_base,
            'def': crime.sentenca_definitiva
        })
        final_json += final
    final_json = final_json.rstrip(",")  # Remove the trailing comma
    final_json += " ]"
    responses = generate(message=final_json, prompt=get_calculate_date_prompt())

    for response in responses:
        save_to_file(f"results/date/{crime_type}.csv", response.text)
        print(response.text, end="")