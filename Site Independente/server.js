const express = require('express');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/contato', async (req, res) => {
  const { nome, email, mensagem } = req.body;

  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: 'SEUEMAIL@gmail.com',
      pass: 'SENHA_DE_APP' // senha de app, não a senha do Gmail
    }
  });

  const mailOptions = {
    from: 'SEUEMAIL@gmail.com',
    to: 'SEUEMAIL@gmail.com',
    subject: `Contato via site - ${nome}`,
    text: `Nome: ${nome}\nEmail: ${email}\nMensagem:\n${mensagem}`
  };

  try {
    await transporter.sendMail(mailOptions);
    res.send('Mensagem enviada com sucesso!');
  } catch (error) {
    console.error('Erro ao enviar e-mail:', error);
    res.status(500).send('Erro ao enviar e-mail');
  }
});

app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});
