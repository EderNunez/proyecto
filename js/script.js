console.log(rol)
const asistenciaLink = document.getElementById("asistencia-link");
if (rol !== "administrador") {
  asistenciaLink.setAttribute("href", "#");
  asistenciaLink.onclick = () => {
    alert("No tienes permiso para acceder a esta página");
  };
}
