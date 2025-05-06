CREATE TABLE IF NOT EXISTS veiculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(10),
    modelo VARCHAR(50)
);

INSERT INTO veiculos (placa, modelo) VALUES ('DEF5678', 'Civic');
INSERT INTO veiculos (placa, modelo) VALUES ('GHI9012', 'Corolla');
INSERT INTO veiculos (placa, modelo) VALUES ('JKL3456', 'Fusca');
INSERT INTO veiculos (placa, modelo) VALUES ('MNO7890', 'Palio');
INSERT INTO veiculos (placa, modelo) VALUES ('PQR1234', 'Onix');
INSERT INTO veiculos (placa, modelo) VALUES ('STU5678', 'HB20');
INSERT INTO veiculos (placa, modelo) VALUES ('VWX9012', 'Sandero');
