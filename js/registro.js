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
