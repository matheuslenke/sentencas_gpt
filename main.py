import argparse
import asyncio

from src.extract_data import extract_data
from src.json_to_csv import load_all_jsons
from src.run_llms import change_category, run_llms

def main():
    '''
        This is a CLI application that allows the user to download data, run the LLM model, and convert the JSON files to CSV.
        The data is related to criminal sentences and the LLM model is used to extract some information from each sentence.
    '''
    parser = argparse.ArgumentParser(description='CLI App')
    parser.add_argument('command', choices=['download-data', 'run-llms', 'json-to-csv'], help='Choose a function to run')
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
            print(args.type)
            load_all_jsons(args.type)
        else:
            print("Please provide the -t argument for crime type.")

if __name__ == '__main__':
    main()