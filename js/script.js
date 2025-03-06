if (rol != null) {
  const asistenciaLink = document.getElementById("asistencia-link");
  if (rol !== "ADMINISTRADOR") {
    asistenciaLink.setAttribute("href", "#");
    asistenciaLink.onclick = () => {
      alert("No tienes permiso para acceder a esta página");
    };
  }
}
