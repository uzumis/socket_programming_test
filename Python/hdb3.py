#Implementação do HDB3
import numpy as np
import matplotlib.pyplot as plt

string = input("Insira a cadeia de bits: ")
string =str(string)

strOutput = []
strOutputLabel = []
def output():
    contador = 0
    p_anterior = 0
    violacao = 0
    p_violacao = 0

    for bit in string:
        if bit == str(1):
            if p_anterior == 1:
                strOutput.append(-1)
                strOutputLabel.append(-1)
                p_anterior = -1
                p_violacao = -1
                violacao = violacao + 1
            elif p_anterior == -1:
                strOutput.append(1)
                strOutputLabel.append(1)
                p_anterior = 1
            elif p_anterior == 0:
                strOutput.append(bit)
                strOutputLabel.append(bit)
                p_anterior = int(bit)
        elif bit == str(0):
            contador = contador + 1
            if contador == 4:
                strOutput.pop()
                strOutput.pop()
                strOutput.pop()
                strOutputLabel.pop()
                strOutputLabel.pop()
                strOutputLabel.pop()
                if violacao % 2 == 0:
                    #B00V
                    p_violacao = p_anterior * -1
                    strOutput.extend([p_violacao,0,0,p_violacao])
                    strOutputLabel.extend(["B",0,0,"V"])
                    violacao = violacao + 1
                    p_anterior = p_violacao

                else:
                    #000V
                    strOutputLabel.extend([0,0,0,"V"])
                    strOutput.extend([0,0,0,p_violacao])
                    violacao = violacao + 1
                contador = 0
            else :
                strOutput.append(bit)
                strOutputLabel.append(bit)


output()

#Resultado Grafico
x = np.arange(1, len(strOutput)+1,1)
plt.step(x, strOutput)
plt.xlabel(strOutputLabel)
plt.xlim(0, len(strOutput))
plt.ylim(-1,1)
plt.title('Codificação HDB3')
plt.show()