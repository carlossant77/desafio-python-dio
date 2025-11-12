menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = {}
contas = []
numero_conta = 1

while True:
    
    def deposito(valor, /):
        global saldo
        global extrato
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Deposito de {valor} realizado com sucesso! Saldo atual: {saldo}")
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    def saque(*, valor):
        global saldo
        global numero_saques
        global extrato
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print(f"Operação falhou! Você não tem saldo suficiente. (Saldo Atual: R${saldo})")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite. (R$500)")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido. (Número máximo: 3)")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R${valor} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    def mostrar_extrato(saldo, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    def criar_usuario(nome, nascimento, cpf, endereco):
        
        def cpf_em_uso():
            for pessoa, informacoes in usuarios.items():
                for chave, valor in informacoes.items():
                    if cpf == valor:
                        return True
              
        if cpf_em_uso():
            print('Não foi possível se cadastrar: O CPF informado já está em uso.')
            return 
             
        dados = {"CPF": cpf, "Data de nascimento": nascimento, "Endereço": endereco}
        usuarios[nome] = dados
        print(usuarios)
    
    def criar_conta(cpf, *, agencia):
        global numero_conta
        
        def cpf_cadastrado():
            for pessoa, informacoes in usuarios.items():
                for chave, valor in informacoes.items():
                    if cpf == valor:
                        return True
        
        if not cpf_cadastrado():
            print("Não foi possível criar sua conta: O CPF informado ainda não foi cadastrado.")
            return
               
        nova_conta = [cpf, agencia, numero_conta]
        numero_conta += 1
        contas.append(nova_conta)
        print("Sua conta foi criada com sucesso!")
        print(contas)
        
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        deposito(valor)

    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))
        saque(valor=valor_saque)

    elif opcao == "e":
        mostrar_extrato(saldo, extrato=extrato)
        
    elif opcao == "u":
        nome = str(input("Insira o nome completo do usuário a ser cadastrado: "))
        nascimento = str(input("Insira a data de nascimento do usuário: (DD/MM/YY)"))
        cpf = int(input("Insira o cpf do usuário a ser cadastrado: (Digite apenas números)"))
        logradouro = str(input("Insira o seu logradouro: (Rua)"))
        numero = str(input("Insira o número de sua residência: "))
        bairro = str(input("Insira o bairro de sua residência: "))
        cidade = str(input("Insira a cidade de sua residência: "))
        estado = str(input("Insira a sigla de seu estado: (Exe: SP, RJ)"))     
          
        endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
         
        criar_usuario(nome, nascimento, cpf, endereco)
        
    elif opcao == "c":
        cpf = int(input("Insira o CPF cadastrado que será vinculado a conta: (Insira apenas números)"))
        criar_conta(cpf, agencia="0001")
        
    elif opcao == "q":
        break
 
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")