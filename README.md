# TPPE - Gerenciadora de Estacionamento 🚗

Repositório destinado à refatoração de um projeto de Orientação a Objetos (OO) para a disciplina de Técnicas de Programação para Engenharia.  
🔗 Projeto original: [Diagramas UML - OO](https://github.com/RafaelCLG0/Diagramas-UML-OO)

---

## 📘 Cenário do Projeto

Você foi contratado por uma empresa que gerencia estacionamentos privados (shoppings, prédios comerciais) e públicos (aeroportos, ginásios, estádios). O acesso é liberado por catracas, respeitando a **capacidade máxima** de vagas em cada estacionamento.

O sistema deve calcular o valor a ser pago com base nas regras específicas de cada **tipo de acesso**.

---

## 🧾 Tipos de Acesso

- **Frações de 15 minutos** – tarifação fracionada.
- **Horas cheias** – cada hora pode ter desconto percentual.
- **Diária diurna** – acima de 9 horas, valor fixo.
- **Diária noturna** – entrada/saída em horários específicos com desconto sobre a diária.
- **Mensalista** – valor fixo por mês, acesso livre.
- **Evento** – valor fixo durante um período determinado.

Além disso, há **descontos de seguradoras** e **percentual de repasse** ao contratante.

---

## 🧮 Tabela de Tarifas

| Estacionamento | Fração | Hora cheia | Diária diurna | Diária noturna                         |
|----------------|--------|------------|---------------|----------------------------------------|
| Estac. 1       | R$30   | 15%        | R$120         | 45%                                    |
| Estac. 2       | R$20   | 10%        | R$70          | 30%                                    |
| Estac. 3       | R$10   | 0%         | R$50          | 40%                                    |

| Estacionamento | Mensalista | Evento | Horário Noturno       | Capacidade | % Repassado |
|----------------|------------|--------|---------------------|------------|-------------|
| Estac. 1       | R$600      | R$50   | 19:00 às 08:00      | 300        | 50%         |
| Estac. 2       | R$455      | R$60   | 21:00 às 07:00      | 120        | 60%         |
| Estac. 3       | R$350      | R$40   | 20:00 às 08:00      | 600        | 70%         |

---

## 📊 Exemplos de Acessos

### Estacionamento 1

| Placa | Entrada - Saída | Tipo        | Valor Cobrado | Valor Contratante |
|-------|------------------|-------------|----------------|--------------------|
| HI139 | 8:30 – 8:56      | -           | R$60,00        | R$30,00            |
| G49NG | -                | Mensalista  | R$600,00       | R$300,00           |
| AC50M | 8:00 – 18:00     | Diária      | R$120,00       | R$60,00            |
| RM3A9 | -                | Noturno     | R$54,00        | R$27,00            |
| AM31J | -                | Evento      | R$50,00        | R$25,00            |

**➡️ Total repassado ao contratante: R$442,00**

### Estacionamento 2

| Placa | Entrada - Saída | Tipo        | Valor Cobrado | Valor Contratante |
|-------|------------------|-------------|----------------|--------------------|
| HI139 | 8:30 – 9:30      | Hora        | R$72,00        | R$43,20            |
| G49NG | 15:12 – 16:00    | Hora        | R$72,00        | R$43,20            |
| AC50M | 8:00 – 18:00     | Diária      | R$70,00        | R$42,00            |
| RM3A9 | 21:36 – 6:12     | Noturno     | R$21,00        | R$12,60            |
| AM31J | -                | Evento      | R$60,00        | R$36,00            |

**➡️ Total repassado ao contratante: R$177,00**

---

## 🧠 Protótipo de Alta Fidelidade

O protótipo de alta fidelidade foi criado no Figma para representar as interfaces do sistema de forma visual e navegável, cobrindo todas as funcionalidades do sistema, como cadastro de estacionamento, registros de acesso, relatórios e painel inicial.

### 🔗 Acesse o protótipo:

👉 [Protótipo no Figma](https://www.figma.com/proto/CSsRpoXBR0BWWojN1ZrDn0/Prot%C3%B3tipo-de-Alta-FIdelidade?page-id=0%3A1&type=design&node-id=107-1118&viewport=29390%2C34193%2C3.02&scaling=min-zoom&starting-point-node-id=107%3A1118&show-proto-sidebar=1&mode=design)

<p align="center">
  <iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FCSsRpoXBR0BWWojN1ZrDn0%2FProt%25C3%25B3tipo-de-Alta-FIdelidade%3Fpage-id%3D0%253A1%26type%3Ddesign%26node-id%3D107-1118%26viewport%3D29390%252C34193%252C3.02%26scaling%3Dmin-zoom%26starting-point-node-id%3D107%253A1118%26show-proto-sidebar%3D1%26mode%3Ddesign" allowfullscreen></iframe>
</p>

---

## 🗂️ Estrutura de Pastas

```bash
.
├── docs/                   # Documentação geral do projeto
├── src/                    # Código-fonte da aplicação
│   ├── repository/         # Regras de negócio (operações de CRUD e lógica)
│   ├── router/             # Rotas/endpoints da API
│   ├── schemas/            # Esquemas de entrada/saída (Pydantic)
│   ├── main.py             # Arquivo principal da aplicação (FastAPI)
│   └── database.py         # Conexão e modelo do banco de dados
├── test/                   # Testes automatizados (unitários e de integração)
├── .env                    # Variáveis de ambiente (configuração do banco)
├── docker-compose.yml      # Orquestração dos containers
├── Dockerfile              # Container da aplicação
├── requirements.txt        # Dependências Python
└── README.md               # Documentação inicial do projeto

