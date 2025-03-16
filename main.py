# main.py
from utils.multiprocessor import multiprocess_file

def main():
    """
    Ponto de entrada do programa.
    """
    print("=== Leitor de Arquivos para Soma de Valores Específicos ===")
    
    # Solicita o caminho do arquivo
    file_path = input("Digite o caminho do arquivo: ").strip()
    
    # Solicita o tipo de arquivo
    file_type = input("Digite o tipo de arquivo (pdf, txt, csv): ").lower().strip()
    if file_type not in ["pdf", "txt", "csv"]:
        print("Tipo de arquivo não suportado. Use 'pdf', 'txt' ou 'csv'.")
        return
    
    # Solicita os códigos a serem buscados
    codes_input = input("Digite os códigos a serem buscados (separados por vírgula): ").strip()
    codes = [code.strip() for code in codes_input.split(",")]
    
    # Verifica se há códigos válidos
    if not codes:
        print("Nenhum código foi informado.")
        return
    
    # Processa o arquivo usando multiprocessamento
    try:
        results = multiprocess_file(file_path, file_type, codes)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")
        return
    
    # Exibe os resultados
    print("\n=== Resultados ===")
    for code, total in results.items():
        print(f"O valor total para o código {code} é: {total:.2f}")

if __name__ == "__main__":
    main()