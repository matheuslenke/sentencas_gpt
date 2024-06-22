# Justice Data Extractor CLI

> Author: Matheus Lenke Coutinho

## Overview

Justice Data Extractor is a command-line interface (CLI) program designed to leverage Large Language Models (LLMs) for extracting and analyzing data from judicial sentences. This tool aims to simplify the process of gathering insights from legal documents, making it easier for legal professionals, researchers, and enthusiasts to access and understand justice-related data.

This project was created to experiment in a Discipline for my Masters degree at Federal University of Espírito Santo (UFES)

## Features

- **Data Extraction**: Automatically extract key information such as case numbers, parties involved, judgment dates, and legal outcomes from a wide range of judicial sentences.
- **Analysis Tools**: Utilize LLMs to perform qualitative analysis on extracted data, identifying trends, patterns, and anomalies in judicial decisions.
- **Custom Queries**: Support for custom queries, allowing users to specify the type of data they are interested in extracting.
- **Batch Processing**: Process multiple documents at once, saving time and effort in data collection and analysis.
- **Export Options**: Extracted data can be exported in various formats such as CSV, JSON, and XML for further analysis or integration with other tools.

## Getting Started

### Prerequisites

- Python 3.8 or later
- pip (Python package installer)

### Installation

1. Clone the repository to your local machine:
2. Navigate to the cloned directory
3. Install libraries

```bash
pip install -r requirements.txt
```

4. Run the code

- To download the PDF Data

```bash
python main.py download-data
```

- To run the LLM in order to extract the data from a crime type

```bash
python main.py run-llms -t <<crime_type>>
```

- To extract the JSON generated data to a unique CSV file

```bash
python main.py json-to-csv -t roubo_simples
```

#### Available Crime Types

> - furto_simples
> - furto_qualificado
> - roubo_simples
> - roubo_majorado

