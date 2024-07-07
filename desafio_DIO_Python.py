menu = """
##########################################################

Selecione uma opção para realização do serviço desejado

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

#########################################################

=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Prencha o valor a ser depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! Favor verificar o valor digitado.")

    elif opcao == "2":
        valor = float(input("Entre com a valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente para essa operação.")

        elif excedeu_limite:
            print("Operação falhou! O valor excede o limite para saques diários.")

        elif excedeu_saques:
            print("Operação falhou! Você excedeu o limite de saques de hoje.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! Há algo errado no valor digitado. Verifique.")

    elif opcao == "3":
        print("******************************************")
        print("================ EXTRATO =================\n")
        print(" ")
        print("Não há registro de transações até o momento." if not extrato else extrato)
        print(f"\nSaldo:    R$ {saldo:.2f}")
        print(" ")
        print("==========================================")
        print("******************************************")

    elif opcao == "0":
        print("\nObrigado por utilizar nossos serviços!!\n")
        break

    else:
        print("Operação inválida, verifique as opções e informe uma operção válida.")
