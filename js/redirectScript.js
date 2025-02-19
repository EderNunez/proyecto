const username = localStorage.getItem("user");
const rol = localStorage.getItem("rol");
console.log(username);
if (username != null) {
  document.getElementById(
    "name-user"
  ).innerHTML = `<h4>${username}</h4><p>${rol}</p><button type="button" class="logout" onclick="logout()">CERRAR SESION</button>`;
} else {
  window.location.href = "/html/Login.html";
}

const logout = () => {
  localStorage.removeItem("user");
  localStorage.removeItem("rol");
  window.location.href = "/html/Login.html";
};
