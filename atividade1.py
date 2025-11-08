from base_quente import CidadesQuente
from base_fria import CidadesFria


# FUNÇÃO PRINCIPAL
def recomenda_viage():

    # VERIFICAÇÃO DAS ETAPAS
    try:
        print("\n") # FORMATAÇÃO DO SISTEMA
        print(f"=======================================================")
        title = 'Sistema de Recomendação de Viagem'
        print(f"==========< {title} >==========")
        print(f"=======================================================")
        print(f"Ola Seja Bem Vindo ao {title}")

        # PERGUNTA 1 CLIMA
        print("""
        Me diga Você prefere clima quente ou frio?
        [1] clima quente
        [2] clima frio
        """)
        while True:
            clima = int(input('escolha uma opção: '))
            if clima in [1,2]:
                break
            else:
                print('Opção inválida! Digite 1 ou 2')

        # PERGUNTA 2 AMBIENTE
        print("""
        Qual a sua preferência: Natureza ou Paisagens urbanas?
        [1] Natureza
        [2] Urbana
        """)
        while True:
            ambiente = int(input('escolha uma opção: '))
            if ambiente in [1,2]:
                if ambiente == 1:
                    ambiente = str('Natureza')
                else:
                    ambiente = str('Urbana')
                break
            else:
                print('Opção inválida! Digite apenas 1 ou 2')

        # PERGUNTA 3 ORÇAMENTO
        print(
            """
        Qual é o seu orçamento para a viagem?
        [1] BAIXO
        [2] MÉDIO
        [3] ALTO
        [4] SEM LIMITE
        """
        )
        while True:
            orcamento = int(input('escolha uma opção: '))
            if orcamento in [1,2,3,4]:
                break
            else:
                print('Opção inválida! Digite apenas 1, 2, 3 ou 4')

        # ESTANCIANDO A BASE1
        if clima == 1:
            base_dados = CidadesQuente
        if clima == 2:
            base_dados = CidadesFria

        Sugestoes = []
        for i in range(0, len(base_dados)):
            if base_dados[i]['Ambiente'] == ambiente and orcamento == 1 and base_dados[i]['Orçamento'] <= 500:
                Sugestoes.append(base_dados[i])

            if base_dados[i]['Ambiente'] == ambiente and orcamento == 2 and base_dados[i]['Orçamento'] > 500 and base_dados[i]['Orçamento'] <= 1000:
                Sugestoes.append(CidadesQuente[i])

            if base_dados[i]['Ambiente'] == ambiente and orcamento == 3 and base_dados[i]['Orçamento'] > 1000 and base_dados[i]['Orçamento'] <= 1500:
                Sugestoes.append(base_dados[i])

            if base_dados[i]['Ambiente'] == ambiente and orcamento == 4 and base_dados[i]['Orçamento'] > 1500:
                Sugestoes.append(base_dados[i])
        if Sugestoes:
            # SAÍDA FORMATADA
            print('\n')
            print(f"===================< VOU TE DAR {len(Sugestoes)} SUGESTÔES PARA VOCÊ VIAJAR >====================")

            cont = 0
            for Lista in Sugestoes:
                cont += 1
                print(f"Sugestão {cont}")
                print(f"Cidade: {Lista['Cidade']}")
                print(f"Orçamento: R$ {Lista['Orçamento']:.2f}")
                print(f"Clima Predominate: {Lista['Clima']}")
                print(f"Ambiente: {Lista['Ambiente']}")
                print('\n')

            print('============================< FIM DO PROGRAMA >================================')
            print("\n")
        else:
            print(f"===================< DESCULPA NÃO ENCONTREI NENHUMA SUGESTÃO COM ESSAS CARACTERÍSTICAS PARA VOCÊ VIAJAR >====================")

    except:
        print(f"===================< ERRO AO EXECULTAR O PROGRAMA! TENTE NOVAMENTE >====================")


# EXECULTAR O PROGRAMA
if __name__ == '__main__':
    recomenda_viage()
