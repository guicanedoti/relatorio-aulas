# 📈 Relatório de Aulas e Professores

Este é um programa em Python projetado para automatizar a verificação de trabalhos e gerar relatórios detalhados sobre a quantidade de aulas dadas por professores em disciplinas específicas. O resultado é salvo em um arquivo CSV, facilitando a análise e o compartilhamento.

---

### 📋 O que este programa faz?

O objetivo principal deste projeto é transformar dados brutos em informações úteis. Ele executa as seguintes tarefas:

1.  **Leitura de Dados:** O programa lê um arquivo chamado `dados.csv`, que deve conter as informações sobre as aulas, professores, disciplinas e semestres.
2.  **Processamento:** Ele agrupa os dados e calcula a quantidade total de aulas por professor e por disciplina, gerando um resumo claro e conciso.
3.  **Geração de Relatório:** O resultado do processamento é salvo em um novo arquivo CSV chamado `relatorio_aulas.csv`, pronto para ser visualizado em qualquer editor de planilhas (como Excel ou Google Sheets).

---

### 🚀 Como usar?

Existem duas formas de utilizar este programa, dependendo da sua preferência.

#### Opção 1: Usando o Aplicativo (recomendado para o cliente)

Esta é a forma mais fácil e direta. Você não precisa ter o Python instalado.

1.  **Faça o download do arquivo executável:** Envie o arquivo `processador_aulas.exe` para o cliente.
2.  **Crie a pasta do projeto:** Crie uma pasta no seu computador e coloque os dois arquivos dentro dela:
    * `dados.csv` (seu arquivo com os dados brutos)
    * `processador_aulas.exe` (o programa que você baixou)
3.  **Execute o programa:** Basta dar um **duplo clique** no arquivo `processador_aulas.exe`.
4.  **Verifique o resultado:** O programa irá rodar rapidamente. Um novo arquivo chamado `relatorio_aulas.csv` será gerado automaticamente na mesma pasta.

#### Opção 2: Usando o Código Python (para desenvolvedores)

Se você é um desenvolvedor e quer ver o código ou modificar o script, siga estes passos:

1.  **Clonar o repositório:**
    ```bash
    git clone [https://docs.github.com/pt/repositories/creating-and-managing-repositories/quickstart-for-repositories](https://docs.github.com/pt/repositories/creating-and-managing-repositories/quickstart-for-repositories)
    ```
2.  **Navegue até a pasta do projeto:**
    ```bash
    cd [processador_aulas]
    ```
3.  **Instale as dependências:**
    ```bash
    pip install pandas
    ```
4.  **Execute o script:**
    ```bash
    python processador_aulas.py
    ```

---

### 🧩 Estrutura do Arquivo `dados.csv`

Para que o programa funcione corretamente, o arquivo de entrada `dados.csv` deve seguir a seguinte estrutura de colunas:

| Coluna | Descrição | Exemplo |
| :--- | :--- | :--- |
| **professor** | Nome do professor. | `João da Silva` |
| **disciplina** | Nome da disciplina. | `Matemática` |
| **semestre** | O semestre da aula. | `2023.1` |
| **data_aula** | A data em que a aula ocorreu. | `01/03/2023` |

---

### 🛠️ Tecnologias Utilizadas

* **Python 3:** Linguagem principal.
* **Pandas:** Biblioteca para manipulação e análise de dados.
* **PyInstaller:** Ferramenta para transformar o script em um executável.

---

### 📝 Contato e Suporte

Se tiver qualquer problema ou precisar de novas funcionalidades, entre em contato comigo.

**[Guilherme Canedo Santos]**
[guilhermecanedo09@gmail.com]
[(https://github.com/guicanedoti)]