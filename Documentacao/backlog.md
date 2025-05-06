# Backlog

## Introdução

Este backlog foi elaborado com base nas regras de negócio e necessidades da empresa contratante responsável pelo gerenciamento de estacionamentos. A estrutura foi pensada de forma a garantir clareza, priorização e rastreabilidade das funcionalidades previstas no sistema.

## Metodologia

O backlog foi dividido em épicos, features e histórias de usuário com cada história de usuário associada a uma priorização definida com base no impacto da funcionalidade para o negócio.

<center>

*Tabela 1* - Product Backlog Elaborado com o Product Owner.

<table>
<thead>
  <tr>
    <th>Épico</th>
    <th>Feature</th>
    <th>História de usuário</th>
    <th>Priorização</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="3">Épico 1 - Cadastro de Entidades</td>
    <td rowspan="2">Feature 1 - Estacionamentos</td>
    <td><a href="../historia-de-usuario#us01">US01</a> - Cadastrar dados de estacionamento com valores e horários</td>
    <td>Alta</td>
  </tr>
  <tr>
    <td><a href="../historia-de-usuario#us02">US02</a> - Validar campos obrigatórios e lançar exceções personalizadas</td>
    <td>Alta</td>
  </tr>
  <tr>
    <td>Feature 2 - Acessos</td>
    <td><a href="../historia-de-usuario#us03">US03</a> - Cadastrar acessos de veículos (placa, entrada, saída)</td>
    <td>Alta</td>
  </tr>
  <tr>
    <td rowspan="4">Épico 2 - Cálculos de Acesso</td>
    <td rowspan="2">Feature 3 - Inferência</td>
    <td><a href="../historia-de-usuario#us04">US04</a> - Inferir tipo de acesso com base na duração e horários</td>
    <td>Alta</td>
  </tr>
  <tr>
    <td><a href="../historia-de-usuario#us05">US05</a> - Aplicar cálculo específico para evento (informado pelo usuário)</td>
    <td>Média</td>
  </tr>
  <tr>
    <td rowspan="2">Feature 4 - Valor</td>
    <td><a href="../historia-de-usuario#us06">US06</a> - Calcular valor do acesso (fração, hora cheia, diária, noturno, etc.)</td>
    <td>Alta</td>
  </tr>
  <tr>
    <td><a href="../historia-de-usuario#us07">US07</a> - Calcular valor de repasse ao contratante</td>
    <td>Alta</td>
  </tr>
  <tr>
    <td rowspan="2">Épico 3 - Validação e Segurança</td>
    <td>Feature 5 - Validações</td>
    <td><a href="../historia-de-usuario#us08">US08</a> - Lançar exceções para campos em branco ou valores negativos</td>
    <td>Alta</td>
  </tr>
  <tr>
    <td>Feature 6 - Utilitários</td>
    <td><a href="../historia-de-usuario#us09">US09</a> - Converter horário para minutos para cálculo de tempo</td>
    <td>Média</td>
  </tr>
  <tr>
    <td rowspan="2">Épico 4 - Relatórios e Apuração</td>
    <td>Feature 7 - Relatórios Gerenciais</td>
    <td><a href="../historia-de-usuario#us10">US10</a> - Gerar relatório consolidado de acessos por estacionamento</td>
    <td>Alta</td>
  </tr>
  <tr>
    <td>Feature 7 - Relatórios Gerenciais</td>
    <td><a href="../historia-de-usuario#us11">US11</a> - Calcular o total de repasses por período</td>
    <td>Alta</td>
  </tr>
  <tr>
    <td rowspan="2">Épico 5 - Manutenção de Dados</td>
    <td>Feature 8 - Atualização e Exclusão</td>
    <td><a href="../historia-de-usuario#us12">US12</a> - Atualizar dados de estacionamento ou acesso</td>
    <td>Média</td>
  </tr>
  <tr>
    <td>Feature 8 - Atualização e Exclusão</td>
    <td><a href="../historia-de-usuario#us13">US13</a> - Remover cadastro de acesso ou estacionamento</td>
    <td>Média</td>
  </tr>
  <tr>
    <td>Épico 6 - Integração com Seguradoras</td>
    <td>Feature 9 - Descontos por Seguradora</td>
    <td><a href="../historia-de-usuario#us14">US14</a> - Aplicar desconto global da seguradora sobre o valor do acesso</td>
    <td>Média</td>
  </tr>
</tbody>
</table>

</center>
<center>

