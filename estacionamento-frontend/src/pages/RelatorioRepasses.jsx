import { useEffect, useState } from "react";
import api from "../services/api";

export default function RelatorioRepasses() {
  const [repasses, setRepasses] = useState([]);
  const [inicio, setInicio] = useState("");
  const [fim, setFim] = useState("");

  const buscarRepasses = async () => {
    if (!inicio || !fim) return alert("Informe as datas inicial e final.");

    try {
      const response = await api.get(`/relatorios/repasses/?inicio=${inicio}&fim=${fim}`);
      setRepasses(response.data);
    } catch (error) {
      console.error("Erro ao buscar relatório de repasses", error);
    }
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Relatório de Repasses</h2>

      <div className="flex gap-4 mb-4">
        <input
          type="date"
          value={inicio}
          onChange={(e) => setInicio(e.target.value)}
          className="border p-2"
        />
        <input
          type="date"
          value={fim}
          onChange={(e) => setFim(e.target.value)}
          className="border p-2"
        />
        <button
          onClick={buscarRepasses}
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Buscar
        </button>
      </div>

      <table className="w-full border border-gray-300">
        <thead className="bg-gray-200">
          <tr>
            <th className="p-2 border">Estacionamento</th>
            <th className="p-2 border">Valor Bruto</th>
            <th className="p-2 border">Valor Repassado</th>
            <th className="p-2 border">Lucro</th>
          </tr>
        </thead>
        <tbody>
          {repasses.map((item) => (
            <tr key={item.estacionamento_id} className="hover:bg-gray-50">
              <td className="p-2 border">{item.estacionamento_nome}</td>
              <td className="p-2 border">R$ {item.valor_bruto.toFixed(2)}</td>
              <td className="p-2 border">R$ {item.valor_repasse.toFixed(2)}</td>
              <td className="p-2 border">R$ {item.lucro.toFixed(2)}</td>
            </tr>
          ))}
          {repasses.length === 0 && (
            <tr>
              <td colSpan="4" className="text-center p-4">
                Nenhum dado encontrado.
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
