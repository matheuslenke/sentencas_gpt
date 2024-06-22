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

def get_gemini_prompt():
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