import { useEffect, useState } from "react";
import api from "../services/api";

export default function RelatorioAcessos() {
  const [relatorio, setRelatorio] = useState([]);

  useEffect(() => {
    buscarRelatorio();
  }, []);

  const buscarRelatorio = async () => {
    try {
      const response = await api.get("/relatorios/acessos/");
      setRelatorio(response.data);
    } catch (error) {
      console.error("Erro ao buscar relatório de acessos", error);
    }
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Relatório de Acessos por Estacionamento</h2>

      <table className="w-full border border-gray-300">
        <thead className="bg-gray-200">
          <tr>
            <th className="p-2 border">Estacionamento</th>
            <th className="p-2 border">Total de Acessos</th>
          </tr>
        </thead>
        <tbody>
          {relatorio.map((item) => (
            <tr key={item.estacionamento_id} className="hover:bg-gray-50">
              <td className="p-2 border">{item.estacionamento_nome}</td>
              <td className="p-2 border">{item.total_acessos}</td>
            </tr>
          ))}
          {relatorio.length === 0 && (
            <tr>
              <td colSpan="2" className="text-center p-4">
                Nenhum dado encontrado.
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
