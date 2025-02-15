const login = () => {
  const link =
    "https://script.googleusercontent.com/macros/echo?user_content_key=KgKQ2Oj4rtV0rU5njTbDay1B1gfJzjM_hFi0ErNrTHh9OphcOo_KdscrpZFDXvGlm8inhuQoivfrIBLMeh_A6RKIfWgUUwCFm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnPHfceE88sGtwpZtrQyBlDrYyiE3E4J6IANLw4UKO6ek-fZNWCTIAQk-PABwz6Q3SHRzqbpTwz6XUUiZxydDR26CKlQg_JT939z9Jw9Md8uu&lib=MZj_kfHkoxrRpYNE8CWpKtGJUPzYgWWy8";
  fetch(link)
    .then((response) => response.json())
    .then((data) => handleResponse(data))
    .catch((error) => console.error(error));
};

const handleResponse = (response) => {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const user = response.find(
    (row) => row["USUARIO"] == username && row["CONTRASEÑA"] == password
  );
  if (user == undefined) {
    alert("Usuario o contraseña incorrectos");
    return;
  }
  localStorage.setItem("user", username);
localStorage.setItem("rol", user["ROL"]);
  window.location.href = "../index.html";
};

const username = localStorage.getItem("user")
const rol = localStorage.getItem("rol")
if (username != null) {
  document.getElementById(
    "name-user"
  ).innerHTML = `<h4>${username}</h4><p>${rol}</p><button type="button" class="login" onclick="logout()">CERRAR SESION</button>`;
} else {
  document.getElementById("name-user").innerHTML =
    '<button type="button" class="login" onclick="window.location.href =\'html/Login.html\'">INICIAR SESION</button>';
}

const logout = () => {
  localStorage.removeItem("user");
  window.location.href = "index.html";
};