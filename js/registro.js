<<<<<<< HEAD
const registrar = () => {
  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const passwordConfirm = document.getElementById("password-confirm").value;
  if (password != passwordConfirm) {
    alert("Las contraseñas no coinciden");
    return;
  }

  const myHeaders = new Headers();
  myHeaders.append(
    "Content-Type","Aplicattion/json"
  );
  const requestOptions = {
    method: "POST",
    headers: myHeaders,
    
  };
  const link =
    "https://script.google.com/macros/s/AKfycbzgnxYvq6hkZvmKcunsxx5aT6-hi8rbXO2UO3hQhdK3kyCJPdySLswPjlRhFUWzESRJkQ/exec";
  fetch(link,requestOptions)
    .then((response) => response.json())
    .then((data) => { })
    .catch((error) => console.error(error));
};
=======
const registrar = () => {
  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const passwordConfirm = document.getElementById("password-confirm").value;
  if (password != passwordConfirm) {
    alert("Las contraseñas no coinciden");
    return;
  }
  alert("Usted ha sido registrado exitosamente");
};
>>>>>>> 93f4b80998295ff468f6e5a9e14aae83110e9c5a
