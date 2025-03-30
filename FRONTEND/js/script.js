const username = localStorage.getItem("user");
const rol = localStorage.getItem("rol");

const add_menu_asistencia = (li, nav) => {
  const a = document.createElement("a");
  a.textContent = "ASISTENCIA";
  a.setAttribute("href", "asistencia.html");
  a.setAttribute("id", "asistencia-link");
  a.setAttribute("class", "nav-link text-white fw-bold fs-5");
  a.setAttribute(
    "onmouseover",
    "this.classList.replace('text-white', 'text-warning')"
  );
  a.setAttribute(
    "onmouseout",
    "this.classList.replace('text-warning', 'text-white')"
  );

  li.appendChild(a);
  nav.appendChild(li);

  const donaciones = document.getElementById("donaciones-link");
  donaciones.setAttribute("href", "donacion-admin.html");
};

const add_button_logout = () => {
  const usernameP = document.createElement("h4");
  const rolP = document.createElement("p");
  const button = document.createElement("button");

  usernameP.textContent = username;

  rolP.textContent = rol;
  button.setAttribute("type", "button");
  button.setAttribute("onclick", "logout()");
  button.setAttribute("class", "btn btn-warning text-dark rounded-pill me-2");
  button.setAttribute("onmouseover", "this.classList.add('btn-light')");
  button.setAttribute("onmouseout", "this.classList.remove('btn-light')");

  button.textContent = "Cerrar sesión";

  const nameUser = document.getElementById("name-user");
  nameUser.appendChild(usernameP);
  nameUser.appendChild(rolP);
  nameUser.appendChild(button);
};

const logout = () => {
  localStorage.removeItem("user");
  localStorage.removeItem("rol");
  if (window.location.href == "../html/login.html") {
    window.location.href = "../html/login.html";
  } else {
    window.location.href = "../html/login.html";
  }
};

if (username != null) {
  add_button_logout();
  if (rol == "Administrador") {
    const nav = document.getElementsByClassName("nav")[0];
    const li = document.createElement("li");
    li.setAttribute("class", "nav-item");
    add_menu_asistencia(li, nav);
    const peticiones = document.getElementById("peticiones-link");
    peticiones.setAttribute("href", "peticiones-admin.html");
  }
} else {
  window.location.href = "login.html";
}
