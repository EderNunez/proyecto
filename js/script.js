if (rol != null && rol == "ADMINISTRADOR") {
  const menu = document.getElementById("menu");
  const li = document.createElement('li')
  const a = document.createElement('a')
  a.setAttribute('href', 'asistencia.html')
  a.setAttribute('id', 'asistencia-link')
  const b = document.createElement('b')
  b.textContent = 'ASISTENCIA'
  a.appendChild(b)
  li.appendChild(a)
  menu.appendChild(li);
}
