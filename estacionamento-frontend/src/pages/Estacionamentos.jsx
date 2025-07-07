import { useEffect, useState } from "react";
import api from "../services/api";

export default function Estacionamentos() {
  const [estacionamentos, setEstacionamentos] = useState([]);
  const [mostrarFormulario, setMostrarFormulario] = useState(false);
  const [visualizando, setVisualizando] = useState(null);

  const [formulario, setFormulario] = useState({
    nome: "",
    cnpj: "",
    capacidade: "",
    valorFracao: "",
    valorHoraCheia: "",
    valorDiaria: "",
    valorMensalista: "",
    valorEvento: "",
    valorNoturno: "",
    horarioNoturnoInicio: "",
    horarioNoturnoFim: "",
    percentualRepasse: "",
  });

  useEffect(() => {
    buscarEstacionamentos();
  }, []);

  const buscarEstacionamentos = async () => {
    try {
      const response = await api.get("/estacionamentos/");
      setEstacionamentos(response.data);
    } catch (error) {
      console.error("Erro ao buscar estacionamentos", error);
    }
  };

  const deletarEstacionamento = async (id) => {
    if (!confirm("Deseja realmente deletar este estacionamento?")) return;
    try {
      await api.delete(`/estacionamentos/${id}`);
      buscarEstacionamentos();
    } catch (error) {
      alert("Erro ao deletar estacionamento");
    }
  };

  const salvarEstacionamento = async (e) => {
    e.preventDefault();
    if (
      !formulario.nome || !formulario.cnpj || !formulario.capacidade ||
      !formulario.valorFracao || !formulario.valorHoraCheia || !formulario.valorDiaria ||
      !formulario.valorMensalista || !formulario.valorEvento || !formulario.valorNoturno ||
      !formulario.horarioNoturnoInicio || !formulario.horarioNoturnoFim || !formulario.percentualRepasse
    ) {
      return alert("Preencha todos os campos obrigatórios.");
    }

    try {
      await api.post("/estacionamentos/", {
        nome: formulario.nome,
        cnpj: formulario.cnpj,
        capacidade: parseInt(formulario.capacidade),
        valorFracao: parseFloat(formulario.valorFracao),
        valorHoraCheia: parseFloat(formulario.valorHoraCheia),
        valorDiaria: parseFloat(formulario.valorDiaria),
        valorMensalista: parseFloat(formulario.valorMensalista),
        valorEvento: parseFloat(formulario.valorEvento),
        valorNoturno: parseFloat(formulario.valorNoturno),
        horarioNoturnoInicio: formulario.horarioNoturnoInicio,
        horarioNoturnoFim: formulario.horarioNoturnoFim,
        percentualRepasse: parseFloat(formulario.percentualRepasse),
      });
      setFormulario({
        nome: "",
        cnpj: "",
        capacidade: "",
        valorFracao: "",
        valorHoraCheia: "",
        valorDiaria: "",
        valorMensalista: "",
        valorEvento: "",
        valorNoturno: "",
        horarioNoturnoInicio: "",
        horarioNoturnoFim: "",
        percentualRepasse: "",
      });
      setMostrarFormulario(false);
      buscarEstacionamentos();
    } catch (error) {
      console.error("Erro ao cadastrar", error);
      alert("Erro ao cadastrar estacionamento");
    }
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Estacionamentos</h2>

      <button
        className="bg-blue-600 text-white px-4 py-2 rounded mb-4"
        onClick={() => setMostrarFormulario(true)}
      >
        Novo Estacionamento
      </button>

      <table className="w-full border border-gray-300">
        <thead className="bg-gray-200">
          <tr>
            <th className="p-2 border">ID</th>
            <th className="p-2 border">Nome</th>
            <th className="p-2 border">CNPJ</th>
            <th className="p-2 border">Capacidade</th>
            <th className="p-2 border">Ações</th>
          </tr>
        </thead>
        <tbody>
          {estacionamentos.map((e) => (
            <tr key={e.id} className="hover:bg-gray-50">
              <td className="p-2 border">{e.id}</td>
              <td className="p-2 border">{e.nome}</td>
              <td className="p-2 border">{e.cnpj}</td>
              <td className="p-2 border">{e.capacidade}</td>
              <td className="p-2 border flex gap-2">
                <button
                  onClick={() => setVisualizando(e)}
                  className="bg-blue-500 text-white px-3 py-1 rounded"
                >
                  Visualizar
                </button>
                <button
                  onClick={() => deletarEstacionamento(e.id)}
                  className="bg-red-500 text-white px-3 py-1 rounded"
                >
                  Deletar
                </button>
              </td>
            </tr>
          ))}
          {estacionamentos.length === 0 && (
            <tr>
              <td colSpan="5" className="text-center p-4">Nenhum estacionamento cadastrado.</td>
            </tr>
          )}
        </tbody>
      </table>

      {mostrarFormulario && (
        <div className="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg shadow-lg w-full max-w-2xl p-6">
            <h2 className="text-lg font-bold bg-blue-600 text-white px-4 py-2 rounded-t">Criar um estacionamento</h2>

            <form onSubmit={salvarEstacionamento} className="mt-4 grid grid-cols-2 gap-4">
              <input type="text" placeholder="Nome" value={formulario.nome} onChange={(e) => setFormulario({ ...formulario, nome: e.target.value })} className="border p-2 w-full rounded" required />
              <input type="text" placeholder="CNPJ" value={formulario.cnpj} onChange={(e) => setFormulario({ ...formulario, cnpj: e.target.value })} className="border p-2 w-full rounded" required />
              <input type="number" placeholder="Valor Fração" value={formulario.valorFracao} onChange={(e) => setFormulario({ ...formulario, valorFracao: e.target.value })} className="border p-2 w-full rounded" required />
              <input type="number" placeholder="Valor Hora Cheia" value={formulario.valorHoraCheia} onChange={(e) => setFormulario({ ...formulario, valorHoraCheia: e.target.value })} className="border p-2 w-full rounded" required />
              <input type="number" placeholder="Valor Diária" value={formulario.valorDiaria} onChange={(e) => setFormulario({ ...formulario, valorDiaria: e.target.value })} className="border p-2 w-full rounded" required />
              <input type="number" placeholder="Valor Mensalista" value={formulario.valorMensalista} onChange={(e) => setFormulario({ ...formulario, valorMensalista: e.target.value })} className="border p-2 w-full rounded" required />
              <input type="number" placeholder="Valor Evento" value={formulario.valorEvento} onChange={(e) => setFormulario({ ...formulario, valorEvento: e.target.value })} className="border p-2 w-full rounded" required />
              <input type="number" placeholder="Valor Noturno" value={formulario.valorNoturno} onChange={(e) => setFormulario({ ...formulario, valorNoturno: e.target.value })} className="border p-2 w-full rounded" required />
              <input type="time" value={formulario.horarioNoturnoInicio} onChange={(e) => setFormulario({ ...formulario, horarioNoturnoInicio: e.target.value })} className="border p-2 w-full rounded" required />
              <input type="time" value={formulario.horarioNoturnoFim} onChange={(e) => setFormulario({ ...formulario, horarioNoturnoFim: e.target.value })} className="border p-2 w-full rounded" required />
              <input type="number" placeholder="Capacidade" value={formulario.capacidade} onChange={(e) => setFormulario({ ...formulario, capacidade: e.target.value })} className="border p-2 w-full rounded" required />
              <input type="number" placeholder="Percentual de Repasse" value={formulario.percentualRepasse} onChange={(e) => setFormulario({ ...formulario, percentualRepasse: e.target.value })} className="border p-2 w-full rounded" required />
            </form>

            <div className="flex justify-end gap-4 mt-6">
              <button onClick={() => setMostrarFormulario(false)} type="button" className="bg-gray-200 px-4 py-2 rounded">Cancelar</button>
              <button onClick={salvarEstacionamento} className="bg-blue-600 text-white px-4 py-2 rounded">Salvar</button>
            </div>
          </div>
        </div>
      )}

      {visualizando && (
        <div className="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg shadow-lg w-[400px] p-6">
            <h2 className="text-lg font-bold mb-4">Detalhes do Estacionamento</h2>
            <p><strong>Nome:</strong> {visualizando.nome}</p>
            <p><strong>CNPJ:</strong> {visualizando.cnpj}</p>
            <p><strong>Capacidade:</strong> {visualizando.capacidade}</p>
            <p><strong>Percentual Repasse:</strong> {visualizando.percentualRepasse}%</p>

            <div className="mt-4 flex justify-end">
              <button onClick={() => setVisualizando(null)} className="bg-gray-200 px-4 py-2 rounded">Fechar</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
