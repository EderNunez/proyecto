document
  .getElementById("registroForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Obtener valores del formulario
    let nombre = document.getElementById("nombre").value;
    let apellido = document.getElementById("apellido").value;
    let telefono = document.getElementById("telefono").value;
    let barrio = document.getElementById("barrio").value;
    let direccion = document.getElementById("direccion").value;
    let cargo = document.getElementById("cargo").value;
    let bautizado = document.getElementById("bautizado").value;

    // Crear nueva fila en la tabla
    let tabla = document.getElementById("tablaCuerpo");
    let nuevaFila = tabla.insertRow();

    nuevaFila.innerHTML = `
        <td>${nombre}</td>
        <td>${apellido}</td>
        <td>${telefono}</td>
        <td>${barrio}</td>
        <td>${direccion}</td>
        <td>${cargo}</td>
        <td>${bautizado}</td>
        <td><input type="checkbox"></td>
    `;

    // Limpiar el formulario
    document.getElementById("registroForm").reset();
  });
