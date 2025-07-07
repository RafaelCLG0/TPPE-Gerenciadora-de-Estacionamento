import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Usuarios from "./pages/Usuarios";
import Estacionamentos from "./pages/Estacionamentos";
import Acessos from "./pages/Acessos";
import RelatorioAcessos from "./pages/RelatorioAcessos";
import RelatorioRepasses from "./pages/RelatorioRepasses";
import Layout from "./components/Layout";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="usuarios" element={<Usuarios />} />
          <Route path="estacionamentos" element={<Estacionamentos />} />
          <Route path="acessos" element={<Acessos />} />
          <Route path="relatorios/acessos" element={<RelatorioAcessos />} />
          <Route path="relatorios/repasses" element={<RelatorioRepasses />} />
        </Route>
      </Routes>
    </Router>
  );
}
