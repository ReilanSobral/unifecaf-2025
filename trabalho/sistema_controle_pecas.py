# Sistema de Controle de Produção de Peças
# Trabalho de Lógica de Programação - UNIFECAF 2025

# Importações Cor
from colorama import init, Fore

# Inicializa colorama para cores no terminal
init(autoreset=True)

# Sistema de Autenticação
print(Fore.CYAN + "🔐 Sistema de Controle de Produção - Login Obrigatório")
print("="*50)

senha_cadastrada = "123"
senha_digitada = input("Digite sua senha: ")
quantidade_tentativas = 1

while senha_digitada != senha_cadastrada:
    quantidade_tentativas += 1
    if quantidade_tentativas > 3:
        print(Fore.RED + "❌ Número máximo de tentativas excedido. Acesso bloqueado.")
        exit()  # Para o programa completamente
    
    senha_digitada = input(Fore.RED + "Senha incorreta, tente novamente: ")

print(Fore.GREEN + "✅ Senha correta! Acesso liberado.")
print("="*50)
print("="*50)

# Listas para armazenar os dados (banco de dados simples)
pecas_aprovadas = []
pecas_reprovadas = []
caixas_fechadas = []
caixa_atual = []

# Contador para ID automático
proximo_id = 1

def cadastrar_peca():
    """Função para cadastrar uma nova peça"""
    global proximo_id
    
    print("\n--- CADASTRAR NOVA PEÇA ---")
    
    # ID do produto (não permite repetição)
    id_peca = proximo_id
    proximo_id += 1  
    
    print(f"🆔 ID da peça: {id_peca} (gerado automaticamente)")
    
    # Recebe os dados da peça
    peso = float(input("Digite o peso da peça (em gramas): "))
    cor = input("Digite a cor da peça: ").lower()
    comprimento = float(input("Digite o comprimento da peça (em cm): "))
    
    # Cria um dicionário com os dados da peça
    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento
    }
    
    # Verifica se a peça está aprovada
    motivos_reprovacao = []
    
    # Verifica peso (95g a 105g)
    if peso < 95 or peso > 105:
        motivos_reprovacao.append(f"Peso fora do padrão: {peso}g")
    
    # Verifica cor (azul ou verde)
    if cor != "azul" and cor != "verde":
        motivos_reprovacao.append(f"Cor inválida: {cor}")
    
    # Verifica comprimento (10cm a 20cm)
    if comprimento < 10 or comprimento > 20:
        motivos_reprovacao.append(f"Comprimento fora do padrão: {comprimento}cm")
    
    # Se não tem motivos de reprovação, peça está aprovada
    if len(motivos_reprovacao) == 0:
        pecas_aprovadas.append(peca)
        adicionar_na_caixa(peca)
        print(Fore.GREEN + f"✅ Peça {id_peca} APROVADA!")
    else:
        peca["motivos_reprovacao"] = motivos_reprovacao
        pecas_reprovadas.append(peca)
        print(Fore.RED + f"❌ Peça {id_peca} REPROVADA!")
        for motivo in motivos_reprovacao:
            print(Fore.YELLOW + f"   - {motivo}")

def adicionar_na_caixa(peca):
    """Adiciona peça na caixa atual"""
    global caixa_atual
    
    caixa_atual.append(peca)
    print(Fore.CYAN + f"📦 Peça adicionada na caixa. Total na caixa: {len(caixa_atual)}/10")
    
    # Se a caixa está cheia (10 peças), fecha ela
    if len(caixa_atual) == 10:
        caixas_fechadas.append(caixa_atual.copy())
        print(Fore.MAGENTA + f"🔒 Caixa {len(caixas_fechadas)} fechada! Nova caixa iniciada.")
        caixa_atual = []

