
# TPPE - Gerenciadora de Estacionamento

Repositório destinado à refatoração de um trabalho de Orientação a Objetos (OO). O projeto original pode ser acessado em:  
🔗 [https://github.com/RafaelCLG0/Diagramas-UML-OO](https://github.com/RafaelCLG0/Diagramas-UML-OO)

---

## 📘 Cenário do Projeto

Você foi contratado por uma empresa que explora o gerenciamento de estacionamentos particulares (prédios comerciais, shoppings, etc.) e de instalações públicas (aeroportos, estádios, ginásios, etc.). 

De modo geral, o gerenciamento se dá pela liberação das catracas eletrônicas sempre que houver pelo menos uma vaga disponível. Cada estacionamento possui uma **ocupação máxima** que, ao ser atingida, impede novos acessos.

A empresa gerencia diversas **formas de acesso**, descritas a seguir:

### 🧾 Tipos de Acesso

- **Frações de 15 minutos**: a cada 15 minutos desde a entrada, contabiliza-se o valor da fração.
- **Horas cheias**: a cada 1 hora (4 frações), pode ser aplicado um desconto percentual.
- **Diária diurna**: acesso com duração superior a 9 horas tem valor fixo.
- **Diária noturna**: entrada após determinado horário e saída anterior a outro horário no dia seguinte, com percentual aplicado sobre a diária diurna.
- **Mensalista**: valor fixo por mês com acesso irrestrito durante o horário de funcionamento.
- **Evento**: valor fixo aplicado durante determinado período do dia.

Os valores variam conforme o estacionamento. Estabelecimentos com maior fluxo têm preços mais altos. A empresa contratante recebe uma **porcentagem** do valor cobrado por acesso.

Além disso, há parcerias com seguradoras de veículos, que oferecem **desconto global** sobre o valor total do acesso.

---

## 🧮 Tabela de Tarifas

| Estacionamento | Fração | Hora cheia | Diária diurna | Diária noturna                         |
|----------------|--------|------------|---------------|----------------------------------------|
| Estac. 1       | R$30   | 15%        | R$120         | 45% (19:00 às 08:00)                   |
| Estac. 2       | R$20   | 10%        | R$70          | 30% (21:00 às 07:00)                   |
| Estac. 3       | R$10   | 0%         | R$50          | 40% (20:00 às 08:00)                   |

| Estacionamento | Mensalista | Evento | Horário de Funcionamento | Capacidade | % Retorno |
|----------------|------------|--------|--------------------------|------------|-----------|
| Estac. 1       | R$600      | R$50   | 06:00 às 22:00           | 300        | 50%       |
| Estac. 2       | R$455      | R$60   | 24 horas                 | 120        | 60%       |
| Estac. 3       | R$350      | R$40   | 06:00 às 22:00           | 600        | 70%       |

---

## 📊 Exemplos de Acessos

### Estacionamento 1

| Placa | Entrada - Saída | Tipo      | Valor Cobrado | Valor Contratante |
|-------|------------------|-----------|----------------|--------------------|
| HI139 | 8:30 – 8:56      | -         | R$60,00        | R$30,00            |
| G49NG | -                | Mensalista| R$600,00       | R$300,00           |
| AC50M | 8:00 – 18:00     | Diária    | R$120,00       | R$60,00            |
| RM3A9 | -                | Noturno   | R$54,00        | R$27,00            |
| AM31J | -                | Evento    | R$50,00        | R$25,00            |

**Total repassado ao contratante:** R$442,00

### Estacionamento 2

| Placa | Entrada - Saída | Tipo      | Valor Cobrado | Valor Contratante |
|-------|------------------|-----------|----------------|--------------------|
| HI139 | 8:30 – 9:30      | Hora      | R$72,00        | R$43,20            |
| G49NG | 15:12 – 16:00    | Hora      | R$72,00        | R$43,20            |
| AC50M | 8:00 – 18:00     | Diária    | R$70,00        | R$42,00            |
| RM3A9 | 21:36 – 6:12     | Noturno   | R$21,00        | R$12,60            |
| AM31J | -                | Evento    | R$60,00        | R$36,00            |

**Total repassado ao contratante:** R$177,00



