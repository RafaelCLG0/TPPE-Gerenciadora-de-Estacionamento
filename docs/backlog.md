# 📋 Backlog

## Introdução

Este backlog foi elaborado com base nas regras de negócio e necessidades da empresa contratante responsável pelo gerenciamento de estacionamentos. A estrutura foi pensada de forma a garantir **clareza**, **priorização** e **rastreabilidade** das funcionalidades previstas no sistema.

---

## 📌 Acompanhamento no Trello

O progresso detalhado das histórias de utilizador, tarefas e sprints pode ser acompanhado através do nosso quadro no Trello.

🔗 **Link para o Quadro**: [Aceder ao Backlog no Trello](https://trello.com/invite/b/685c6ad89be57b96ea138d1e/ATTI4331f0c272579c2191c716078a3ff13e526C9E6F/backlog)

---

## 🧭 Metodologia

O backlog foi dividido em **Épicos**, **Features** e **Histórias de Usuário**, com cada história associada a uma **priorização** definida com base no impacto da funcionalidade para o negócio.

---

### 📊 Tabela 1 - Product Backlog Elaborado com o Product Owner

| Épico                        | Feature                        | História de Usuário                                                                 | Priorização |
|-----------------------------|--------------------------------|--------------------------------------------------------------------------------------|-------------|
| **Épico 1 - Cadastro de Entidades** | Feature 1 - Estacionamentos     | US01 - Cadastrar dados de estacionamento com valores e horários                     | Alta        |
|                             | Feature 2 - Acessos            | US03 - Cadastrar acessos de veículos (placa, entrada, saída)                        | Alta        |
| **Épico 2 - Cálculos de Acesso**    | Feature 3 - Inferência           | US04 - Inferir tipo de acesso com base na duração e horários                        | Alta        |
|                             |                                | US05 - Aplicar cálculo específico para evento (informado pelo cliente)              | Média       |
|                             | Feature 4 - Valor              | US06 - Calcular valor do acesso (fração, hora cheia, diária, noturno, etc.)         | Alta        |
|                             |                                | US07 - Calcular valor de repasse ao contratante                                     | Alta        |
| **Épico 3 - Relatórios e Apuração** | Feature 5 - Relatórios Gerenciais | US10 - Gerar relatório consolidado de acessos por estacionamento                   | Alta        |
|                             |                                | US11 - Calcular o total de repasses por período                                     | Alta        |
| **Épico 4 - Manutenção de Dados**  | Feature 6 - Atualização e Exclusão | US12 - Atualizar dados de estacionamento ou acesso                                 | Média       |
|                             |                                | US13 - Remover cadastro de acesso ou estacionamento                                 | Média       |
| **Épico 5 - Integração com Seguradoras** | Feature 7 - Descontos por Seguradora | US14 - Aplicar desconto global da seguradora sobre o valor do acesso          | Média       |

---

📎 **Fonte**: Rafael Ferreira

---

## 🎯 Temas

As funcionalidades foram agrupadas em dois grandes temas:

- **Funcionalidades**: Recursos voltados para o uso cotidiano do cliente e do administrador.  
- **Apuração & Gestão**: Regras de negócio e relatórios para apoio à tomada de decisão do administrador.

---

## 🧱 Épicos e Perfis

### Épico 1 - Cadastro de Entidades

Permite estruturar os dados fundamentais de estacionamento e acessos.

> 💬 _"Como administrador, desejo cadastrar estacionamentos e como cliente, desejo registrar meus acessos"_

---

### Épico 2 - Cálculos de Acesso

Engloba toda a lógica de inferência e cálculo dos tipos de acesso com seus respectivos valores.

> 💬 _"Como sistema, desejo identificar e calcular corretamente o tipo de acesso para aplicar o valor devido ao cliente"_

---

### Épico 3 - Relatórios e Apuração

Geração de relatórios com os dados de acessos e repasses.

> 💬 _"Como administrador, desejo acessar relatórios consolidados e calcular os valores de repasse ao contratante"_

---

### Épico 4 - Manutenção de Dados

Permite alterações, atualizações e exclusões nos registros.

> 💬 _"Como administrador, desejo manter os cadastros sempre atualizados e consistentes"_

---

### Épico 5 - Integração com Seguradoras

Aplica automaticamente descontos definidos por parcerias com seguradoras.

> 💬 _"Como cliente segurado, desejo que o sistema aplique automaticamente meu desconto no valor do acesso"_
