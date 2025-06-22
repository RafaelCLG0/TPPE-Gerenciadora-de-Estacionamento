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
|----------------|------------|--------|------------------------|------------|-------------|
| Estac. 1       | R$600      | R$50   | 19:00 às 08:00         | 300        | 50%         |
| Estac. 2       | R$455      | R$60   | 21:00 às 07:00         | 120        | 60%         |
| Estac. 3       | R$350      | R$40   | 20:00 às 08:00         | 600        | 70%         |

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

➡️ **Total repassado ao contratante: R$442,00**

### Estacionamento 2

| Placa | Entrada - Saída | Tipo        | Valor Cobrado | Valor Contratante |
|-------|------------------|-------------|----------------|--------------------|
| HI139 | 8:30 – 9:30      | Hora        | R$72,00        | R$43,20            |
| G49NG | 15:12 – 16:00    | Hora        | R$72,00        | R$43,20            |
| AC50M | 8:00 – 18:00     | Diária      | R$70,00        | R$42,00            |
| RM3A9 | 21:36 – 6:12     | Noturno     | R$21,00        | R$12,60            |
| AM31J | -                | Evento      | R$60,00        | R$36,00            |

➡️ **Total repassado ao contratante: R$177,00**

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
```

---

## 🐳 Rodando com Docker

A aplicação pode ser executada facilmente com Docker. A única dependência necessária é o Docker (e o Docker Compose).

### ▶️ Subindo a aplicação

```bash
docker compose up --build
```

### ℹ️ Observações importantes

- Em algumas máquinas, é necessário adicionar `sudo` antes do comando:
  ```bash
  sudo docker compose up --build
  ```

- Se estiver utilizando uma **versão mais antiga** do Docker Compose (com hífen), use:
  ```bash
  docker-compose up --build
  ```

---

## 🧪 Testes e Análise de Código

### ✅ Executando os testes com Pytest

Você pode executar os testes automatizados diretamente no container da aplicação:

```bash
docker-compose exec app pytest
```

📌 Antes, certifique-se de que a API está em execução:

```bash
docker-compose up -d --build
```

---

### 🔍 Análise Estática de Código com Pylint

Para realizar a análise de qualidade de código com `pylint`, ative o ambiente virtual (caso esteja rodando localmente) e execute:

```bash
PYTHONPATH=$(pwd) pylint src/
```

---

## 📄 Documentação da API

Acesse a interface interativa da API via Swagger no navegador:

🔗 **http://localhost:8000/docs**

---

## 🛠️ Comandos Úteis

| Finalidade                     | Comando                                              |
|-------------------------------|------------------------------------------------------|
| Subir os containers (build)   | `docker compose up --build`                         |
| Subir containers em background| `docker-compose up -d --build`                      |
| Derrubar containers + volumes | `docker compose down -v`                            |
| Executar testes Pytest        | `docker-compose exec app pytest`                    |
| Rodar Pylint localmente       | `PYTHONPATH=$(pwd) pylint src/`                     |
