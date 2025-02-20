const username = localStorage.getItem("user");
const rol = localStorage.getItem("rol");
console.log(username);
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

  document
    .getElementById("name-user")
    .appendChild(usernameP)
    .appendChild(rolP)
    .appendChild(button);
} else {
  location.replace("proyecto/html/Login.html");
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
