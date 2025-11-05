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

### 🏭 Contextualização do Desafio: Por que Automação é Importante na Indústria

A automação industrial representa uma revolução fundamental nos processos produtivos modernos. No contexto do controle de qualidade de peças, a automação resolve problemas críticos:

**Problemas do Processo Manual:**
- 🔍 **Inconsistência humana** - Fadiga e variação na precisão de inspeção
- ⏱️ **Lentidão** - Gargalos na linha de produção
- 💰 **Custos elevados** - Necessidade de múltiplos inspetores
- 📊 **Falta de dados** - Dificuldade em gerar relatórios precisos
- ❌ **Erros de classificação** - Peças defeituosas aprovadas ou boas reprovadas

**Benefícios da Automação:**
- 🎯 **Precisão consistente** - Critérios rigorosos aplicados 100% das vezes
- ⚡ **Velocidade** - Processamento instantâneo de cada peça
- 📈 **Escalabilidade** - Capacidade de processar milhares de peças
- 🔄 **Rastreabilidade completa** - Histórico detalhado de cada item

### 🧠 Estruturação do Raciocínio Lógico

**1. Decisões de Arquitetura:**
- **Modularização**: Cada funcionalidade em uma função específica (`cadastrar_peca()`, `adicionar_na_caixa()`, etc.)
- **Estruturas de dados**: Listas para armazenamento simples, dicionários para dados estruturados das peças
- **Fluxo sequencial**: Sistema guiado por menu para facilitar uso industrial

**2. Funções Implementadas:**
- **Sistema de autenticação** - Segurança de acesso
- **Validação automática** - Aplicação rigorosa dos 3 critérios de qualidade
- **Empacotamento inteligente** - Caixas fecham automaticamente ao atingir 10 peças
- **Relatórios gerenciais** - Estatísticas em tempo real

**3. Condições e Validações:**
- **Peso**: `if peso < 95 or peso > 105` - Validação de faixa numérica
- **Cor**: `if cor != "azul" and cor != "verde"` - Validação de opções específicas
- **Comprimento**: `if comprimento < 10 or comprimento > 20` - Controle dimensional

**4. Estruturas de Repetição:**
- **Menu principal**: `while True` - Loop infinito para operação contínua
- **Autenticação**: `while senha_digitada != senha_cadastrada` - Repetição até acesso correto
- **Iterações**: `for` loops para exibir listas e gerar relatórios

### ✅ Benefícios Percebidos + Desafios Enfrentados

**Benefícios Alcançados:**
- 🔐 **Segurança integrada** - Sistema de login protege acesso não autorizado
- 🆔 **IDs únicos automáticos** - Evita duplicações e garante rastreabilidade
- 🎨 **Interface visual atrativa** - Cores melhoram experiência do usuário
- 📦 **Automação completa** - Desde validação até empacotamento
- 📊 **Business Intelligence** - Relatórios com percentuais e tendências

**Desafios Técnicos Enfrentados:**
- 🔄 **Sincronização de estado** - Manter contadores e listas sempre atualizados
- 🔒 **Sistema de autenticação robusto** - Implementar limite de tentativas e bloqueio
- 📝 **Validação de entrada** - Tratar erros de digitação e dados inválidos
- 🎯 **Lógica de múltiplos critérios** - Combinar 3 validações simultâneas
- 💾 **Gerenciamento de memória** - Organizar dados sem banco de dados real

**Lições Aprendidas:**
- Importância da modularização para manutenibilidade
- Necessidade de feedback visual claro para o usuário
- Valor da automação mesmo em protótipos simples

### 🚀 Reflexão Final: Expansão para Cenário Real

**Integração com Sensores IoT:**
- 📏 **Sensores de peso** - Balanças industriais conectadas via protocolo Modbus
- 📸 **Visão computacional** - Câmeras para detecção automática de cor e dimensões
- 🌡️ **Sensores ambientais** - Temperatura e umidade para controle de qualidade

**Implementação de Inteligência Artificial:**
- 🤖 **Machine Learning** - Algoritmos preditivos para detectar padrões de defeito
- 👁️ **Computer Vision** - Reconhecimento de imagem para inspeção visual avançada
- 📈 **Análise preditiva** - Previsão de falhas antes que ocorram
- 🧮 **Otimização automática** - IA ajustando parâmetros de produção

**Integração Industrial Completa:**
- 🏭 **SCADA/MES** - Integração com sistemas de supervisão industrial
- 🔄 **ERP** - Conexão com sistemas de gestão empresarial
- 📱 **Dashboard web** - Interface remota para gerentes e operadores
- ☁️ **Cloud Computing** - Armazenamento e processamento em nuvem
- 🔗 **APIs RESTful** - Integração com outros sistemas da fábrica

**Escalabilidade Empresarial:**
- 📊 **Big Data** - Análise de milhões de peças para insights estratégicos
- 🌐 **Multi-unidades** - Sistema distribuído entre várias fábricas
- 🔒 **Cibersegurança industrial** - Proteção contra ataques a infraestrutura crítica
- 📈 **Analytics avançados** - KPIs e métricas de performance industrial

**Impacto Estratégico:**
Este protótipo demonstra como conceitos fundamentais de programação podem resolver problemas industriais reais. A evolução natural seria uma plataforma completa de Indústria 4.0, integrando IoT, IA e análise de dados para otimização contínua da produção.

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