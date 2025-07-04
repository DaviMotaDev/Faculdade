import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,5,7,11]

plt.plot(x,y,marker='o')

plt.title("exemplo de grafico com matplotlib")
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.show()