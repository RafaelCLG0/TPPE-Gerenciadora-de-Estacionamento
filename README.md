# TPPE - Gerenciadora de Estacionamento 🚗

Repositório destinado à refatoração e expansão de um projeto de Orientação a Objetos (OO) para a disciplina de Técnicas de Programação para Engenharia, agora como uma aplicação Full-Stack completa.

🔗 **Projeto original**: Diagramas UML - OO

---

## 🚀 Acesso Online

A aplicação está hospedada e pode ser acedida através dos seguintes links:

- **Front-end (Aplicação Web)**: [gerenciadoradeestacionamento.netlify.app](https://gerenciadoradeestacionamento.netlify.app)  
- **Back-end (Documentação da API)**: [tppe-gerenciadora-de-estacionamento.onrender.com/docs](https://tppe-gerenciadora-de-estacionamento.onrender.com/docs)

---

## 🏗️ Arquitetura da Solução

Este projeto foi desenvolvido seguindo uma arquitetura de aplicação web moderna, com uma clara separação entre o front-end e o back-end.

- **Front-end**: SPA desenvolvida com HTML, CSS e JavaScript puro. A estilização foi feita com Tailwind CSS.  
  - **Hospedagem**: Netlify.

- **Back-end**: API RESTful robusta com Python e FastAPI, containerizada com Docker.  
  - **Hospedagem**: Render (Web Service).

- **Banco de Dados**: PostgreSQL relacional, com persistência de todos os dados da aplicação.  
  - **Hospedagem**: Render (Database Service).

---

## 📘 Cenário do Projeto

Você foi contratado por uma empresa que gerencia estacionamentos privados (shoppings, prédios comerciais) e públicos (aeroportos, ginásios, estádios). O acesso é liberado por catracas, respeitando a capacidade máxima de vagas em cada estacionamento.

O sistema deve calcular o valor a ser pago com base nas regras específicas de cada tipo de acesso.

---

## 🧾 Tipos de Acesso

- **Frações de 15 minutos** – tarifação fracionada.  
- **Horas cheias** – cada hora pode ter desconto percentual.  
- **Diária diurna** – acima de 9 horas, valor fixo.  
- **Diária noturna** – entrada/saída em horários específicos com desconto sobre a diária.  
- **Mensalista** – valor fixo por mês, acesso livre.  
- **Evento** – valor fixo durante um período determinado.

---

## 🗂️ Estrutura de Pastas

```bash
.
├── estacionamento-frontend/        # Código-fonte do Front-end (HTML, CSS, JS)
├── src/                            # Código-fonte do Back-end (API FastAPI)
│   ├── acesso/
│   ├── estacionamento/
│   ├── relatorios/
│   ├── usuario/
│   ├── utils/
│   ├── main.py                     # Ponto de entrada da API
│   └── database.py                 # Configuração do banco de dados
├── tests/                          # Testes automatizados
│   └── test_e2e_selenium.py        # Testes de ponta a ponta com Selenium
├── docs/                           # Documentação geral do projeto
├── .env                            # Variáveis de ambiente (exemplo)
├── docker-compose.yml              # Orquestração dos containers locais
├── Dockerfile                      # Container da aplicação back-end
├── requirements.txt                # Dependências Python
└── README.md                       # Este ficheiro
```

---

## 🐳 Rodando o Projeto Completo (Localmente)

Para executar a aplicação completa no seu ambiente local, você precisará ter o **Docker** e um editor como **VS Code** com a extensão **Live Server**.

### ▶️ Passo 1: Subir o Back-end e o Banco de Dados

No terminal, na raiz do projeto:

```bash
docker-compose up --build
```

Aguarde até ver a mensagem ✅ *Banco de dados conectado e tabelas criadas*.

### ▶️ Passo 2: Iniciar o Front-end

1. Abra a pasta do projeto no VS Code  
2. Navegue até o arquivo: `estacionamento-frontend/index.html`  
3. Clique com o botão direito e selecione: **"Open with Live Server"**

O navegador abrirá automaticamente com a aplicação conectada à API local.

---

## 🧪 Testes e Análise de Código

### ✅ Testes do Back-end (Pytest)

Validação da lógica da API e da persistência dos dados.

```bash
docker-compose up -d
docker-compose exec app pytest
```

### ✅ Testes de Ponta a Ponta (Selenium)

Simula um usuário real interagindo com a aplicação hospedada.

1. Ative o ambiente virtual Python:

```bash
source venv/bin/activate
```

2. Execute os testes:

```bash
pytest tests/test_e2e_selenium.py -v -s
```

Uma janela do Chrome abrirá automaticamente com o fluxo de testes.

### 🔍 Análise Estática de Código (Pylint)

Para verificar a qualidade do código:

```bash
PYTHONPATH=. pylint src/
```

---

## 📄 Documentação da API (Swagger)

Acesse a interface interativa da API para explorar todos os endpoints disponíveis:

- **Localmente**: [http://localhost:8000/docs](http://localhost:8000/docs)  
