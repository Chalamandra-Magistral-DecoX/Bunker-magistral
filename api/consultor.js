const apiKey = process.env.GOOGLE_API_KEY;
const url = `https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=${apiKey}`;

async function preguntar(prompt) {
    const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            contents: [{ parts: [{ text: prompt }] }]
        })
    });
    const data = await response.json();
    console.log("🤖 Gemini dice:", data.candidates[0].content.parts[0].text);
}

preguntar("Analiza el estado del Microcosmos Elite. Somos una potencia en ascenso.");