def listar_pecas():
    """Lista todas as peças aprovadas e reprovadas"""
    print("\n--- LISTA DE PEÇAS ---")
    
    print(f"\n✅ PEÇAS APROVADAS ({len(pecas_aprovadas)}):")
    if len(pecas_aprovadas) == 0:
        print("   Nenhuma peça aprovada.")
    else:
        for peca in pecas_aprovadas:
            print(f"   ID: {peca['id']} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
    
    print(f"\n❌ PEÇAS REPROVADAS ({len(pecas_reprovadas)}):")
    if len(pecas_reprovadas) == 0:
        print("   Nenhuma peça reprovada.")
    else:
        for peca in pecas_reprovadas:
            print(f"   ID: {peca['id']} | Motivos: {', '.join(peca['motivos_reprovacao'])}")

def remover_peca():
    """Remove uma peça cadastrada"""
    print("\n--- REMOVER PEÇA ---")
    
    try:
        id_busca = int(input("Digite o ID da peça que deseja remover: "))
    except ValueError:
        print("❌ ID inválido! Digite apenas números.")
        return
    
    # Busca nas peças aprovadas
    for i, peca in enumerate(pecas_aprovadas):
        if peca["id"] == id_busca:
            pecas_aprovadas.pop(i)
            print(f"✅ Peça {id_busca} removida das aprovadas!")
            return
    
    # Busca nas peças reprovadas
    for i, peca in enumerate(pecas_reprovadas):
        if peca["id"] == id_busca:
            pecas_reprovadas.pop(i)
            print(f"✅ Peça {id_busca} removida das reprovadas!")
            return
    
    print(f"❌ Peça {id_busca} não encontrada!")

def listar_caixas():
    """Lista todas as caixas fechadas"""
    print("\n--- CAIXAS FECHADAS ---")
    
    if len(caixas_fechadas) == 0:
        print("   Nenhuma caixa fechada ainda.")
    else:
        for i, caixa in enumerate(caixas_fechadas):
            print(f"\n📦 Caixa {i + 1} (10 peças):")
            for peca in caixa:
                print(f"   - ID: {peca['id']}")
    
    # Mostra caixa atual se tiver peças
    if len(caixa_atual) > 0:
        print(f"\n📦 Caixa atual ({len(caixa_atual)}/10 peças):")
        for peca in caixa_atual:
            print(f"   - ID: {peca['id']}")

def gerar_relatorio():
    """Gera relatório final consolidado"""
    print("\n" + "="*50)
    print("           RELATÓRIO FINAL")
    print("="*50)
    
    # Total de peças
    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas)
    total_pecas = total_aprovadas + total_reprovadas
    
    print(f"📊 Total de peças processadas: {total_pecas}")
    print(f"✅ Peças aprovadas: {total_aprovadas}")
    print(f"❌ Peças reprovadas: {total_reprovadas}")
    
    if total_pecas > 0:
        percentual_aprovacao = (total_aprovadas / total_pecas) * 100
        print(f"📈 Taxa de aprovação: {percentual_aprovacao:.1f}%")
    
    # Caixas utilizadas
    total_caixas_fechadas = len(caixas_fechadas)
    print(f"📦 Caixas fechadas: {total_caixas_fechadas}")
    
    if len(caixa_atual) > 0:
        print(f"📦 Caixa atual: {len(caixa_atual)}/10 peças")
    
    # Motivos de reprovação mais comuns
    if len(pecas_reprovadas) > 0:
        print(f"\n❌ PRINCIPAIS MOTIVOS DE REPROVAÇÃO:")
        motivos_peso = 0
        motivos_cor = 0
        motivos_comprimento = 0
        
        for peca in pecas_reprovadas:
            for motivo in peca["motivos_reprovacao"]:
                if "Peso" in motivo:
                    motivos_peso += 1
                elif "Cor" in motivo:
                    motivos_cor += 1
                elif "Comprimento" in motivo:
                    motivos_comprimento += 1
        
        print(f"   - Peso fora do padrão: {motivos_peso} vezes")
        print(f"   - Cor inválida: {motivos_cor} vezes")
        print(f"   - Comprimento fora do padrão: {motivos_comprimento} vezes")
    
    print("="*50)

def mostrar_menu():
    """Mostra o menu principal"""
    print(Fore.BLUE + "\n" + "="*40)
    print(Fore.BLUE + "   SISTEMA DE CONTROLE DE PEÇAS")
    print(Fore.BLUE + "="*40)
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print(Fore.RED + "6. Sair do programa")
    print(Fore.BLUE + "="*40)

def main():
    """Função principal do programa"""
    print(Fore.GREEN + "🏭 Bem-vindo ao Sistema de Controle de Produção!")
    
    while True:
        mostrar_menu()
        opcao = input("Digite sua opção: ")
        
        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "6":
            print(Fore.GREEN + "👋 Saindo do sistema. Até logo!")
            break
        else:
            print(Fore.RED + "❌ Opção inválida! Tente novamente.")
        
        input(Fore.CYAN + "\nPressione ENTER para continuar...")

# Executa o programa
if __name__ == "__main__":
    main()