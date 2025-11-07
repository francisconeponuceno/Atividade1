import random

# --- 1. FUNÇÃO PRINCIPAL PARA RECOMENDAR VIAGEM ---
def recomendar_viagem():
    """
    Função que faz 3 perguntas ao usuário, classifica o perfil
    e sugere um destino de viagem ideal.
    """
    print("--- ✈️ Recomendador de Viagens Python ---")
    
    # --- 2. FAZER AS PERGUNTAS E COLETAR RESPOSTAS ---
    
    # Pergunta 1: Clima
    while True:
        clima = input("1. Você prefere clima **quente** ou **frio**? ").lower().strip()
        if clima in ['quente', 'frio']:
            break
        else:
            print("Resposta inválida. Por favor, digite 'quente' ou 'frio'.")

    # Pergunta 2: Ambiente
    while True:
        ambiente = input("2. Você prefere lugares com **natureza** ou paisagens **urbanas**? ").lower().strip()
        if ambiente in ['natureza', 'urbanas']:
            break
        else:
            print("Resposta inválida. Por favor, digite 'natureza' ou 'urbanas'.")
            
    # Pergunta 3: Orçamento
    while True:
        try:
            orcamento = float(input("3. Qual é o seu orçamento disponível para a viagem (em Reais - ex: 5000)? R$ "))
            if orcamento > 0:
                break
            else:
                print("O orçamento deve ser um valor positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números para o orçamento.")

    # --- 3. CLASSIFICAR O PERFIL DO VIAJANTE ---
    
    # Define o custo (simplesmente classificando o valor)
    if orcamento >= 8000:
        custo = "alto"
    elif orcamento >= 3000:
        custo = "médio"
    else:
        custo = "baixo"
        
    # --- 4. MAPEAR AS RECOMENDAÇÕES (BASEDAS NAS RESPOSTAS) ---
    
    # Dicionário de destinos (pode ser expandido!)
    # Chave: (clima, ambiente, custo)
    recomendacoes = {
        ('quente', 'natureza', 'alto'): "Fernando de Noronha (PE) - Mergulho e praias exclusivas.",
        ('quente', 'natureza', 'médio'): "Jalapão (TO) - Aventura em fervedouros e dunas.",
        ('quente', 'natureza', 'baixo'): "Praias do Nordeste com pousadas simples (Ex: Jericoacoara, CE).",
        
        ('quente', 'urbanas', 'alto'): "Rio de Janeiro (RJ) - Lazer, cultura e alta gastronomia.",
        ('quente', 'urbanas', 'médio'): "Salvador (BA) - História, música e culinária.",
        ('quente', 'urbanas', 'baixo'): "Recife/Olinda (PE) - Cultura e história acessíveis.",
        
        ('frio', 'natureza', 'alto'): "Chapada dos Guimarães (MT) no inverno ou Serras do RS/SC com hotéis de luxo.",
        ('frio', 'natureza', 'médio'): "Serra Gaúcha (RS) ou Serra Catarinense (SC) - Vinícolas e paisagens frias.",
        ('frio', 'natureza', 'baixo'): "Paranapiacaba (SP) ou cidades serranas de MG/SP mais simples.",
        
        ('frio', 'urbanas', 'alto'): "Curitiba (PR) - Cidade organizada e fria com excelente infraestrutura.",
        ('frio', 'urbanas', 'médio'): "Campos do Jordão (SP) - Clima europeu e eventos de inverno.",
        ('frio', 'urbanas', 'baixo'): "Cidades históricas de Minas Gerais no inverno."
    }
    
    # Constrói a chave de busca
    chave = (clima, ambiente, custo)
    
    # Tenta obter a recomendação
    recomendacao = recomendacoes.get(chave, "Não foi possível encontrar uma recomendação exata, mas explore o Brasil! Você busca um lugar **{}**, com foco em **{}** e orçamento **{}**.".format(clima.upper(), ambiente.upper(), custo.upper()))
    
    # --- 5. EXIBIR O RESULTADO ---
    print("\n" + "="*50)
    print(f"✔️ O seu perfil de viajante é: CLIMA {clima.upper()} | AMBIENTE {ambiente.upper()} | CUSTO {custo.upper()}")
    print("-" * 50)
    print(f"✨ Recomendação Ideal: {recomendacao}")
    print("="*50)

# --- 6. EXECUTAR O PROGRAMA ---
if __name__ == "__main__":
    recomendar_viagem()