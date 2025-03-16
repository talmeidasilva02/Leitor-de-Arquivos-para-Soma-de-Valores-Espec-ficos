# main.py
from utils.file_reader import read_pdf, read_txt, read_csv
from utils.value_extractor import find_and_sum_values

def main():
    file_path = input("Digite o caminho do arquivo: ")
    file_type = input("Digite o tipo de arquivo (pdf, txt, csv): ").lower()
    codes = input("Digite os códigos a serem buscados (separados por vírgula): ").split(",")

    # Lê o arquivo conforme o tipo
    if file_type == "pdf":
        data_stream = read_pdf(file_path)
    elif file_type == "txt":
        data_stream = read_txt(file_path)
    elif file_type == "csv":
        data_stream = read_csv(file_path)
    else:
        print("Tipo de arquivo não suportado.")
        return

    # Busca e soma os valores
    results = find_and_sum_values(data_stream, codes)

    # Exibe os resultados
    for code, total in results.items():
        print(f"O valor total para o código {code} é: {total:.2f}")

if __name__ == "__main__":
    main()