Fonte: [Rafael Ferreira](https://github.com/RafaelCLG0)

</center>

## Temas

Analisando as histórias de usuário, foi possível organizá-las inicialmente em dois grandes temas.

- **Funcionalidades**: Agrupa funcionalidades que o sistema precisa oferecer para que o usuário consiga realizar com sucesso suas tarefas.
- **Cálculo & Segurança**: Engloba as funções de validação, regras de negócio e consistência nos acessos.

## Épicos

Após a definição dos temas, eles são "quebrados" em épicos de modo a diminuir ainda mais a abstração das atividades que deverão ser realizadas no projeto.

## Features

Definido um épico, são geradas *features*, que representam funcionalidades de alto nível no sistema.

### Histórias de Usuário

As histórias de usuário detalham as *features* e são descritas como:  
*"Eu, como [perfil], desejo [funcionalidade] para [benefício esperado]"*

---

### Épico 1 - Cadastro de Entidades
Permite estruturar os dados fundamentais de estacionamento e acessos.

<center>
*"Como operador, desejo cadastrar estacionamentos e acessos com dados obrigatórios validados"*
</center>

---

### Épico 2 - Cálculos de Acesso
Engloba toda a lógica de inferência e cálculo dos tipos de acesso com seus respectivos valores.

<center>
*"Como sistema, desejo identificar e calcular corretamente o tipo de acesso para aplicar o valor correto"*
</center>

---

### Épico 3 - Validação e Segurança
Assegura a consistência dos dados e prevenção de erros no processo de cadastro e cálculo.

<center>
*"Como desenvolvedor, desejo garantir a integridade dos dados e regras de negócio com exceções personalizadas"*
</center>

### Épico 4 - Relatórios e Apuração

Este épico contempla a funcionalidade de consolidação e geração de relatórios com os dados de acessos e repasses.

<center>
*"Como administrador, desejo acessar relatórios detalhados com valores e repasses dos estacionamentos"*
</center>

---

#### Feature 7 - Relatórios Gerenciais

- <a href="../historia-de-usuario#us10">US10</a> - Gerar relatório consolidado de acessos por estacionamento  
  **Priorização:** Alta  
  _"Como administrador, desejo ver um relatório de todos os acessos realizados para visualizar os fluxos de entrada e saída."_

- <a href="../historia-de-usuario#us11">US11</a> - Calcular o total de repasses por período  
  **Priorização:** Alta  
  _"Como sistema, desejo calcular o valor total a ser repassado ao contratante de acordo com os percentuais acordados."_

---

### Épico 5 - Manutenção de Dados

Envolve as operações de atualização e remoção de informações dos cadastros realizados no sistema.

<center>
*"Como operador, desejo manipular os cadastros, atualizando dados, editando informações ou excluindo. "*
</center>

---

#### Feature 8 - Atualização e Exclusão

- <a href="../historia-de-usuario#us12">US12</a> - Atualizar dados de estacionamento ou acesso  
  **Priorização:** Média  
  _"Como operador, desejo editar informações de um acesso ou estacionamento para corrigir dados inconsistentes."_

- <a href="../historia-de-usuario#us13">US13</a> - Remover cadastro de acesso ou estacionamento  
  **Priorização:** Média  
  _"Como operador, desejo excluir registros de acesso ou estacionamento que não são mais utilizados."_

---

### Épico 6 - Integração com Seguradoras

Descreve a funcionalidade para aplicar descontos em parceria com seguradoras de veículos.

<center>
*"Como cliente segurado, desejo que meu desconto seja aplicado automaticamente no valor total"*
</center>

---

#### Feature 9 - Descontos por Seguradora

- <a href="../historia-de-usuario#us14">US14</a> - Aplicar desconto global da seguradora sobre o valor do acesso  
  **Priorização:** Média  
  _"Como sistema, desejo aplicar o desconto da seguradora nos valores de acesso sem intervenção manual."_


---

### Épico 4 - Relatórios e Apuração

Este épico contempla a funcionalidade de consolidação e geração de relatórios com os dados de acessos e repasses.

<center>
*"Como administrador, desejo acessar relatórios detalhados com valores e repasses dos estacionamentos"*
</center>

---

#### Feature 7 - Relatórios Gerenciais

- <a href="../historia-de-usuario#us10">US10</a> - Gerar relatório consolidado de acessos por estacionamento  
  **Priorização:** Alta  
  _"Como administrador, desejo ver um relatório de todos os acessos realizados para visualizar os fluxos de entrada e saída."_

- <a href="../historia-de-usuario#us11">US11</a> - Calcular o total de repasses por período  
  **Priorização:** Alta  
  _"Como sistema, desejo calcular o valor total a ser repassado ao contratante de acordo com os percentuais acordados."_

---

### Épico 5 - Manutenção de Dados

Envolve as operações de atualização e remoção de informações dos cadastros realizados no sistema.

<center>
*"Como operador, desejo manter os cadastros atualizados com segurança e controle de erros"*
</center>

---

#### Feature 8 - Atualização e Exclusão

- <a href="../historia-de-usuario#us12">US12</a> - Atualizar dados de estacionamento ou acesso  
  **Priorização:** Média  
  _"Como operador, desejo editar informações de um acesso ou estacionamento para corrigir dados inconsistentes."_

- <a href="../historia-de-usuario#us13">US13</a> - Remover cadastro de acesso ou estacionamento  
  **Priorização:** Média  
  _"Como operador, desejo excluir registros de acesso ou estacionamento que não são mais utilizados."_

---

### Épico 6 - Integração com Seguradoras

Descreve a funcionalidade para aplicar descontos em parceria com seguradoras de veículos.

<center>
*"Como cliente segurado, desejo que meu desconto seja aplicado automaticamente no valor total"*
</center>

---

#### Feature 9 - Descontos por Seguradora

- <a href="../historia-de-usuario#us14">US14</a> - Aplicar desconto global da seguradora sobre o valor do acesso  
  **Priorização:** Média  
  _"Como sistema, desejo aplicar o desconto da seguradora nos valores de acesso sem intervenção manual."_