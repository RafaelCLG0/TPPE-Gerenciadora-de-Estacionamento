// =================================================================
// CONFIGURATION
// =================================================================
const API_BASE_URL = 'https://tppe-gerenciadora-de-estacionamento.onrender.com';

// =================================================================
// STATE MANAGEMENT
// =================================================================
let currentDeleteInfo = {
    id: null,
    type: null
};
const lastActions = [];

// =================================================================
// UTILITY FUNCTIONS
// =================================================================
const formatCurrency = (value) => new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value || 0);
const formatDate = (dateStr) => dateStr ? new Date(dateStr).toLocaleDateString('pt-BR', { timeZone: 'UTC' }) : '';
const formatTime = (timeStr) => timeStr ? timeStr.substring(0, 5) : '';
const formatDateTime = (dateStr) => dateStr ? new Date(dateStr).toLocaleString('pt-BR') : '';

function addLastAction(icon, title, description) {
    lastActions.unshift({ icon, title, description, time: new Date() });
    if (lastActions.length > 4) {
        lastActions.pop();
    }
    renderLastActions();
}

// =================================================================
// API CALLS
// =================================================================
async function fetchAPI(endpoint, options = {}) {
    try {
        const url = `${API_BASE_URL}${endpoint}`;
        const response = await fetch(url, options);
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({ detail: `HTTP error! status: ${response.status}` }));
            throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
        }
        if (response.status === 204) return null;
        return response.json();
    } catch (error) {
        console.error('API Error:', error);
        alert(`Erro na comunicação com a API: ${error.message}`);
        return null;
    }
}

