'''vagas = {"Analista de Dados Jr": ["python", "dados", "sql"],                    #Dicionário de apoio para o programador. não tem função efetiva no código.
         "Desenvolvedor back-end": ["java", "Php", "desenvolvedor"]
}'''

def findCandidatos ():                      #def que irá fazer a filtragem dos candidatos
    candidatosV1 = {}                       #\
    candidatosV2 = {}                        #\
    aptosv1 = {}                              #\
    aptosv2 = {}                               #\ Dicionários vazios que irão receber dados dos usuário conforme condicionáis ao longo do código.

    print( )
    print("##########{:^150}##########".format("BEM VINDO AO FIND CANDIDATOS"))
    print( )
   
    sair = 3
    while (sair != 0):                      #Estrutura de repetição para cadastrar candidatos 
        nome = str.title(input("Olá, candidato. Por favos nos diga seu nome para darmos continuidade: ")) #Nome do candidato
        resumo = str.lower(input("Faça um breve resumo sobre você e o por que deseja ingressar na Trust Companny\n"))  #Resumo onde o candidato irá colocar um resumo pessoal e iremos buscar nossas palavras chaves para saber se o mesmo é apto ou não.
        vaga = int(input("Para qual vaga você deseja se candidatar?\n[1] - Analista de Dados jr\n[2] - Desenvolvedor back end\nEscolha uma das opções: "))  #Variável onde o cancidato irá escolher para qual vaga deseja se inscrever.

        if (vaga == 1):                                  # Condicional para vaga de analista de dados
            candidatosV1.update({nome:resumo})           # usuário sendo inserido no dicionário dos candidatos incritos para vaga de Analista de Dados.
            if "python" and "dados" and "sql" in resumo: # Filtro onde buscamos as palavras chaves no resumo que o candidato fez sobre sí mesmo.
                aptosv1.update({nome:resumo})            # Condicional para colocar o candidato no dicionário de aptos para vaga de analista caso atenda os requisitos    

        elif (vaga == 2):                                # Aqui se repete a estrutura do if anterior mas mudando as palavras chaves e os dicionários que os candidatos serão enviados.
            candidatosV2.update({nome:resumo})
            if "java" and "php" and "desenvolvedor" in resumo:
                aptosv2.update({nome:resumo})

        else:
            print("Opção inválida")
       
        sair = int(input("Deseja inserir mais dados de candidatos?\n[1] - Sim\n[0] - Sair\nEscolha sua opção: "))   #Variável para sair do while
       
    print(f"Temos {len(candidatosV1)} candidatos inscritos para a vaga de Analista de Dados jr com {len(aptosv1)} aptos para prosseguir para a próxima etapa do processo seletivo."  )
    print(f"Temos {len(candidatosV2)} candidatos inscritos para a vaga de Desenvolvedor Backend com {len(aptosv2)} aptos para prosseguir para a próxima etapa do processo seletivo."  )
                                                                     #/\#
                    #Acima nós temos duas frases formatadas onde demonstrarmos a quantidade total de inscritos para cada vaga e a quantidade de aptos.

    print("-"*70)

    import pandas as pd
    if len(aptosv1) >0:          #Caso haja ao menos um candidato apto, será gerado um dataframe para melhor visualização do usuário. 
        dfaptos = pd.DataFrame(list(aptosv1))       #Frame sendo criado usando o dicionário mas transformando o mesmo em lista para melhor visualização
        dfaptos.columns = ["Candidato"]  # Alterando o nome da primeira coluna que era um numeral
        dfaptos["Situação"] = "Apto"  # Adicionando a coluna 'Situação' e 'apto' em todas as linhas já que usamos o dicionário onde todos são aptos.
        print("Os aprovados para próxima fase no processo seletivo para vaga de Analista de dados são:\n ")  #Print de apresentação do frame
        print(dfaptos)          #Finalmente o frame com os candidatos aptos
    else:
        print("Infelizmente nenhum candidato atendeu aos requisitos para prosseguir à próxima fase do processo seletivo para vaga de Analista de Dados.")
                                                        #/\#
                #Acima temos um print para caso não haja nenhum candidato apto.

    if len(aptosv2) >0:                 #Aqui se repete a mesma estrutura do frame anterior.
        dfaptos2 = pd.DataFrame(list(aptosv2))
        dfaptos2.columns = ["Candidato"]
        dfaptos2["Situação"] = "Apto"
        print("\n Os aprovados para próxima fase no processo seletivo para vaga de Desenvolvedor Backend são:\n")
        print(dfaptos2)
    
    else:
        print("Infelizmente nenhum candidato atendeu aos requisitos para prosseguir à próxima fase do processo seletivo para vaga de Desenvolvedor Back-end.")

    


findCandidatos()   #Chamando a função filtrar e buscar os candidatos aptos.

















