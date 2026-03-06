import React, { useLayoutEffect, useReducer } from 'react';

const initialState = { poas: 0, ltv_cac: 0, fidelidad: "0%", decision: "Cargando..." };

function mathReducer(state, action) {
  switch (action.type) {
    case "SET_METRICS": return { ...state, ...action.payload };
    default: return state;
  }
}

export default function App() {
  const [state, dispatch] = useReducer(mathReducer, initialState);

  useLayoutEffect(() => {
    const sync = async () => {
      try {
        const res = await fetch('http://localhost:5000/api/shor');
        const data = await res.json();
        dispatch({ type: "SET_METRICS", payload: data });
      } catch (e) { console.log("Reconectando..."); }
    };
    const t = setInterval(sync, 1500);
    return () => clearInterval(t);
  }, []);

  const handleScale = async () => {
    const res = await fetch('http://localhost:5000/api/scale', { method: 'POST' });
    const data = await res.json();
    alert(`💰 ¡Escalamiento Cuántico!: ${data.status}`);
  };

  return (
    <div style={{ background: '#000', color: '#0f0', minHeight: '100vh', padding: '40px', fontFamily: 'monospace' }}>
      <h1 style={{ borderBottom: '2px solid #0f0' }}>🌌 MICROCOSMOS: MONETIZACIÓN ACTIVA</h1>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', marginTop: '30px' }}>
        <div style={{ border: '2px solid #0f0', padding: '20px' }}>
          <h2>POAS: {state.poas}x</h2>
          <p>Decisión: {state.decision}</p>
        </div>
        <div style={{ border: '2px solid #00ffff', padding: '20px', color: '#00ffff' }}>
          <h2>FIDELIDAD: {state.fidelidad}</h2>
          <p>Estatus: Nirvana Estable</p>
        </div>
      </div>
      <button onClick={handleScale} style={{ marginTop: '40px', padding: '20px', background: '#0f0', color: '#000', fontWeight: 'bold', cursor: 'pointer', width: '100%' }}>
        ESCALAR CAMPAÑAS AHORA
      </button>
    </div>
  );
}
