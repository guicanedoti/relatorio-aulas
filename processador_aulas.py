import pandas as pd
import csv

def processar_dados(caminho_arquivo):
    """
    Processa dados de aulas para contar a quantidade de aulas por professor e disciplina.
    """
    try:
        df = pd.read_csv(caminho_arquivo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None

    # Agrupa por professor e disciplina, e conta a quantidade de aulas
    contagem_aulas = df.groupby(['professor', 'disciplina']).size().reset_index(name='quantidade_aulas')
    
    return contagem_aulas

def salvar_csv(dados, nome_arquivo_saida):
    """
    Salva os dados processados em um arquivo CSV.
    """
    if dados is not None:
        dados.to_csv(nome_arquivo_saida, index=False)
        print(f"Dados salvos com sucesso em '{nome_arquivo_saida}'.")
    else:
        print("Nenhum dado para salvar.")

if __name__ == "__main__":
    # Nome do arquivo de entrada e saída
    arquivo_entrada = 'dados.csv'
    arquivo_saida = 'relatorio_aulas.csv'
    
    # Processa e salva o relatório
    relatorio = processar_dados(arquivo_entrada)
    salvar_csv(relatorio, arquivo_saida)