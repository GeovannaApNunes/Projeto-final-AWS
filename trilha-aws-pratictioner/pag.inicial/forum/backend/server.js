// Importa o framework Express para criar o servidor
const express = require('express');

// Importa o CORS, que permite que outros sites acessem essa API (como seu frontend)
const cors = require('cors');

// Importa a conexão com o banco de dados (arquivo db.js)
const db = require('./db');

// Carrega variáveis de ambiente do arquivo .env
require('dotenv').config();

// Cria a aplicação Express
const app = express();

// Permite que qualquer origem acesse a API (útil para testes locais)
app.use(cors());

// Permite o uso de JSON no corpo das requisições (body)
app.use(express.json());

// Rota POST para receber dúvidas do formulário
app.post('/api/duvidas', (req, res) => {
  // Extrai os dados enviados pelo frontend (nome, email, duvida)
  const { nome, email, duvida } = req.body;

  // Verifica se todos os campos foram preenchidos
  if (!nome || !email || !duvida) {
    return res.status(400).json({ erro: 'Preencha todos os campos!' });
  }

  // Comando SQL para inserir os dados no banco de dados
  // Substitua "perguntas" pelo nome da sua tabela no MySQL
  const sql = 'INSERT INTO perguntas (titulo, corpo, usuario_id) VALUES (?, ?, NULL)';

  // Executa a query passando os valores do nome como título e da dúvida como corpo
  db.query(sql, [nome, duvida], (err, result) => {
    if (err) {
      // Em caso de erro no banco, retorna status 500
      return res.status(500).json({ erro: 'Erro ao salvar no banco' });
    }
    // Se tudo der certo, retorna mensagem de sucesso
    res.status(200).json({ mensagem: 'Dúvida enviada com sucesso!' });
  });
});

// Inicia o servidor na porta 3000 e exibe mensagem no terminal
app.listen(3000, () => console.log('Servidor rodando na porta 3000'));
