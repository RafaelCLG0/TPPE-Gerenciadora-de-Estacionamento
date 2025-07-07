import { useEffect, useState } from "react";
import api from "../services/api";

export default function Acessos() {
  const [acessos, setAcessos] = useState([]);

  useEffect(() => {
    buscarAcessos();
  }, []);

  const buscarAcessos = async () => {
    try {
      const response = await api.get("/acessos/");
      setAcessos(response.data);
    } catch (error) {
      console.error("Erro ao buscar acessos", error);
    }
  };

  const deletarAcesso = async (id) => {
    if (!confirm("Deseja realmente deletar este acesso?")) return;
    try {
      await api.delete(`/acessos/${id}`);
      buscarAcessos();
    } catch (error) {
      alert("Erro ao deletar acesso");
    }
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Acessos</h2>

      <button className="bg-blue-600 text-white px-4 py-2 rounded mb-4">
        Novo Acesso
      </button>

      <table className="w-full border border-gray-300">
        <thead className="bg-gray-200">
          <tr>
            <th className="p-2 border">ID</th>
            <th className="p-2 border">Placa</th>
            <th className="p-2 border">Entrada</th>
            <th className="p-2 border">Saída</th>
            <th className="p-2 border">Estacionamento</th>
            <th className="p-2 border">Ações</th>
          </tr>
        </thead>
        <tbody>
          {acessos.map((a) => (
            <tr key={a.id} className="hover:bg-gray-50">
              <td className="p-2 border">{a.id}</td>
              <td className="p-2 border">{a.placa}</td>
              <td className="p-2 border">{a.entrada}</td>
              <td className="p-2 border">{a.saida}</td>
              <td className="p-2 border">{a.estacionamento?.nome}</td>
              <td className="p-2 border">
                <button
                  onClick={() => deletarAcesso(a.id)}
                  className="bg-red-500 text-white px-3 py-1 rounded"
                >
                  Deletar
                </button>
              </td>
            </tr>
          ))}
          {acessos.length === 0 && (
            <tr>
              <td colSpan="6" className="text-center p-4">
                Nenhum acesso registrado.
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
