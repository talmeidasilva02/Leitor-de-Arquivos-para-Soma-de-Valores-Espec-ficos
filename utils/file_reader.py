# utils/file_reader.py
import PyPDF2
import csv

def read_pdf(file_path: str):
    """
    Lê um arquivo PDF página por página (eficiente para grandes arquivos).
    """
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            yield page.extract_text()  # Retorna o texto de cada página

def read_txt(file_path: str):
    """
    Lê um arquivo TXT linha por linha (eficiente para grandes arquivos).
    """
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()  # Retorna cada linha

def read_csv(file_path: str):
    """
    Lê um arquivo CSV linha por linha (eficiente para grandes arquivos).
    """
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            yield ",".join(row)  # Retorna cada linha como uma string