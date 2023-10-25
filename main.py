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

# Entrada de dados
pos1 = int(input('Entre com o valor de 1:1 (-1/0/1): '))
pos2 = int(input('Entre com o valor de 1:2 (-1/0/1): '))
pos3 = int(input('Entre com o valor de 1:3 (-1/0/1): '))
pos4 = int(input('Entre com o valor de 2:1 (-1/0/1): '))
pos5 = int(input('Entre com o valor de 2:2 (-1/0/1): '))
pos6 = int(input('Entre com o valor de 2:3 (-1/0/1): '))
pos7 = int(input('Entre com o valor de 3:1 (-1/0/1): '))
pos8 = int(input('Entre com o valor de 3:2 (-1/0/1): '))
pos9 = int(input('Entre com o valor de 3:3 (-1/0/1): '))

confere = {'1':[pos1],'2':[pos2],'3':[pos3],'4':[pos4],'5':[pos5],'6':[pos6],'7':[pos7],'8':[pos8],'9':[pos9]}
confere = pd.read_csv(confere, delimiter=',')

print(confere)

'''
class_predict = perceptron.predict(confere)

if class_predict == 1:
    print('Vitória de x')
else:
    print('Derrota de x')
'''