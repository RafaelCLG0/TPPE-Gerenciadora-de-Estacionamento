CREATE TABLE IF NOT EXISTS acessos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(10) NOT NULL,
    tipo_acesso VARCHAR(20) NOT NULL,
    horario_entrada DATETIME NOT NULL,
    horario_saida DATETIME
);
