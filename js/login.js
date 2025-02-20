const login = () => {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  if (username == "" || password == "") {
    alert("Por favor ingrese su usuario y contraseña");
    return;
  }
  const link =
    "https://script.googleusercontent.com/macros/echo?user_content_key=KgKQ2Oj4rtV0rU5njTbDay1B1gfJzjM_hFi0ErNrTHh9OphcOo_KdscrpZFDXvGlm8inhuQoivfrIBLMeh_A6RKIfWgUUwCFm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnPHfceE88sGtwpZtrQyBlDrYyiE3E4J6IANLw4UKO6ek-fZNWCTIAQk-PABwz6Q3SHRzqbpTwz6XUUiZxydDR26CKlQg_JT939z9Jw9Md8uu&lib=MZj_kfHkoxrRpYNE8CWpKtGJUPzYgWWy8";
  fetch(link)
    .then((response) => response.json())
    .then((data) => handleResponse(data, username, password))
    .catch((error) => console.error(error));
};

const handleResponse = (response, username, password) => {
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
