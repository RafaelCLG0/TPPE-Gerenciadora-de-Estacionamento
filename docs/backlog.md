
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
    <td rowspan="2">Épico 1 - Cadastro de Entidades</td>
    <td>Feature 1 - Estacionamentos</td>
    <td><a href="../historia-de-usuario#us01">US01</a> - Cadastrar dados de estacionamento com valores e horários</td>
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
    <td><a href="../historia-de-usuario#us05">US05</a> - Aplicar cálculo específico para evento (informado pelo cliente)</td>
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
    <td rowspan="2">Épico 3 - Relatórios e Apuração</td>
    <td>Feature 5 - Relatórios Gerenciais</td>
    <td><a href="../historia-de-usuario#us10">US10</a> - Gerar relatório consolidado de acessos por estacionamento</td>
    <td>Alta</td>
  </tr>
  <tr>
    <td>Feature 5 - Relatórios Gerenciais</td>
    <td><a href="../historia-de-usuario#us11">US11</a> - Calcular o total de repasses por período</td>
    <td>Alta</td>
  </tr>
  <tr>
    <td rowspan="2">Épico 4 - Manutenção de Dados</td>
    <td>Feature 6 - Atualização e Exclusão</td>
    <td><a href="../historia-de-usuario#us12">US12</a> - Atualizar dados de estacionamento ou acesso</td>
    <td>Média</td>
  </tr>
  <tr>
    <td>Feature 6 - Atualização e Exclusão</td>
    <td><a href="../historia-de-usuario#us13">US13</a> - Remover cadastro de acesso ou estacionamento</td>
    <td>Média</td>
  </tr>
  <tr>
    <td>Épico 5 - Integração com Seguradoras</td>
    <td>Feature 7 - Descontos por Seguradora</td>
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

As funcionalidades foram agrupadas em:

- **Funcionalidades**: Recursos voltados para o uso cotidiano do cliente e do administrador.
- **Apuração & Gestão**: Regras de negócio e relatórios para apoio à tomada de decisão do administrador.

## Épicos e Perfis

---

### Épico 1 - Cadastro de Entidades

Permite estruturar os dados fundamentais de estacionamento e acessos.

<center>
Como administrador, desejo cadastrar estacionamentos e como cliente, desejo registrar meus acessos
</center>

---

### Épico 2 - Cálculos de Acesso

Engloba toda a lógica de inferência e cálculo dos tipos de acesso com seus respectivos valores.

<center>
Como sistema, desejo identificar e calcular corretamente o tipo de acesso para aplicar o valor devido ao cliente
</center>

---

### Épico 3 - Relatórios e Apuração

Geração de relatórios com os dados de acessos e repasses.

<center>
Como administrador, desejo acessar relatórios consolidados e calcular os valores de repasse ao contratante
</center>

---

### Épico 4 - Manutenção de Dados

Permite alterações, atualizações e exclusões nos registros.

<center>
Como administrador, desejo manter os cadastros sempre atualizados e consistentes
</center>

---

### Épico 5 - Integração com Seguradoras

Aplica automaticamente descontos definidos por parcerias com seguradoras.

<center>
Como cliente segurado, desejo que o sistema aplique automaticamente meu desconto no valor do acesso
</center>
