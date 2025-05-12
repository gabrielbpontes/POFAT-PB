# 🚧 Previsor de Ocorrência de Feridos em Acidentes de Trânsito na Paraíba - POFAT PB

Este projeto tem como objetivo aplicar técnicas de aprendizado de máquina para prever a ocorrência de feridos em acidentes de trânsito no estado da Paraíba, utilizando dados históricos e variáveis como dia da semana, horário do acidente, condições meteorológicas e número de veículos e pessoas envolvidos.

## 🚀 Como Executar o Dashboard

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git

### 1. Clonar o Repositório

```bash
# Clone o repositório
git clone https://github.com/gabrielbpontes/POFAT-PB.git
cd POFAT-PB
```

### 2. Configuração do Ambiente

```bash
# Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt
```

### 3. Executando a Aplicação

Execute a aplicação Streamlit:
```bash
streamlit run APP/main.py
```

## 🧠 Modelos Avaliados

Foram testados diversos algoritmos de classificação supervisionada, incluindo:

- Regressão Logística (Logit)
- Naive Bayes
- K-Nearest Neighbors (KNN)
- Árvore de Decisão
- Floresta Aleatória (Random Forest)

A Regressão Logística apresentou o melhor desempenho, com acurácia média superior a **80%** após validação cruzada.

## 📊 Resultados

- **Melhor modelo**: Regressão Logística
- **Acurácia final**: ~82%
- **Matriz de confusão**: Equilíbrio satisfatório entre os verdadeiros positivos e negativos
- **Variáveis utilizadas**: Dia da semana, fase do dia, condições climáticas, BR, quantidade de veículos e pessoas, etc.

## 🔧 Tecnologias Utilizadas

- Python 3
- Pandas
- Scikit-learn
- Pickle
- Jupyter Notebook
- Streamlit
- Plotly
- NumPy

## 📃 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

> Desenvolvido por

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/gabrielbpontes">
        <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/127130171?s=48&v=4" width="100px;" alt=""/>
        <br />
        <sub><b>Gabriel Pontes</b></sub>
      </a>
      <br/>
      <a href="https://github.com/gabrielbpontes" target="_blank">
        <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" style="padding-top: 10px;">
      </a>
      <br/>
      <a href="https://www.linkedin.com/in/gabriel-pontes-2152a9276/" target="_blank">
        <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" style="padding-top: 10px;">
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/NercinoN21">
        <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/86074258?v=4" width="100px;" alt=""/>
        <br />
        <sub><b>Nercino Neto</b></sub>
      </a>
      <br />
      <a href="https://github.com/NercinoN21" target="_blank">
        <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" style="padding-top: 10px;">
      </a>
      <br/>
      <a href="https://www.linkedin.com/in/nercino-neto/" target="_blank">
        <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" style="padding-top: 10px;">
      </a>
    </td>
  </tr>
</table>

> Contribuições e sugestões são muito bem-vindas!
