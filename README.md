# Leitor de Arquivos para Soma de Valores Específicos

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Um projeto em Python para ler arquivos grandes (PDF, TXT, CSV) de forma eficiente, buscar valores específicos com base em códigos e somar esses valores. O projeto utiliza técnicas avançadas, como **multiprocessamento**, **expressões regulares** e **leitura em fluxo (streaming)**, para garantir alto desempenho mesmo com arquivos de grande porte.

---

## Funcionalidades

- **Leitura de Arquivos**: Suporte para arquivos PDF, TXT e CSV.
- **Busca de Códigos**: Busca múltiplos códigos em um arquivo.
- **Soma de Valores**: Soma os valores associados a cada código.
- **Multiprocessamento**: Processamento paralelo para acelerar a leitura de arquivos grandes.
- **Eficiência**: Leitura em fluxo (streaming) para evitar carregar arquivos grandes na memória.


---

## Como Executar

### Pré-requisitos

- Python 3.8 ou superior instalado.
- Git (opcional, para clonar o repositório).

### Passos para Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/file-value-extractor.git
   cd file-value-extractor

2. (Opcional) Crie um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt

4. Execute o programa:
    ```bash
    python main.py

---

## Exemplo de Uso

### Conteúdo do Arquivo (exemplo):
TXT/CSV:
0001,100.50
0002,200.00
0001,50.75
0003,300.00
0001,75.25
0002,150.00

PDF:
0001 - Valor: 100.50
0002 - Valor: 200.00
0001 - Valor: 50.75
0003 - Valor: 300.00

Saída do Programa:
Digite o caminho do arquivo: exemplo.csv
Digite o tipo de arquivo (pdf, txt, csv): csv
Digite os códigos a serem buscados (separados por vírgula): 0001,0002
O valor total para o código 0001 é: 226.50
O valor total para o código 0002 é: 350.00

### Tecnologias e Técnicas Utilizadas
Python: Linguagem de programação principal.

PyPDF2: Biblioteca para leitura de arquivos PDF.

Multiprocessamento: Uso da biblioteca multiprocessing para processamento paralelo.

Expressões Regulares: Uso do módulo re para encontrar valores numéricos.

Leitura em Fluxo (Streaming): Processamento de arquivos linha por linha ou página por página para evitar carregar tudo na memória.

---

### Licença
Este projeto está licenciado sob a licença MIT.

### Contato
Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

Nome: Tiago Almeida

Email: tiago@codecity.app