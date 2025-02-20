const username = localStorage.getItem("user");
const rol = localStorage.getItem("rol");
if (username != null) {
  const usernameP = document.createElement("h4");
  const rolP = document.createElement("p");
  const button = document.createElement("button");

  usernameP.textContent = username;

  rolP.textContent = rol;

  button.setAttribute("type", "button");
  button.setAttribute("class", "logout");
  button.setAttribute("onclick", "logout()");
  button.textContent = "Cerrar sesión";

  const nameUser = document.getElementById("name-user");
  nameUser.appendChild(usernameP);
  nameUser.appendChild(rolP);
  nameUser.appendChild(button);
} else {
  const button2 = document.createElement("button");
  button2.setAttribute("type", "button");
  button2.setAttribute("class", "logout");
  button2.setAttribute("onclick", "location.href='html/Login.html'");
  button2.textContent = "Iniciar Sesión";

  document.getElementById("name-user").appendChild(button2);
}

const logout = () => {
  localStorage.removeItem("user");
  localStorage.removeItem("rol");
  if (window.location.href == "../index.html") {
    window.location.href = "html/Login.html";
  } else {
    window.location.href = "Login.html";
  }
};
