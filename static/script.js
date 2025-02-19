async function buscarRespuesta() {
    const query = document.getElementById("query").value;
    const respuestaDiv = document.getElementById("respuesta");
    
    if (!query.trim()) {
        respuestaDiv.innerHTML = "Por favor, escribe una pregunta.";
        return;
    }

    const response = await fetch("/faq/suggest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: query })
    });

    const data = await response.json();
    respuestaDiv.innerHTML = `Respuesta: ${data.suggestion}`;
    actualizarHistorial();
}

async function actualizarHistorial() {
    const historialUl = document.getElementById("historial");
    historialUl.innerHTML = "";

    const response = await fetch("/faq/history");
    const data = await response.json();

    data.forEach(item => {
        const li = document.createElement("li");
        li.textContent = `${item.query} → ${item.suggestion}`;
        historialUl.appendChild(li);
    });
}
async function agregarPregunta() {
    const pregunta = document.getElementById("newPregunta").value;
    const respuesta = document.getElementById("newRespuesta").value;
    const mensajeDiv = document.getElementById("addMessage");

    if (!pregunta.trim() || !respuesta.trim()) {
        mensajeDiv.innerHTML = "Por favor, completa ambos campos.";
        return;
    }

    const response = await fetch("/faq/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pregunta, respuesta })
    });
    
    const data = await response.json();
    mensajeDiv.innerHTML = data.mensaje;

    if (response.ok) {
        document.getElementById("newPregunta").value = "";
        document.getElementById("newRespuesta").value = "";
        actualizarHistorial();
    }
}


// Cargar historial al inicio
document.addEventListener("DOMContentLoaded", actualizarHistorial);
