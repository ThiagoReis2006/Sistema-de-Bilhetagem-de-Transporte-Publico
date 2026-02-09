#Declaração de variáveis para a compra das passagens de acordo com o usuário.
comprar_passagem_padrao = 0
comprar_passagem_estudante_idoso = 0
comprar_passagem_social = 0 

#Declaração de variáveis para recargas de acordo com o usuário.
fazer_recarga_padrao = 0
fazer_recarga_estudante_idoso = 0
fazer_recarga_social = 0

#Declaração de variável para definir o valor da passagem.
valor_da_passagem = 0

#Declaração de variáveis para definir os menus.
menu = 0
menu_0 = 0
menu_1 = 0
menu_2 = 0

#Declaração de variáveis para futura impressão da quantidade de recarga total de acordo com o usuário.
quantidade_recarga_total_padrao = 0
quantidade_recarga_total_estudante_idoso = 0
quantidade_recarga_total_social = 0

#Declaração de variáveis para futura impressão do número de recargas feitas de acordo com o usuário.
numero_recargas_padrao = 0
numero_recargas_estudante_idoso = 0
numero_recargas_social = 0

#Declaração de variáveis para futura impressão da quantidade de passagens compradas de acordo com o usuário.
quantidade_passagens_compradas_padrao = 0
quantidade_passagens_compradas_estudante_idoso = 0
quantidade_passagens_compradas_social = 0

#Declaração de variáveis para futura impressão do valor total gasto com passagens de acordo com o usuário.
valor_total_gasto_passagens_padrao = 0
valor_total_gasto_passagens_estudante_idoso = 0
valor_total_gasto_passagens_social = 0

#Declaração de variáveis para futura impressão do saldo restante de acordo com o usuário.
saldo_restante_padrao = 0
saldo_restante_estudante_idoso = 0
saldo_restante_social = 0

#Declaração de variáveis que interrompem os loops.
continuar_1 = True
continuar_2 = True

