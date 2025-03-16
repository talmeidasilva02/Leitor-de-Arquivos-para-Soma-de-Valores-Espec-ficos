# utils/value_extractor.py
import re

def find_and_sum_values(data_stream, codes: list) -> dict:
    """
    Busca linhas que contenham os códigos e soma os valores encontrados.
    Retorna um dicionário com o total para cada código.
    """
    results = {code: 0.0 for code in codes}

    for line in data_stream:
        for code in codes:
            if code in line:
                # Usa expressão regular para encontrar valores numéricos
                values = re.findall(r"\d+\.\d+", line)  # Encontra números com ponto decimal
                for value in values:
                    results[code] += float(value)

    return results