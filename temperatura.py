# 2. Monitor de Temperatura de Servidor
# Monitorar um valor constante e agir caso ultrapasse o limite.

# Lógica: Implementar um loop que "escuta" um sensor (valor manual) até que o sistema seja desligado.

# Regra: Temperatura limite do servidor: 80 ºC

# Resultado Esperado: Alerta de "Resfriamento ativado".

while True: #Permite que o loop continue até que o usuário decida sair, digitando -1234.
    temperatura = float(input("Digite a temperatura do servidor (ou -1234 para sair): "))
    
    if temperatura == -1234:
        print("Desligando o monitor de temperatura. Até mais!")
        break
    
    if temperatura > 80:
        print("Alerta: Resfriamento ativado!")
    else:
        print("Temperatura dentro do limite seguro.")

#Nesse código, o while serve para permitir que o usuário continue digitando a temperatura até que saia digitando -1234.
#O if e o else verificam se a temperatura está dentro do aceitável ou se é necessário resfriamento, printando a mensagem de resfriamento quando necessário.