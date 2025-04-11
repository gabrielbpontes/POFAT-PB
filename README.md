# 🚧 Previsão de Ocorrência de Feridos em Acidentes de Trânsito na Paraíba 🛣️

Este projeto tem como objetivo aplicar técnicas de aprendizado de máquina para prever a ocorrência de feridos em acidentes de trânsito no estado da Paraíba, utilizando dados históricos e variáveis como dia da semana, horário do acidente, condições meteorológicas e número de veículos e pessoas envolvidos.

## 📂 Estrutura do Projeto

- `acidentespb.csv`: Base de dados contendo registros de acidentes na Paraíba.
- `modelo_preditivo.ipynb`: Notebook principal com o passo a passo do pré-processamento, modelagem e avaliação.

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

## 📃 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

> Desenvolvido por

> <img src="![Imagem do WhatsApp de 2025-04-11 à(s) 00 22 56_65813567](https://github.com/user-attachments/assets/36e85c53-2c34-44d1-ab7d-d41512e023f6)
" width="40" height="40" style="border-radius:50%"> [Gabriel Batista Pontes] &nbsp;&nbsp;&nbsp;  
> <img src="![Imagem do WhatsApp de 2025-04-11 à(s) 00 21 26_53417f03](https://github.com/user-attachments/assets/0864f455-d6b7-44fc-a420-98d96d9974bd)
" width="40" height="40" style="border-radius:50%"> [Nercino José de Barros Neto]

>  contribuições e sugestões são muito bem-vindas!
