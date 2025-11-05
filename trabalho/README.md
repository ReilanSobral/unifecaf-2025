# Sistema de Controle de Produção de Peças

## 🔗 Repositório GitHub
**Link do projeto:** [https://github.com/ReilanSobral/unifecaf-2025](https://github.com/ReilanSobral/unifecaf-2025)

*📁 Navegue até a pasta `/trabalho` para acessar todos os arquivos do projeto*

## 📋 Descrição do Projeto
Sistema desenvolvido em Python para automatizar o controle de qualidade de peças em uma linha de produção industrial. O sistema avalia peças baseado em critérios pré-definidos e organiza as aprovadas em caixas.

##  Funcionalidades
-  Cadastro de peças com validação automática
-  Organização automática em caixas (10 peças por caixa)
-  Relatórios detalhados de produção
-  Listagem e remoção de peças
-  Análise de qualidade com percentuais

## 📏 Critérios de Aprovação
Uma peça é aprovada quando atende TODOS os critérios:
- **Peso**: entre 95g e 105g
- **Cor**: azul ou verde
- **Comprimento**: entre 10cm e 20cm

##  Como Executar

### Pré-requisitos
- Python 3.x instalado
- Terminal ou IDE Python
- Biblioteca colorama (para cores no terminal)

### Passos para Execução
1. Baixe os arquivos do projeto
2. Abra o terminal na pasta do projeto
3. Instale as dependências:
   pip install colorama
   
4. Execute o programa:
   python sistema_controle_pecas.py
   
4. Use o menu interativo para navegar pelas opções

##  Menu Principal
```
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
6. Sair do programa
```

##  Exemplos de Uso

### Exemplo 1: Peça Aprovada
```
Digite o ID da peça: P001
Digite o peso da peça (em gramas): 100
Digite a cor da peça: azul
Digite o comprimento da peça (em cm): 15

✅ Peça P001 APROVADA!
📦 Peça adicionada na caixa. Total na caixa: 1/10
```

### Exemplo 2: Peça Reprovada
```
Digite o ID da peça: P002
Digite o peso da peça (em gramas): 120
Digite a cor da peça: vermelha
Digite o comprimento da peça (em cm): 25

❌ Peça P002 REPROVADA!
   - Peso fora do padrão: 120.0g
   - Cor inválida: vermelha
   - Comprimento fora do padrão: 25.0cm
```

### Exemplo 3: Relatório Final
```
==================================================
                   RELATÓRIO FINAL
==================================================
📊 Total de peças processadas: 15
✅ Peças aprovadas: 12
❌ Peças reprovadas: 3
📈 Taxa de aprovação: 80.0%
📦 Caixas fechadas: 1
📦 Caixa atual: 2/10 peças

❌ PRINCIPAIS MOTIVOS DE REPROVAÇÃO:
   - Peso fora do padrão: 2 vezes
   - Cor inválida: 1 vezes
   - Comprimento fora do padrão: 1 vezes
==================================================
```

##  Estrutura do Código

### Conceitos Python Utilizados
- **Listas**: Armazenamento de peças e caixas
- **Dicionários**: Estrutura de dados das peças
- **Funções**: Organização do código em módulos
- **Loops**: Menu principal e iterações
- **Condicionais**: Validação de critérios
- **Input/Output**: Interação com usuário

### Principais Funções
- `cadastrar_peca()`: Cadastra e valida nova peça
- `adicionar_na_caixa()`: Gerencia caixas automaticamente
- `listar_pecas()`: Exibe peças aprovadas/reprovadas
- `remover_peca()`: Remove peça por ID
- `listar_caixas()`: Mostra caixas fechadas
- `gerar_relatorio()`: Relatório consolidado
- `main()`: Loop principal do programa

##  Tecnologias Utilizadas
- **Python 3.x**
- **Estruturas de dados nativas** (listas, dicionários)
- **Programação procedural**
- **Interface via terminal**

## 📊 Benefícios da Solução
- ✅ Automatização do controle de qualidade
- ✅ Redução de erros humanos
- ✅ Relatórios instantâneos
- ✅ Organização automática em caixas
- ✅ Rastreabilidade completa das peças

##  Conceitos Acadêmicos Aplicados
- Algoritmos de validação
- Estruturas de controle (if/else, while)
- Modularização com funções
- Manipulação de listas e dicionários
- Interface de usuário simples
- Lógica de negócio industrial

---
**Desenvolvido para disciplina de Lógica de Programação - UNIFECAF 2025**