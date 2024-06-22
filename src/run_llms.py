import os
import PyPDF2
import time
from src.generate_gemini import generate

crime_category = "roubo_simples"

def change_category(category: str) -> None:
    '''
    Change the category of the crime to be analyzed.
    '''
    global crime_category
    crime_category = category

def save_to_file(file_path: str, content: str):
    '''
    Save any content to a file with Append mode
    '''
    with open(file_path, "a") as result_file:
         result_file.write(content)

def get_pdf_data(pdf_folder, pdf_file):
    pdf_data = ""
    path = os.path.join(pdf_folder, pdf_file)
    with open(path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        # Extract the PDF data as a string
        for page in pdf_reader.pages:
            pdf_data += page.extract_text()
        pdf_data += "\n$$$\n"
    return pdf_data

def get_files(folder):
    # Get the list of PDF files in the folder
    pdf_files = [file for file in os.listdir(folder) if file.endswith(".pdf")]
    print(f"Quantidade de arquivos: {len(pdf_files)}")
    return pdf_files

def get_pdf_chunks(folder):
    pdf_files = get_files(folder)
    return [pdf_files[i:i+10] for i in range(0, len(pdf_files), 10)]

def run_llm_in_chunk(chunk, pdfs_folder, index):
    '''
        Run the LLM model in a chunk of PDF files. This function read the files
        based on crime_category and generate the response using the Gemini model.
    '''
    # Get the data from each PDF file and concatenate them in one file
    pdf_data = ""
    for pdf_file in chunk:
        pdf_data += get_pdf_data(pdfs_folder, pdf_file)

    # Saving to one file with an entire chunk of data.
    save_to_file(f"results/sentencas/{crime_category}/{crime_category}_{index}.md", pdf_data)

    # Sending request to Gemini with current chunk of data
    responses = generate(pdf_data)

    # Saving the responses to a file
    for response in responses:
        save_to_file(f"results/result-gemini-{crime_category}_{index}.md", response.text)
        print(response.text, end="")

async def run_llms():
    '''
        Main function that get the data from each downloaded PDF and
        generate the response using the Gemini or the OpenAI model.
    '''
    # Define the path to the PDF folder
    pdfs_folder = f"data/{crime_category}"
    pdf_files_chunks = get_pdf_chunks(pdfs_folder)

    # Process each chunk of pdf_files
    index = 0
    for chunk in pdf_files_chunks:
        run_llm_in_chunk(chunk=chunk, pdfs_folder=pdfs_folder, index=index)
        index += 1
        time.sleep(0.5)
