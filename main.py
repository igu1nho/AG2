import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# Use a função read_csv do Pandas para ler o arquivo CSV em um DataFrame.
data = pd.read_csv('tic-tac-toe.csv', delimiter=',')

# Exemplo de substituição de valores em uma coluna específica do DataFrame.
mapeamento = {
    'o': -1,
    'b': 0,
    'x': 1,
    'negativo': -1,
    'positivo': 1
}

data.replace(mapeamento, inplace=True)

# Imprimir o DataFrame resultante
print(data)

# Treinamento dos dados Pela Perceptron
linha = ['1','2','3','4','5','6','7','8','9']
coluna = ['resultado']

x = data[linha]
y = data[coluna]

# Dividir o conjunto de dados em 80% treinamento e 20% teste
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

perceptron = Perceptron(tol=1e-3, random_state=0)
perceptron.fit(X_train,y_train.values.ravel())

#Calculo da predicção
y_predc = perceptron.predict(X_test)

precisao = accuracy_score(y_test,y_predc)

print('Precisão:', precisao)

# Função para validar a entrada do usuário
def is_valid_input(confere_df):
    return data[linha].apply(tuple, axis=1).isin([tuple(confere_df.values[0])]).any()

# Entrada de dados
while True:
    confere = {}
    for i in range(1, 10):
        posicao = int(input(f'Entre com o valor para a posição {i} (-1/0/1): '))
        confere[str(i)] = [posicao]

    if is_valid_input(pd.DataFrame(confere)):
        break
    else:
        print("Os valores digitados não representam uma possibilidade de um jogo da velha convencional."
              "\n" "Digite uma combinação válida.")

#Prevendo o valor entrado com algumas das possibilidades do DataFrame dado.
class_predict = perceptron.predict(pd.DataFrame(confere))

if class_predict == 1:
    print('Vitória de x')
else:
    print('Empate ou derrota de x')