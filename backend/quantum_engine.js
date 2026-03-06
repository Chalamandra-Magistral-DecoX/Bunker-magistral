const os = require('os');

function getCosmosState() {
    const freeMem = os.freemem();
    const totalMem = os.totalmem();
    const load = (1 - (freeMem / totalMem));
    const revenue = Math.random() * 1000 + 500;
    const adSpend = 200;
    const cogs = revenue * 0.45;
    const fees = revenue * 0.12;
    const netProfit = revenue - cogs - fees;
    const poas = (netProfit / adSpend).toFixed(2);
    const ltv = (Math.random() * 300 + 600).toFixed(2);
    const cac = (adSpend / (Math.random() * 10 + 5)).toFixed(2);

    return {
        poas: poas,
        roas: (revenue / adSpend).toFixed(2),
        ltv_cac: (ltv / cac).toFixed(2),
        fidelidad: "96.4%",
        segmentos: Math.floor(Math.random() * 500 + 800),
        riesgo_trabe: (load * 100).toFixed(1) + "%",
        estado: poas > 1.2 ? "REINVERSIÓN AGRESIVA" : "OPTIMIZACIÓN DE MARGEN"
    };
}

module.exports = { getCosmosState };
