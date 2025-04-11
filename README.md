# 🚧 Previsão de Ocorrência de Feridos em Acidentes de Trânsito na Paraíba 

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

> <img src="![Gabriel](https://github.com/user-attachments/assets/43f395b7-8162-4acb-8ce2-d362cf114a4f)
" width="40" height="40" style="border-radius:50%"> Gabriel Batista Pontes &nbsp;&nbsp;&nbsp;  
> <img src="![Nercino](https://github.com/user-attachments/assets/3fe7baa4-5d62-4698-90b2-95ef43b0601c)
" width="40" height="40" style="border-radius:50%"> Nercino José de Barros Neto

> Contribuições e sugestões são muito bem-vindas!
