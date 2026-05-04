# 1. Validador de Complexidade de Senha

# Garantir que uma senha tenha o comprimento mínimo e caracteres especiais.
# Regras:
# 1. Comprimento mínimo: 8 caracteres;
# 2. Um caracter maiúsculo;
# 3. Um caracter minúsculo;
# 4. Um caracter especial;
# 5. Um número;

# Lógica: Percorrer a string caractere por caractere para validar critérios.
# Resultado Esperado: "Senha forte" ou lista de requisitos ausentes.

while True:  #Loop para que o usuário possa tentar novamente caso a senha seja inválida
    senha = input("Sua senha deve conter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais. \nDigite a sua senha: ")
    
    tem_maiuscula = False
    tem_minuscula = False
    tem_especial = False
    tem_numero = False
    if len(senha) >= 8: #Verifica se a senha tem pelo menos 8 caracteres
        for c in senha:
            if c.isupper(): #Verifica se o caracter é uma letra maiúscula
                tem_maiuscula = True
            elif c.islower(): #Verifica se o caracter é uma letra minúscula
                tem_minuscula = True
            elif c.isdigit(): #Verifica se o caracter é um número
                tem_numero = True
            elif not c.isalnum(): #Verifica se o caracter é um caracter especial (não alfanumérico)
                tem_especial = True
        erros = []
        if not tem_maiuscula:
            erros.append("- Um caracter maiúsculo") 
        if not tem_minuscula:
          erros.append("- Um caracter minúsculo")
        if not tem_especial:
            erros.append("- Um caracter especial")
        if not tem_numero:
            erros.append("- Um número")
        #O append é usado para adicionar itens à lista de erros, caso algum critério não seja atendido.

        if erros:
            print("Senha fraca. Requisitos ausentes:")
            for erro in erros:
                print(erro) #Mostra a lista de requisitos ausentes, caso a senha seja fraca.
        else:
            print("Senha forte.")
            break #Encerra o loop caso a senha seja forte, permitindo que o usuário saia do programa.
    else:
        print("A senha deve conter pelo menos 8 caracteres.")

#Nesse caso, o programa repete o loop em duas ocasiões: quando a senha é fraca por não atender um dos requisitos, ou quando ela não tem pelo menos 8 caracteres.
#O while serve exatamente para garantir que esse loop ocorra enquanto uma senha válida não for digitada.
#O if, o else e o elif adicionam condições para verificar se a senha atende aos requisitos ou não.
