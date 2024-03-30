const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

let messages = [];

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.get('/messages', (req, res) => {
  res.json(messages);
});

app.post('/messages', (req, res) => {
  const { user, text } = req.body;
  if (user && text) {
    const newMessage = { user, text, timestamp: new Date() };
    messages.push(newMessage);
    res.status(201).json(newMessage);
  } else {
    res.status(400).send('Bad request: Missing user or text field.');
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