// =================================================================
// RENDER FUNCTIONS
// =================================================================
function renderEstacionamentosTable(estacionamentos) {
    const tableBody = document.getElementById('estacionamentos-table-body');
    tableBody.innerHTML = '';
    if (!estacionamentos || estacionamentos.length === 0) {
        tableBody.innerHTML = '<tr><td colspan="5" class="p-4 text-center text-gray-500">Nenhum estacionamento encontrado.</td></tr>';
        return;
    }
    estacionamentos.forEach(est => {
        const row = document.createElement('tr');
        row.className = 'border-b hover:bg-gray-50';
        row.innerHTML = `
            <td class="p-4">${est.nome}</td>
            <td class="p-4">${est.cnpj}</td>
            <td class="p-4">${est.percentualRepasse}%</td>
            <td class="p-4">${est.capacidade}</td>
            <td class="p-4 space-x-2">
                <button onclick="handleEditEstacionamento(${est.id})" class="px-3 py-1 text-sm font-semibold text-white bg-blue-500 rounded-md hover:bg-blue-600">Visualizar</button>
                <button onclick="handleDelete('estacionamento', ${est.id})" class="px-3 py-1 text-sm font-semibold text-white bg-red-500 rounded-md hover:bg-red-600">Deletar</button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

function renderAcessosTable(acessos) {
    const tableBody = document.getElementById('acessos-table-body');
    tableBody.innerHTML = '';
    if (!acessos || acessos.length === 0) {
        tableBody.innerHTML = '<tr><td colspan="5" class="p-4 text-center text-gray-500">Nenhum acesso encontrado.</td></tr>';
        return;
    }
    acessos.forEach(acesso => {
        const row = document.createElement('tr');
        row.className = 'border-b hover:bg-gray-50';
        row.innerHTML = `
            <td class="p-4">${acesso.placa}</td>
            <td class="p-4">${formatDate(acesso.data_entrada)} ${formatTime(acesso.hora_entrada)}</td>
            <td class="p-4">${formatDate(acesso.data_saida)} ${formatTime(acesso.hora_saida)}</td>
            <td class="p-4">${formatCurrency(acesso.valor_pago)}</td>
            <td class="p-4 space-x-2">
                <button onclick="handleEditAcesso(${acesso.id})" class="px-3 py-1 text-sm font-semibold text-white bg-blue-500 rounded-md hover:bg-blue-600">Visualizar</button>
                <button onclick="handleDelete('acesso', ${acesso.id})" class="px-3 py-1 text-sm font-semibold text-white bg-red-500 rounded-md hover:bg-red-600">Deletar</button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

async function populateEstacionamentoDropdowns() {
    const estacionamentos = await fetchAPI('/estacionamentos/');
    const selectFilter = document.getElementById('acesso-estacionamento-filter');
    const selectForm = document.getElementById('acesso-estacionamento-id');
    
    selectFilter.innerHTML = '<option value="">Todos os Estacionamentos</option>';
    selectForm.innerHTML = '<option value="">Selecione um Estacionamento</option>';

    if(estacionamentos) {
        estacionamentos.forEach(est => {
            selectFilter.innerHTML += `<option value="${est.id}">${est.nome}</option>`;
            selectForm.innerHTML += `<option value="${est.id}">${est.nome}</option>`;
        });
    }
}

function renderLastActions() {
    const container = document.getElementById('home-ultimas-acoes');
    container.innerHTML = '';
    if (lastActions.length === 0) {
        container.innerHTML = '<p class="text-gray-500">Nenhuma ação recente.</p>';
        return;
    }
    lastActions.forEach(action => {
        const actionEl = document.createElement('div');
        actionEl.className = 'flex items-start';
        actionEl.innerHTML = `
            <i class="p-2 mt-1 text-blue-600 bg-blue-100 rounded-full ${action.icon}"></i>
            <div class="ml-4">
                <p class="font-semibold text-gray-800">${action.title}</p>
                <p class="text-sm text-gray-600">${action.description}</p>
                <p class="text-xs text-gray-400">${formatDateTime(action.time)}</p>
            </div>
        `;
        container.appendChild(actionEl);
    });
}

// =================================================================
// PAGE LOADERS
// =================================================================
async function loadHomePage() {
    const estacionamentos = await fetchAPI('/estacionamentos/');
    const acessos = await fetchAPI('/acessos/');
    document.getElementById('home-estacionamentos-ativos').textContent = estacionamentos?.length || 0;
    document.getElementById('home-acessos-total').textContent = acessos?.length || 0;
    renderLastActions();
}

async function loadEstacionamentosPage() {
    const estacionamentos = await fetchAPI('/estacionamentos/');
    renderEstacionamentosTable(estacionamentos || []);
}

async function loadAcessosPage(filterId = '') {
    const acessos = await fetchAPI('/acessos/');
    let acessosFiltrados = acessos || [];
    if (filterId) {
        acessosFiltrados = acessosFiltrados.filter(a => a.estacionamento_id == filterId);
    }
    renderAcessosTable(acessosFiltrados);
}

// =================================================================
// MODAL & FORM HANDLING
// =================================================================
window.openModal = (modalId) => {
    const modal = document.getElementById(modalId);
    modal.classList.remove('hidden');
};

window.closeModal = (modalId) => {
    const modal = document.getElementById(modalId);
    modal.classList.add('hidden');
    const estForm = document.getElementById('estacionamento-form');
    if (estForm) {
        estForm.reset();
        document.getElementById('estacionamento-id').value = '';
    }
    const accForm = document.getElementById('acesso-form');
    if(accForm) {
        accForm.reset();
        document.getElementById('acesso-id').value = '';
    }
};

document.getElementById('estacionamento-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const id = document.getElementById('estacionamento-id').value;
    const data = {
        nome: document.getElementById('estacionamento-nome').value,
        cnpj: document.getElementById('estacionamento-cnpj').value,
        valorFracao: parseFloat(document.getElementById('estacionamento-valorFracao').value),
        valorHoraCheia: parseFloat(document.getElementById('estacionamento-valorHoraCheia').value),
        valorDiaria: parseFloat(document.getElementById('estacionamento-valorDiaria').value),
        valorMensalista: parseFloat(document.getElementById('estacionamento-valorMensalista').value),
        valorEvento: parseFloat(document.getElementById('estacionamento-valorEvento').value),
        valorNoturno: parseFloat(document.getElementById('estacionamento-valorNoturno').value),
        horarioNoturnoInicio: document.getElementById('estacionamento-horarioNoturnoInicio').value,
        horarioNoturnoFim: document.getElementById('estacionamento-horarioNoturnoFim').value,
        capacidade: parseInt(document.getElementById('estacionamento-capacidade').value),
        percentualRepasse: parseFloat(document.getElementById('estacionamento-percentualRepasse').value),
    };

    const method = id ? 'PUT' : 'POST';
    const endpoint = id ? `/estacionamentos/${id}` : '/estacionamentos/';
    const result = await fetchAPI(endpoint, {
        method: method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    });

    if (result) {
        closeModal('estacionamento-modal');
        loadEstacionamentosPage();
        // CORREÇÃO: Atualiza a lista de estacionamentos nos formulários.
        populateEstacionamentoDropdowns();
        const action = id ? 'atualizado' : 'criado';
        addLastAction('fa-solid fa-car-side', `Estacionamento ${action}`, `Estacionamento ${data.nome} ${action}.`);
    }
});

window.handleEditEstacionamento = async (id) => {
    const estacionamentos = await fetchAPI(`/estacionamentos/`); 
    const data = estacionamentos.find(e => e.id === id);
    if (data) {
        document.getElementById('estacionamento-modal-title').textContent = 'Visualizar/Editar Estacionamento';
        document.getElementById('estacionamento-id').value = data.id;
        document.getElementById('estacionamento-nome').value = data.nome;
        document.getElementById('estacionamento-cnpj').value = data.cnpj;
        document.getElementById('estacionamento-valorFracao').value = data.valorFracao;
        document.getElementById('estacionamento-valorHoraCheia').value = data.valorHoraCheia;
        document.getElementById('estacionamento-valorDiaria').value = data.valorDiaria;
        document.getElementById('estacionamento-valorMensalista').value = data.valorMensalista;
        document.getElementById('estacionamento-valorEvento').value = data.valorEvento;
        document.getElementById('estacionamento-valorNoturno').value = data.valorNoturno;
        document.getElementById('estacionamento-horarioNoturnoInicio').value = data.horarioNoturnoInicio;
        document.getElementById('estacionamento-horarioNoturnoFim').value = data.horarioNoturnoFim;
        document.getElementById('estacionamento-capacidade').value = data.capacidade;
        document.getElementById('estacionamento-percentualRepasse').value = data.percentualRepasse;
        openModal('estacionamento-modal');
    }
};

document.getElementById('acesso-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const id = document.getElementById('acesso-id').value;
    const data = {
        placa: document.getElementById('acesso-placa').value,
        data_entrada: document.getElementById('acesso-data-entrada').value,
        hora_entrada: document.getElementById('acesso-hora-entrada').value,
        data_saida: document.getElementById('acesso-data-saida').value,
        hora_saida: document.getElementById('acesso-hora-saida').value,
        evento: document.getElementById('acesso-evento').value === 'true',
        mensalista: document.getElementById('acesso-mensalista').value === 'true',
        estacionamento_id: parseInt(document.getElementById('acesso-estacionamento-id').value),
    };

    const method = id ? 'PUT' : 'POST';
    const endpoint = id ? `/acessos/${id}` : '/acessos/';
    const result = await fetchAPI(endpoint, {
        method: method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    });

    if (result) {
        closeModal('acesso-modal');
        loadAcessosPage(document.getElementById('acesso-estacionamento-filter').value);
        const action = id ? 'atualizado' : 'registrado';
        addLastAction('fa-solid fa-right-to-bracket', `Acesso ${action}`, `Acesso da placa ${data.placa} ${action}.`);
    }
});

window.handleEditAcesso = async (id) => {
    const acessos = await fetchAPI(`/acessos/`);
    const data = acessos.find(a => a.id === id);
    if (data) {
        document.getElementById('acesso-modal-title').textContent = 'Visualizar/Editar Acesso';
        document.getElementById('acesso-id').value = data.id;
        document.getElementById('acesso-placa').value = data.placa;
        document.getElementById('acesso-estacionamento-id').value = data.estacionamento_id;
        document.getElementById('acesso-data-entrada').value = data.data_entrada;
        document.getElementById('acesso-hora-entrada').value = data.hora_entrada;
        document.getElementById('acesso-data-saida').value = data.data_saida;
        document.getElementById('acesso-hora-saida').value = data.hora_saida;
        document.getElementById('acesso-evento').value = data.evento.toString();
        document.getElementById('acesso-mensalista').value = data.mensalista.toString();
        openModal('acesso-modal');
    }
};

document.getElementById('relatorio-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const inicio = new Date(document.getElementById('relatorio-data-inicio').value).toISOString();
    const fim = new Date(document.getElementById('relatorio-data-fim').value).toISOString();
    
    const results = await fetchAPI(`/relatorios/repasses/?inicio=${inicio}&fim=${fim}`);
    
    if (results && results.length > 0) {
        const totalBruto = results.reduce((sum, r) => sum + r.total_bruto, 0);
        const totalRepasse = results.reduce((sum, r) => sum + r.total_repasse, 0);
        const totalLiquido = results.reduce((sum, r) => sum + r.lucro_liquido, 0);
        const percentual = totalBruto > 0 ? (totalRepasse / totalBruto) * 100 : 0;

        document.getElementById('relatorio-valor-total').textContent = formatCurrency(totalBruto);
        document.getElementById('relatorio-percentual').textContent = `-${percentual.toFixed(0)}%`;
        document.getElementById('relatorio-valor-contratante').textContent = formatCurrency(totalLiquido);
        document.getElementById('relatorio-resultado').classList.remove('hidden');
        
        addLastAction('fa-solid fa-chart-line', 'Relatório Gerado', `Relatório financeiro gerado com sucesso.`);
    } else {
        alert('Nenhum dado encontrado para o período selecionado.');
        document.getElementById('relatorio-resultado').classList.add('hidden');
    }
});

