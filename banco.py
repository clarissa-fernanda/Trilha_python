menu=input(""" 
Selecione a operação:
[1] Depósito 
[2] Saque 
[3] Extrato
[4] Sair
Opção: """)

def deposito(saldo, extrato):
    valor = float(input("Digite o valor para depósito: R$ "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: +R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação invalida. O depósito deve ser um valor positivo.")
    return saldo, extrato

def saque(saldo, extrato, limite_do_saque):
    valor = float(input("Digite o valor para saque: R$ "))
    if 0 < valor <= saldo and valor <= limite_do_saque:
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    elif valor > limite_do_saque:
        print(f"Valor ultrapassa o limite do saque de R$ {limite_do_saque:.2f}.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        print("Valor inválido. O saque deve ser um valor positivo.")
    return saldo, extrato

def extrato_bancario(extrato, saldo):
    print("\n------ Extrato ------")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("---------------------\n")

def main():
    saldo = 0
    limite_do_saque = 500
    extrato = []

    while True:
        opcao = menu()
        if opcao == '1':
            saldo, extrato = deposito(saldo, extrato)
        elif opcao == '2':
            saldo, extrato = saque(saldo, extrato, limite_do_saque)
        elif opcao == '3':
            extrato_bancario(extrato, saldo)
        elif opcao == '4':
            print("Saindo do sistema. Obrigado por usar nosso banco!")
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

if __name__ == "__main__":
    main()



