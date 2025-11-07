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

---

## 📖 PARTE TEÓRICA - ANÁLISE E DISCUSSÃO

### ❓ **Por que automação é importante na indústria?**

**Resposta:** A automação resolve problemas críticos da inspeção manual como inconsistência humana, lentidão e custos elevados. Ela garante precisão consistente, velocidade no processamento e capacidade de rastreamento completo de cada peça, eliminando erros de classificação e gargalos na produção.

### ❓ **Como você estruturou o raciocínio lógico do sistema?**

**Resposta:** Utilizei modularização com funções específicas para cada tarefa (cadastrar, validar, empacotar). As decisões foram baseadas em:
- **Condições**: `if/else` para validar peso, cor e comprimento
- **Repetições**: `while True` para menu contínuo e `for` para percorrer listas
- **Funções**: Separação clara de responsabilidades (cadastrar_peca, adicionar_na_caixa, etc.)
- **Estruturas de dados**: Listas para armazenamento e dicionários para organizar dados das peças

### ❓ **Quais benefícios e desafios você enfrentou no desenvolvimento?**

**Benefícios alcançados:**
- Sistema de segurança com autenticação por senha
- Geração automática de IDs únicos para rastreabilidade
- Interface colorida que melhora a experiência do usuário
- Automação completa desde validação até empacotamento
- Relatórios instantâneos com percentuais e estatísticas

**Desafios enfrentados:**
- Manter sincronização entre contadores e listas
- Implementar sistema de autenticação robusto com limite de tentativas
- Tratar erros de entrada de dados inválidos
- Combinar múltiplos critérios de validação simultaneamente

### ❓ **Como este protótipo poderia ser expandido para cenário real?**

**Resposta:** O sistema pode evoluir integrando:

**Sensores IoT:** Balanças industriais automáticas, câmeras para detecção de cor/dimensões, sensores de temperatura e umidade.

**Inteligência Artificial:** Machine Learning para detectar padrões de defeito, visão computacional para inspeção visual automática, análise preditiva para prever falhas.

**Integração Industrial:** Conexão com sistemas SCADA/MES, integração com ERP empresarial, dashboards web para gestores, armazenamento em nuvem e APIs para comunicação entre sistemas da fábrica.

**Escalabilidade:** Processamento de big data para análise de milhões de peças, sistema distribuído para múltiplas fábricas, cibersegurança industrial e analytics avançados para KPIs de performance.

---

##  Conceitos Acadêmicos Aplicados
- Algoritmos de validação
- Estruturas de controle (if/else, while)
- Modularização com funções
- Manipulação de listas e dicionários
- Interface de usuário simples
- Lógica de negócio industrial

---
**Desenvolvido para disciplina de Lógica de Programação - UNIFECAF 2025**