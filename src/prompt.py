def get_history():
    history = [
    {"role": "system", "content": """
        Você me ajudará a extrair dados de um arquivo PDF. Este arquivo está em português. A entrada será o conteúdo do arquivo PDF dentro do delimitador ### pdf_data ###. 
        Obedeça as seguintes instruções:
        1. Leia o PDF sem escrever nada.
        2. Responda somente em Português
        3. Não faça perguntas e produza SOMENTE os dados necessários.
        4. Produza um JSON como resultado. O JSON terá o seguinte formato:
        {
            "tipo_crime": "tipo do crime,
            "sentença_base": "base da sentença",
            "sentença_definitiva": "sentença final",
            "nome_suspeito": "nome",
            "nome_juiz": "nome"
        }
    """},
    ]
    return history

def get_instructions_prompt():
    return """
        Você me ajudará a extrair dados de sentenças de juízes brasileiros. Este arquivo está em português. A entrada será o conteúdo de vários arquivos dentro do delimitador ### pdf_data ###. Cada arquivo contém uma sentença de um juiz, e o delimitador $$$ está diferenciando cada um dos documentos.
        Obedeça as seguintes instruções:
        1. Leia o PDF sem escrever nada.
        2. Responda somente em Português
        3. Não faça perguntas e produza SOMENTE os dados necessários.
        4. Produza um array de JSONs como resultado. O array JSON terá o seguinte formato:
        [{
            "tipo_crime": "tipo do crime,
            "numero_processo": "O numero do processo",
            "sentença_base": "A sentença base, em anos, meses ou dias",
            "sentença_definitiva": "sentença final, em anos, meses ou dias",
            "conclusao": "Se o réu foi absolvido ou condenado",
            "nome_suspeito": "nome",
            "nome_juiz": "nome"
        }, ...]
    """

def get_instructions_prompt_intermediate_sentence() -> str:
    return """Você é um assistente útil projetado para gerar resultados em JSON. Você é um assistente legal especializado em sentenças judiciais brasileiras. Analise as sentenças dentro da seção delimitada (###), separadas por ($$$) e forneça um array JSON com a seguinte estrutura:

[{
  "numero_processo": "O número do processo",
  "tipo_crime": "Tipo de crime",
  "pena_base": "A pena base, decretada no início",
  "pena_definitiva": "A pena final",
  "agravantes": "Agravantes da pena que aumentam a mesma",
  "atenuantes": "Atenuantes da pena que reduzem a mesma"
}, ...]
"""

def get_calculate_date_prompt():
    return """
        Você me ajudará a calcular o tempo de prisão de um réu. A entrada será um array em JSON com os seguintes campos:
        [{
            "sentença_base": "A sentença base, em anos, meses ou dias",
            "sentença_definitiva": "sentença final, em anos, meses ou dias"
        }, ...]

        Como resultado, você retornará um array JSON com o seguinte formato:
        [{ "tempo_prisao": "tempo de prisão em dias (somente em dias!)" }, ...]

        O JSON de Input estará dentro do delimitador ### <JSON aqui> ###.
    """