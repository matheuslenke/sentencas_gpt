import json
import glob
import os

def json_to_csv(json_content, csv_path):
    # Read the JSON file
    json_content = json_content.replace("```json", "").replace("```", "").replace(";", "").replace("\\n", "")
    data = json.loads(json_content)
    # Write the CSV file
    with open(csv_path, 'a') as file:
        for item in data:
            file.write(f'{item["tipo_crime"]} ; {item["numero_processo"]} ; {item["sentença_base"]} ; {item["sentença_definitiva"]} ; {item["conclusao"]} ; {item["nome_suspeito"]} ; {item["nome_juiz"]}\n')

def load_all_jsons(path: str, crime_category: str):
    '''
        This code loads all JSON files in the folder and convert them to CSV format.
    '''
    path = os.path.join(os.getcwd(), path, crime_category)
    md_files = glob.glob(f'./results/gemini/{crime_category}/*.md')
    csv_file = f"{crime_category}.csv"
    csv_path = os.path.join(path, csv_file)

    with open(csv_path, 'w') as file:
        file.write('tipo_crime;numero_processo;sentença_base;sentença_definitiva;conclusao;nome_suspeito;nome_juiz\n')
    for file_path in md_files:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            json_to_csv(content, csv_path)

def json_to_csv_intermediate(json_content, csv_path):
    json_content = json_content.replace("```json", "").replace("```", "").replace(";", "").replace("\\n", "")
    data = json.loads(json_content)
    with open(csv_path, 'a') as file:
        for item in data:
            file.write(f'{item["tipo_crime"]} ; {item["numero_processo"]} ; {item["pena_base"]} ; {item["pena_definitiva"]} ; {item["agravantes"]} ; {item["atenuantes"]}\n')

def load_all_jsons_intermediate(crime_category: str):
    path = os.path.join(os.getcwd(), "results/intermediaria")
    md_files = glob.glob(f'{path}/*.md')
    csv_file = f"{crime_category}.csv"
    csv_path = os.path.join(path, csv_file)

    with open(csv_path, 'w') as file:
        file.write('tipo_crime;numero_processo;pena_base;pena_definitiva;agravantes;atenuantes\n')
    for file_path in md_files:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            json_to_csv_intermediate(content, csv_path)