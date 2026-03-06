const express = require('express');
const cors = require('cors');
const { getCosmosState } = require('./quantum_engine');
const app = express();
app.use(cors());

app.get('/api/shor', (req, res) => {
    res.json(getCosmosState());
});

app.post('/api/scale', (req, res) => {
    res.json({ status: "Presupuesto +10% aplicado", timestamp: new Date() });
});

app.listen(5000, () => console.log('🚀 API de Monetización activa en puerto 5000'));