#Estrutura de repetição que repete o código completo.
while continuar_1:  
    
    #Estrutura de repetição que encerra quanto o valor da passagem for válido.
    while continuar_2:
        
        #Estrutura que realiza a validação e verifica se ele é um número inteiro ou de ponto flutuante.
        try:
            
            #Imprime uma frase de boas-vindas.
            print("\nBem vindo à TechVille Transportes!\n")
    
            #Entrada de dados.
            valor_da_passagem = float (input("Digite o valor da passagem: "))

            #Estrutura condicional que verifica se o valor da passagem é maior do que 0.
            if valor_da_passagem > 0:
                print(f"\nRegistrado! Agora, a passagem custa {valor_da_passagem} créditos.\n")
                
                #Interrompe o loop.
                continuar_2 = False
            else:
                print("\nPor favor, digite um número maior do que 0.\n")

        except ValueError:
            print("\nPor favor, digite um número inteiro ou de ponto flutuante.\n")
    
       
    #Estrutura que realiza a validação e verifica se ele é um número inteiro.
    try:

        #Entrada de dados.
        menu = int (input ("\n 0 - Imprimir relatório.\n 1 - Fazer recarga.\n 2 - Comprar passagem.\n 3 - Sair.\n \nDigite um dos números acima para definir sua opção: "))

        #Estrutura condicional que executa os comandos adequados para cada opção do menu.
        match menu:

            case 0:
            
                #Estrutura que realiza a validação e verifica se ele é um número inteiro.
                try:
            
                    #Entrada de dados.
                    menu_0 = int (input("\n 1 - Usuário padrão.\n 2 - Usuário estudante/idoso.\n 3 - Usuário social.\n \nDigite um dos números acima para definir sua categoria: "))
        
                    #Estrutura condicional que executa os comandos adequados para cada categoria do menu.
                    match menu_0:

                        case 1:
        
                            #Imprime um relatório para o usuário padrão.
                            print("\nRelatório do usuário padrão: ")
                            print(f"\nQuantidade de recarga total = {quantidade_recarga_total_padrao} créditos.")
                            print(f"Número de recargas = {numero_recargas_padrao} recargas.")
                            print(f"Quantidade de passagens utilizadas = {quantidade_passagens_compradas_padrao} passagens.")
                            print(f"Valor total gasto com passagens = {valor_total_gasto_passagens_padrao} créditos.")
                            print(f"Saldo restante = {saldo_restante_padrao} créditos.")

                        case 2:

                            #Imprime um relatório para o usuário estudante/idoso.
                            print("\nRelatório do usuário estudante/idoso: ")
                            print(f"\nQuantidade de recarga total = {quantidade_recarga_total_estudante_idoso} créditos.")
                            print(f"Número de recargas = {numero_recargas_estudante_idoso} recargas.")
                            print(f"Quantidade de passagens utilizadas = {quantidade_passagens_compradas_estudante_idoso} passagens.")
                            print(f"Valor total gasto com passagens = {valor_total_gasto_passagens_estudante_idoso} créditos.")
                            print(f"Saldo restante = {saldo_restante_estudante_idoso} créditos.")
            
                        case 3:
                
                            #Imprime um relatório para o usuário social.
                            print("\nRelatório do usuário social: ")
                            print(f"\nQuantidade de recarga total = {quantidade_recarga_total_social} créditos.")
                            print(f"Número de recargas = {numero_recargas_social} recargas.")
                            print(f"Quantidade de passagens utilizadas = {quantidade_passagens_compradas_social} passagens.")
                            print(f"Valor total gasto com passagens = {valor_total_gasto_passagens_social} créditos.")
                            print(f"Saldo restante = {saldo_restante_social} créditos.")
                    
                        case _:
                            print("\nPor favor, digite um dos números do menu.\n")
            
                except ValueError:
                    print("\nPor favor, digite um número inteiro.\n")
    
            case 1:
            
                #Estrutura que realiza a validação e verifica se ele é um número inteiro.
                try:

                    #Entrada de dados.
                    menu_1 = int (input("\n 0 - Imprimir relatório.\n 1 - Usuário padrão.\n 2 - Usuário estudante/idoso.\n 3 - Usuário social.\n \nDigite um dos números acima para definir sua opção: "))

                    #Estrutura condicional que executa os comandos adequados para cada categoria do menu.
                    match menu_1:

                        case 0:
                        
                            #Estrutura que realiza a validação e verifica se ele é um número inteiro.
                            try:
                            
                                #Entrada de dados.
                                menu_0 = int (input("\n 1 - Usuário padrão.\n 2 - Usuário estudante/idoso.\n 3 - Usuário social.\n \nDigite um dos números acima para definir sua categoria: "))
        
                                #Estrutura condicional que executa os comandos adequados para cada categoria do menu.
                                match menu_0:

                                    case 1:
        
                                        #Imprime um relatório para o usuário padrão.
                                        print("\nRelatório do usuário padrão: ")
                                        print(f"\nQuantidade de recarga total = {quantidade_recarga_total_padrao} créditos.")
                                        print(f"Número de recargas = {numero_recargas_padrao} recargas.")
                                        print(f"Quantidade de passagens utilizadas = {quantidade_passagens_compradas_padrao} passagens.")
                                        print(f"Valor total gasto com passagens = {valor_total_gasto_passagens_padrao} créditos.")
                                        print(f"Saldo restante = {saldo_restante_padrao} créditos.")

                                    case 2:

                                        #Imprime um relatório para o usuário estudante/idoso.
                                        print("\nRelatório do usuário estudante/idoso: ")
                                        print(f"\nQuantidade de recarga total = {quantidade_recarga_total_estudante_idoso} créditos.")
                                        print(f"Número de recargas = {numero_recargas_estudante_idoso} recargas.")
                                        print(f"Quantidade de passagens utilizadas = {quantidade_passagens_compradas_estudante_idoso} passagens.")
                                        print(f"Valor total gasto com passagens = {valor_total_gasto_passagens_estudante_idoso} créditos.")
                                        print(f"Saldo restante = {saldo_restante_estudante_idoso} créditos.")
            
                                    case 3:
                
                                        #Imprime um relatório para o usuário social.
                                        print("\nRelatório do usuário social: ")
                                        print(f"\nQuantidade de recarga total = {quantidade_recarga_total_social} créditos.")
                                        print(f"Número de recargas = {numero_recargas_social} recargas.")
                                        print(f"Quantidade de passagens utilizadas = {quantidade_passagens_compradas_social} passagens.")
                                        print(f"Valor total gasto com passagens = {valor_total_gasto_passagens_social} créditos.")
                                        print(f"Saldo restante = {saldo_restante_social} créditos.")
                                    
                                    case _:
                                        print("\nPor favor, digite um dos números do menu.\n")
                        
                            except ValueError:
                                print("\nPor favor, digite um número inteiro.\n")

                        case 1:
                        
                            #Estrutura que realiza a validação e verifica se ele é um número inteiro ou de ponto flutuante.
                            try:
                
                                #Entrada de dados.
                                fazer_recarga_padrao = float (input("\nDigite quanto você quer recarregar: "))

                                #Estrutura condicional que verifica se o valor da recarga é maior do que 0.
                                if fazer_recarga_padrao > 0:
                                    
                                    #Atribuições para as variáveis (processamento de dados).
                                    quantidade_recarga_total_padrao += fazer_recarga_padrao
                                    numero_recargas_padrao += 1
                                    saldo_restante_padrao += quantidade_recarga_total_padrao
                                    
                                    print (f"\nParabéns! Você fez uma recarga de {fazer_recarga_padrao} créditos.\n")
                                else:
                                    print ("\nPor favor, digite um número maior do que 0.\n")
                        
                            except ValueError:
                                print("\nPor favor, digite um número inteiro ou de ponto flutuante.\n")

                        case 2:

                            #Estrutura que realiza a validação e verifica se ele é um número inteiro ou de ponto flutuante.
                            try:
                            
                                #Entrada de dados.
                                fazer_recarga_estudante_idoso = float (input("\nDigite quanto você quer recarregar: "))

                                #Estrutura condicional que verifica se o valor da recarga é maior do que 0.
                                if fazer_recarga_estudante_idoso > 0:
                                    
                                    #Atribuições para as variáveis (processamento de dados).
                                    quantidade_recarga_total_estudante_idoso += fazer_recarga_estudante_idoso
                                    numero_recargas_estudante_idoso += 1
                                    saldo_restante_estudante_idoso += quantidade_recarga_total_estudante_idoso
                                    
                                    print (f"\nParabéns! Você fez uma recarga de {fazer_recarga_estudante_idoso} créditos.\n")
                                else:
                                    print ("\nPor favor, digite um número maior do que 0.\n")
                        
                            except ValueError:
                                print("\nPor favor, digite um número inteiro ou de ponto flutuante.\n")

                        case 3:

                            #Estrutura que realiza a validação e verifica se ele é um número inteiro ou de ponto flutuante.
                            try:
                            
                                #Entrada de dados.
                                fazer_recarga_social = float (input("\nDigite quanto você quer recarregar: "))

                                #Estrutura condicional que verifica se o valor da recarga é maior do que 0.
                                if fazer_recarga_social > 0:
                                    
                                    #Atribuições para as variáveis (processamento de dados).
                                    quantidade_recarga_total_social += fazer_recarga_social
                                    numero_recargas_social += 1
                                    saldo_restante_social += quantidade_recarga_total_social 
                                    
                                    print (f"\nParabéns! Você fez uma recarga de {fazer_recarga_social} créditos.\n")
                                else:
                                    print ("\nPor favor, digite um número maior do que 0.\n")
                        
                            except ValueError:
                                print("\nPor favor, digite um número inteiro ou de ponto flutuante.\n")
                            
                        case _:
                            print("\nPor favor, digite um dos números do menu.\n")
            
                except ValueError:
                    print("\nPor favor, digite um número inteiro.\n")

            case 2:
            
                #Estrutura que realiza a validação e verifica se ele é um número inteiro.
                try:
                
                    #Entrada de dados.
                    menu_2 = int (input("\n 0 - Imprimir relatório.\n 1 - Usuário padrão.\n 2 - Usuário estudante/idoso.\n 3 - Usuário social.\n \nDigite um dos números acima para definir sua opção: "))

                    #Estrutura condicional que executa os comandos adequados para cada categoria do menu.
                    match menu_2:

                        case 0:
                        
                            #Estrutura que realiza a validação e verifica se ele é um número inteiro.
                            try:
                        
                                #Entrada de dados.
                                menu_0 = int (input("\n 1 - Usuário padrão.\n 2 - Usuário estudante/idoso.\n 3 - Usuário social.\n \nDigite um dos números acima para definir sua categoria: "))
        
                                #Estrutura condicional que executa os comandos adequados para cada categoria do menu.
                                match menu_0:

                                    case 1:
        
                                        #Imprime um relatório para o usuário padrão.
                                        print("\nRelatório do usuário padrão: ")
                                        print(f"\nQuantidade de recarga total = {quantidade_recarga_total_padrao} créditos.")
                                        print(f"Número de recargas = {numero_recargas_padrao} recargas.")
                                        print(f"Quantidade de passagens utilizadas = {quantidade_passagens_compradas_padrao} passagens.")
                                        print(f"Valor total gasto com passagens = {valor_total_gasto_passagens_padrao} créditos.")
                                        print(f"Saldo restante = {saldo_restante_padrao} créditos.")

                                    case 2:

                                        #Imprime um relatório para o usuário estudante/idoso.
                                        print("\nRelatório do usuário estudante/idoso: ")
                                        print(f"\nQuantidade de recarga total = {quantidade_recarga_total_estudante_idoso} créditos.")
                                        print(f"Número de recargas = {numero_recargas_estudante_idoso} recargas.")
                                        print(f"Quantidade de passagens utilizadas = {quantidade_passagens_compradas_estudante_idoso} passagens.")
                                        print(f"Valor total gasto com passagens = {valor_total_gasto_passagens_estudante_idoso} créditos.")
                                        print(f"Saldo restante = {saldo_restante_estudante_idoso} créditos.")
            
                                    case 3:
                
                                        #Imprime um relatório para o usuário social.
                                        print("\nRelatório do usuário social: ")
                                        print(f"\nQuantidade de recarga total = {quantidade_recarga_total_social} créditos.")
                                        print(f"Número de recargas = {numero_recargas_social} recargas.")
                                        print(f"Quantidade de passagens utilizadas = {quantidade_passagens_compradas_social} passagens.")
                                        print(f"Valor total gasto com passagens = {valor_total_gasto_passagens_social} créditos.")
                                        print(f"Saldo restante = {saldo_restante_social} créditos.")
                                
                                    case _:
                                        print("\nPor favor, digite um dos números do menu.\n")
                        
                            except ValueError:
                                print("\nPor favor, digite um número inteiro.\n")
                        
                        case 1:

                            #Estrutura que realiza a validação e verifica se ele é um número inteiro.
                            try:
                            
                                #Entrada de dados.
                                comprar_passagem_padrao = int (input("\nDigite quantas passagens você quer comprar: "))

                                #Estrutura condicional que verifica se o valor da recarga é maior do que 0.
                                if comprar_passagem_padrao > 0:
                                    #Estrutura condicional que verifica se o saldo é suficiente.
                                    if saldo_restante_padrao >= (comprar_passagem_padrao * valor_da_passagem):
                                        
                                        #Atribuições para as variáveis (processamento de dados).
                                        valor_total_gasto_passagens_padrao += (comprar_passagem_padrao * valor_da_passagem)
                                        quantidade_passagens_compradas_padrao += comprar_passagem_padrao
                                        saldo_restante_padrao -= valor_total_gasto_passagens_padrao
                                        
                                        print (f"\nParabéns! Você comprou {comprar_passagem_padrao} passagens.\n")
                                    else:
                                        print ("\nSaldo insuficiente!\n")
                                else:
                                    print ("Por favor, digite um número maior do que 0.\n")
                                
                            except ValueError:
                                print("Por favor, digite um número inteiro.")
            
                        case 2:
                        
                            #Estrutura que realiza a validação e verifica se ele é um número inteiro.
                            try:
                            
                                #Entrada de dados.
                                comprar_passagem_estudante_idoso = int (input("\nDigite quantas passagens você quer comprar: "))

                                #Estrutura condicional que verifica se o valor da recarga é maior do que 0.
                                if comprar_passagem_estudante_idoso > 0:
                                    #Estrutura condicional que verifica se o saldo é suficiente.
                                    if saldo_restante_estudante_idoso >= (comprar_passagem_estudante_idoso * (valor_da_passagem * 0.5)):
                                        
                                        #Atribuições para as variáveis (processamento de dados).
                                        valor_total_gasto_passagens_estudante_idoso += (comprar_passagem_estudante_idoso * (valor_da_passagem * 0.5))                                                                                     
                                        quantidade_passagens_compradas_estudante_idoso += comprar_passagem_estudante_idoso
                                        saldo_restante_estudante_idoso -= valor_total_gasto_passagens_estudante_idoso
                                        
                                        print (f"\nParabéns! Você comprou {comprar_passagem_estudante_idoso} passagens.\n")
                                    else:
                                        print ("\nSaldo insuficiente!\n")
                                else:
                                    print ("\nPor favor, digite um número maior do que 0.\n")
                        
                            except ValueError:
                                print("\nPor favor, digite um número inteiro.\n")

                        case 3:
                            
                            #Estrutura que realiza a validação e verifica se ele é um número inteiro.
                            try:
                        
                                #Entrada de dados.
                                comprar_passagem_social = int (input("\nDigite quantas passagens você quer comprar: "))

                                #Estrutura condicional que verifica se o valor da recarga é maior do que 0.
                                if comprar_passagem_social > 0:
                                    #Estrutura condicional que verifica se o saldo é suficiente.
                                    if saldo_restante_social >= (comprar_passagem_social * (valor_da_passagem * 0.2)):
                                        
                                        #Atribuições para as variáveis (processamento de dados).
                                        valor_total_gasto_passagens_social += (comprar_passagem_social * (valor_da_passagem * 0.2))
                                        quantidade_passagens_compradas_social += comprar_passagem_social
                                        saldo_restante_social -= valor_total_gasto_passagens_social
                                        
                                        print (f"\nParabéns! Você comprou {comprar_passagem_social} passagens.\n")
                                    else:
                                        print ("\nSaldo insuficiente!\n")
                                else:
                                    print ("\nPor favor, digite um número maior do que 0.\n")
                                
                            except ValueError:
                                print("\nPor favor, digite um número inteiro.\n")
                            
                        case _:
                            print("\nPor favor, digite um dos números do menu.\n")
                        
                except ValueError:
                    print("\nPor favor, digite um número inteiro.\n")
    
            case 3:
                exit("\nObrigado pela presença. Até mais!\n")
                
            case _:
                print("\nPor favor, digite um dos números do menu.\n")

    except ValueError:
        print("\nPor favor, digite um número inteiro.\n")