window.handleDelete = (type, id) => {
    currentDeleteInfo = { type, id };
    const modalText = document.getElementById('delete-modal-text');
    modalText.textContent = `Você realmente deseja deletar este ${type}? Esta ação não pode ser desfeita.`;
    openModal('delete-modal');
};

document.getElementById('delete-confirm-button').addEventListener('click', async () => {
    const { type, id } = currentDeleteInfo;
    if (!type || !id) return;

    let endpoint = '';
    if (type === 'estacionamento') endpoint = `/estacionamentos/${id}`;
    if (type === 'acesso') endpoint = `/acessos/${id}`;

    await fetchAPI(endpoint, { method: 'DELETE' });
    
    closeModal('delete-modal');
    if (type === 'estacionamento') {
        loadEstacionamentosPage();
        populateEstacionamentoDropdowns();
    }
    if (type === 'acesso') {
        loadAcessosPage(document.getElementById('acesso-estacionamento-filter').value);
    }
});

// =================================================================
// NAVIGATION
// =================================================================
const pages = document.querySelectorAll('.page');
const navLinks = document.querySelectorAll('.nav-link');

window.showPage = (pageId, openFormModal = false, isAcesso = false) => {
    pages.forEach(page => {
        page.classList.remove('active');
    });
    document.getElementById(pageId).classList.add('active');

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${pageId.replace('page-', '')}`) {
            link.classList.add('active');
        }
    });

    if (pageId === 'page-home') loadHomePage();
    if (pageId === 'page-estacionamentos') loadEstacionamentosPage();
    if (pageId === 'page-acessos') loadAcessosPage();
    
    if (openFormModal) {
        const modalId = isAcesso ? 'acesso-modal' : 'estacionamento-modal';
        const titleId = isAcesso ? 'acesso-modal-title' : 'estacionamento-modal-title';
        const defaultTitle = isAcesso ? 'Criar um Acesso' : 'Criar um Estacionamento';
        document.getElementById(titleId).textContent = defaultTitle;
        openModal(modalId);
    }
};

navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const pageId = `page-${link.getAttribute('href').substring(1)}`;
        showPage(pageId);
    });
});

document.getElementById('acesso-estacionamento-filter').addEventListener('change', (e) => {
    const filterId = e.target.value;
    loadAcessosPage(filterId);
});

// =================================================================
// INITIALIZATION
// =================================================================
function initApp() {
    document.getElementById('login-screen').classList.add('hidden');
    document.getElementById('app').classList.remove('hidden');
    showPage('page-home');
    populateEstacionamentoDropdowns();
}

document.getElementById('login-form').addEventListener('submit', (e) => {
    e.preventDefault();
    initApp();
});

// Make functions globally accessible for inline onclick attributes
window.handleEditEstacionamento = handleEditEstacionamento;
window.handleDelete = handleDelete;
window.handleEditAcesso = handleEditAcesso;
window.showPage = showPage;
window.openModal = openModal;
window.closeModal = closeModal;
