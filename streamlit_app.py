# Desenvolvimento de Aplicativo de Gerenciamento de Dados Laboratoriais

# Título: Desenvolvimento de Aplicativo de Gerenciamento de Dados Laboratoriais
# Descrição: Crie um aplicativo inteligente que facilite a coleta, armazenamento, visualização e análise de dados laboratoriais. O aplicativo é composto por um formulário intuitivo para entrada de dados e um gráfico dinâmico para visualização dos resultados. Ele é especialmente projetado para monitorar o crescimento de bactérias ao longo do tempo, mas também pode ser personalizado para atender às necessidades específicas de diferentes laboratórios.

# Funcionalidades Principais:
# 1. Formulário de Entrada de Dados:
#    - O aplicativo apresenta um formulário de fácil utilização para a coleta de dados.
#    - Os campos obrigatórios incluem: Data, Hora, Local, Tipo de Amostra e Antibiótico.
#    - Também oferece a possibilidade de adicionar campos personalizados, garantindo flexibilidade.

class Formulario:
    def __init__(self):
        self.campos_obrigatorios = ['Data', 'Hora', 'Local', 'Tipo de Amostra', 'Antibiótico']
        self.campos_personalizados = []

    def adicionar_campo_personalizado(self, campo):
        self.campos_personalizados.append(campo)

# 2. Visualização de Dados:
#    - Os dados coletados são armazenados em formato JSON e usados para gerar um gráfico de linha.
#    - O gráfico exibe o crescimento de bactérias em relação ao tempo, permitindo a análise de tendências.

import json
import matplotlib.pyplot as plt

dados_coletados = {
    'data': ['2021-01-01', '2021-01-02', '2021-01-03'],
    'crescimento_bacterias': [10, 15, 20]
}

plt.plot(dados_coletados['data'], dados_coletados['crescimento_bacterias'])
plt.xlabel('Data')
plt.ylabel('Crescimento de Bactérias')
plt.title('Gráfico de Crescimento de Bactérias')
plt.show()

# 3. Opções de Filtro:
#    - Os usuários podem filtrar os dados com base em critérios como data, hora, local, tipo de amostra ou antibiótico.

def filtrar_dados(dados, criterio):
    dados_filtrados = []
    for dado in dados:
        if criterio in dado:
            dados_filtrados.append(dado)
    return dados_filtrados

# Exemplo de uso:
dados = [
    {'data': '2021-01-01', 'hora': '09:00', 'local': 'Laboratório A', 'tipo_amostra': 'Sangue', 'antibiotico': 'Penicilina'},
    {'data': '2021-01-02', 'hora': '10:00', 'local': 'Laboratório B', 'tipo_amostra': 'Urina', 'antibiotico': 'Amoxicilina'},
    {'data': '2021-01-03', 'hora': '11:00', 'local': 'Laboratório A', 'tipo_amostra': 'Sangue', 'antibiotico': 'Penicilina'}
]

criterio = 'Penicilina'
dados_filtrados = filtrar_dados(dados, criterio)
print(dados_filtrados)

# 4. Exportação de Dados:
#    - Os dados podem ser exportados para formatos CSV ou PDF, facilitando a documentação e compartilhamento.

import csv

def exportar_para_csv(dados, nome_arquivo):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        writer = csv.DictWriter(arquivo_csv, fieldnames=dados[0].keys())
        writer.writeheader()
        writer.writerows(dados)

# Exemplo de uso:
dados = [
    {'data': '2021-01-01', 'hora': '09:00', 'local': 'Laboratório A', 'tipo_amostra': 'Sangue', 'antibiotico': 'Penicilina'},
    {'data': '2021-01-02', 'hora': '10:00', 'local': 'Laboratório B', 'tipo_amostra': 'Urina', 'antibiotico': 'Amoxicilina'},
    {'data': '2021-01-03', 'hora': '11:00', 'local': 'Laboratório A', 'tipo_amostra': 'Sangue', 'antibiotico': 'Penicilina'}
]

nome_arquivo = 'dados_laboratoriais.csv'
exportar_para_csv(dados, nome_arquivo)

# 5. Correlação de Informações:
#    - Ferramentas estão disponíveis para identificar correlações entre informações de diferentes testes, auxiliando na análise.

import numpy as np

dados_teste1 = [1, 2, 3, 4, 5]
dados_teste2 = [2, 4, 6, 8, 10]

correlacao = np.corrcoef(dados_teste1, dados_teste2)
print(correlacao)

# 6. Integração com Sistemas de Laboratório:
#    - O aplicativo suporta integração com sistemas LIMS via API REST ou conector ODBC.
#    - Isso permite a sincronização dos dados entre o aplicativo e o sistema LIMS, simplificando a gestão e análise dos dados.

import requests

def sincronizar_dados_lims(dados):
    response = requests.post('https://api.lims.com/sync', json=dados)
    if response.status_code == 200:
        return True
    else:
        return False

# Exemplo de uso:
dados = [
    {'data': '2021-01-01', 'hora': '09:00', 'local': 'Laboratório A', 'tipo_amostra': 'Sangue', 'antibiotico': 'Penicilina'},
    {'data': '2021-01-02', 'hora': '10:00', 'local': 'Laboratório B', 'tipo_amostra': 'Urina', 'antibiotico': 'Amoxicilina'},
    {'data': '2021-01-03', 'hora': '11:00', 'local': 'Laboratório A', 'tipo_amostra': 'Sangue', 'antibiotico': 'Penicilina'}
]

sincronizado = sincronizar_dados_lims(dados)
print(sincronizado)

# 7. Ampliação para Outros Tipos de Dados:
#    - O aplicativo pode ser expandido para incluir mais campos de dados, como resultados de testes de sensibilidade a antibióticos, perfil de resistência bacteriana e dados clínicos.

class DadosLaboratoriais:
    def __init__(self):
        self.resultados_testes_sensibilidade = []
        self.perfil_resistencia_bacteriana = []
        self.dados_clinicos = []

    def adicionar_resultado_teste_sensibilidade(self, resultado):
        self.resultados_testes_sensibilidade.append(resultado)

    def adicionar_perfil_resistencia_bacteriana(self, perfil):
        self.perfil_resistencia_bacteriana.append(perfil)

    def adicionar_dado_clinico(self, dado):
        self.dados_clinicos.append(dado)

# 8. Personalização:
#    - Um painel de configurações permite personalizar o aplicativo para atender às necessidades específicas de cada laboratório.
#    - Usuários podem adicionar campos personalizados, ajustar o layout do formulário e dos gráficos, e definir opções de exportação.

class PainelConfiguracoes:
    def __init__(self):
        self.campos_personalizados = []
        self.layout_formulario = 'padrao'
        self.layout_grafico = 'padrao'
        self.opcoes_exportacao = ['CSV', 'PDF']

    def adicionar_campo_personalizado(self, campo):
        self.campos_personalizados.append(campo)

    def definir_layout_formulario(self, layout):
        self.layout_formulario = layout

    def definir_layout_grafico(self, layout):
        self.layout_grafico = layout

    def definir_opcoes_exportacao(self, opcoes):
        self.opcoes_exportacao = opcoes

# Benefícios:
# - Facilita o processo de coleta, armazenamento e análise de dados laboratoriais.
# - O gráfico dinâmico ajuda na identificação de padrões e tendências.
# - Integração com sistemas LIMS melhora a eficiência do gerenciamento de dados.
# - A possibilidade de ampliação para diferentes tipos de dados aumenta a versatilidade.
# - A personalização garante que o aplicativo atenda às necessidades únicas de cada laboratório.
