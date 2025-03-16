# utils/multiprocessor.py
import csv
from multiprocessing import Pool
from utils.file_reader import read_pdf
from utils.value_extractor import find_and_sum_values

def split_file(file_path: str, file_type: str, num_chunks: int = 4):
    """
    Divide um arquivo em pedaços para processamento paralelo.

    Args:
        file_path (str): Caminho do arquivo.
        file_type (str): Tipo do arquivo (txt, csv, pdf).
        num_chunks (int): Número de pedaços para dividir o arquivo.

    Yields:
        list: Pedaço do arquivo (linhas ou páginas).
    """
    if file_type == "txt":
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            chunk_size = len(lines) // num_chunks
            for i in range(0, len(lines), chunk_size):
                yield lines[i:i + chunk_size]

    elif file_type == "csv":
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            lines = list(reader)
            chunk_size = len(lines) // num_chunks
            for i in range(0, len(lines), chunk_size):
                yield lines[i:i + chunk_size]

    elif file_type == "pdf":
        # PDFs são processados página por página, então não dividimos
        yield read_pdf(file_path)

def process_chunk(chunk: list, codes: list) -> dict:
    """
    Processa um pedaço do arquivo e retorna os resultados parciais.

    Args:
        chunk (list): Pedaço do arquivo (linhas ou páginas).
        codes (list): Lista de códigos a serem buscados.

    Returns:
        dict: Resultados parciais (código: valor total).
    """
    if isinstance(chunk, list):
        text = "\n".join(chunk)
    else:
        text = chunk
    return find_and_sum_values(text.split("\n"), codes)

def multiprocess_file(file_path: str, file_type: str, codes: list, num_processes: int = 4) -> dict:
    """
    Processa um arquivo grande usando multiprocessamento.

    Args:
        file_path (str): Caminho do arquivo.
        file_type (str): Tipo do arquivo (txt, csv, pdf).
        codes (list): Lista de códigos a serem buscados.
        num_processes (int): Número de processos a serem usados.

    Returns:
        dict: Resultados finais (código: valor total).
    """
    # Divide o arquivo em pedaços
    chunks = list(split_file(file_path, file_type, num_processes))

    # Cria um pool de processos
    with Pool(processes=num_processes) as pool:
        # Processa cada pedaço em paralelo
        results = pool.starmap(process_chunk, [(chunk, codes) for chunk in chunks])

    # Combina os resultados
    final_results = {code: 0.0 for code in codes}
    for result in results:
        for code, value in result.items():
            final_results[code] += value

    return final_results