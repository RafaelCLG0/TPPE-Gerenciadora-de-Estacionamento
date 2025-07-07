import { Link, Outlet } from "react-router-dom";

export default function Layout() {
  return (
    <div className="flex min-h-screen">
      {/* Sidebar */}
      <aside className="w-64 bg-blue-600 text-white flex flex-col p-4">
        <h2 className="text-2xl font-bold mb-6">Estacionamento</h2>

        <nav className="flex flex-col gap-4">
          <Link to="/" className="hover:underline">Home</Link>
          <Link to="/usuarios" className="hover:underline">Usuários</Link>
          <Link to="/estacionamentos" className="hover:underline">Estacionamentos</Link>
          <Link to="/acessos" className="hover:underline">Acessos</Link>
          <Link to="/relatorios/acessos" className="hover:underline">Relatório Acessos</Link>
          <Link to="/relatorios/repasses" className="hover:underline">Relatório Repasses</Link>
        </nav>
      </aside>

      {/* Conteúdo principal */}
      <div className="flex-1 flex flex-col">
        <header className="bg-gray-100 p-4 border-b flex justify-between items-center">
          <h1 className="text-xl font-semibold">Painel do Sistema</h1>
          <div>Usuário: Admin</div>
        </header>

        <main className="p-6">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
