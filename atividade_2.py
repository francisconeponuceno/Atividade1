# IMPORTAÇÃO DAS BLIBIOTECAS
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


# CRIAÇÃO DOS DADOS FICTÍCIOS
dados = {
    "idade": [22, 35, 45, 28, 52, 33, 41, 29, 48, 39],
    "tempo_cadastro": [12, 48, 5, 30, 60, 10, 22, 15, 55, 40],
    "email_aberto": [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    "clicou_no_link": [0, 0, 1, 1, 0, 1, 1, 0, 0, 1],
    "comprou": [0, 0, 1, 1, 0, 1, 1, 0, 0, 1]
}

# TRANSFORMANDO EM DATA FRAME
df = pd.DataFrame(dados)


# SEPARAÇÃO DAS VARIÁVEIS DEPENDETES E INDEPENDENTES
x = df[['idade', 'tempo_cadastro', 'email_aberto', 'clicou_no_link']]

y = df['comprou']


# DIVISÃO EM TREINO E TESTE
x_treino, x_teste, y_treino, y_teste = train_test_split(
    x, y, test_size=0.3, random_state=42
)


# CRIANDO O MODELO
modelo = DecisionTreeClassifier()

# TREINANDO O MODELO
modelo.fit(x_treino, y_treino)


# PREVISÕES NOS TESTES
previsoes = modelo.predict(x_teste)



print('Acurácia:', accuracy_score(y_teste, previsoes))
print('\nRelatório de Classificação:\n')
print(classification_report(y_teste, previsoes))