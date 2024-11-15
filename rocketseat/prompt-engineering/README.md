# 🧠 **Técnicas de Prompting**

## 1️⃣ **Técnicas Aplicadas Diretamente no Chat**

### ✨ 1.1. Zero-shot Prompting
O **Zero-shot Prompting** consiste em solicitar uma tarefa ao modelo sem fornecer exemplos específicos.  
✅ **Ideal para:** perguntas diretas ou solicitações simples.

💡 **Exemplo de Prompt:**  
*"Explique o conceito de machine learning em poucas palavras."*

---

### 🤏 1.2. Few-shot Prompting
O **Few-shot Prompting** fornece alguns exemplos para orientar o modelo antes da solicitação principal.  
✅ **Ideal para:** tarefas específicas que requerem mais precisão.

💡 **Exemplo de Prompt:**  
*"Aqui está um exemplo de como descrever animais: 'Um cachorro é um animal de quatro patas que late'. Agora, descreva um elefante."*

---

### 🧩 1.3. Chain-of-Thought Prompting (CoT)
O **Chain-of-Thought Prompting** incentiva o modelo a "pensar em voz alta", decompondo problemas complexos em passos intermediários.  
✅ **Ideal para:** problemas matemáticos e de lógica.

💡 **Dica:** Inclua *"vamos pensar passo a passo"* no prompt para melhores resultados.

📘 **Exemplo de Prompt:**  
*"João tem 12 maçãs e dá 3 para cada um dos seus 4 amigos. Explique passo a passo quantas maçãs ele fica no final."*

---

### 🎯 1.4. Context, Instructions, Details, Input (CIDI)
A técnica **CIDI** estrutura o prompt com:  
- **📌 Contexto**
- **📋 Instruções claras**
- **🔍 Detalhes específicos**
- **✏️ Dados de entrada**  

✅ **Ideal para:** cenários que exigem respostas precisas e detalhadas.

💡 **Exemplo de Prompt:**  
*"Você é um assistente de IA para planejamento financeiro. Um cliente quer saber como economizar para uma viagem de um ano. Considere suas despesas mensais e sugira um plano."*

---

## 2️⃣ **Técnicas Aplicadas Programaticamente**

### 🛠️ 2.1. Context, Instructions, Details, Input (CIDI)
Aplicada programaticamente, a técnica **CIDI** configura o contexto diretamente no código, incluindo detalhes sobre a tarefa e expectativas de resposta.  
✅ **Ideal para:** sistemas automatizados.

💡 **Exemplo de Prompt:**  
*"No contexto de uma aplicação médica, explique ao paciente o que esperar após uma cirurgia de apendicite. Inclua informações sobre repouso e dieta."*

---

### 🌳 2.2. Tree of Thoughts
A técnica **Tree of Thoughts** ajuda o modelo a explorar alternativas e caminhos lógicos, criando uma “árvore” de ideias.  
✅ **Ideal para:** resolver problemas complexos com várias abordagens possíveis.

💡 **Exemplo de Prompt:**  
*"Liste possíveis métodos para resolver o problema de trânsito em uma cidade grande e discuta as vantagens e desvantagens de cada um."*

---

### 📚 2.3. Retrieval Augmented Generation (RAG)
O **RAG** combina o modelo com recuperação de informações externas (bases de dados, documentos).  
✅ **Ideal para:** respostas que precisam de informações atualizadas ou contextuais.

💡 **Exemplo de Prompt:**  
*"Encontre as últimas estatísticas sobre o mercado de trabalho em tecnologia e resuma as principais tendências."*

---

### 🔄 2.4. ReAct Prompting
O **ReAct Prompting** mistura raciocínio lógico com ferramentas específicas, ajustando a resposta conforme necessário.  
✅ **Ideal para:** tarefas interativas e adaptativas.

💡 **Exemplo de Prompt:**  
*"Você é um consultor de viagens ajudando o cliente a planejar uma viagem de três dias para Nova York. Sugerindo atrações, ajuste o itinerário com base nas preferências de passeios históricos e culturais do cliente."*
