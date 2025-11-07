print("\n")
print(f"=======================================================")
title = 'Sistema de Recomendação de Viagem'
print(f"========== {title} ==========")
print(f"=======================================================")
print(f"Ola Seja Bem Vindo ao {title}")


#pergunta 1 clima
print("""
Me diga Você prefere clima quente ou frio?
[1] clima quente
[2] clima frio
""")
while True:
    clima = int(input('escolha uma opção: '))
    if clima in [1,2]:
        if clima == 1:
            clima = str('CLIMA QUENTE')
        else:
            clima = str('CLIMA FRIO')
        break
    else:
        print('Opção inválida! Digite 1 ou 2')

#pergunta 2 ambiente
print("""
Qual a sua preferência: Natureza ou Paisagens urbanas?
[1] NATUREZA
[2] PAISAGENS URBANAS
""")
while True:
    ambiente = int(input('escolha uma opção: '))
    if ambiente in [1,2]:
        if ambiente == 1:
            ambiente = str('NATUREZA')
        else:
            ambiente = str('PAISAGENS URBANAS')
        break
    else:
        print('Opção inválida! Digite apenas 1 ou 2')

#pergunta 3 orçamento
print("""
Qual é o seu orçamento para a viagem?
[1] BAIXO
[2] MÉDIO
[3] ALTO
""")
while True:
    orcamento = int(input('escolha uma opção: '))
    if orcamento in [1,2,3]:
        if orcamento == 1:
            orcamento = str('BAIXO')
        elif orcamento == 2:
            orcamento = str('MÉDIO')
        else: 
            orcamento = str('ALTO')
        break
    else:
        print('Opção inválida! Digite apenas 1, 2 ou 3')

print('\n')
print(f'SUAS CARACTERÍSTICAS DE VIAGEM E {clima}, {ambiente} e {orcamento}')
print('=================== FIM DO PROGRAMA ====================')
print("\n")