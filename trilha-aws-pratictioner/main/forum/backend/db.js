// Importa o módulo mysql2, que permite conectar ao MySQL usando Node.js
const mysql = require('mysql2'); 

// Carrega as variáveis de ambiente do arquivo .env
require('dotenv').config();

// Cria a conexão com o banco de dados usando as variáveis do .env
const db = mysql.createConnection({
  host: process.env.DB_HOST,       // Endereço do banco (ex: localhost ou endpoint da AWS RDS)
  user: process.env.DB_USER,       // Nome de usuário do banco
  password: process.env.DB_PASSWORD, // Senha do banco
  database: process.env.DB_NAME    // Nome do banco de dados
});

// Conecta ao banco de dados e trata possíveis erros
db.connect(err => {
  if (err) throw err; // Mostra o erro se a conexão falhar
  console.log('Conectado ao banco de dados!'); // Mensagem de sucesso
});

// Exporta a conexão para ser usada em outros arquivos do backend
module.exports = db;
