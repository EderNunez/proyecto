const myHeaders = new Headers();
myHeaders.append(
  "x-collection-access-token",
  "c7b04cd9-bcbd-46e4-b8fb-d45faa6e3422" // cambia con el usuario y depende si la colección es publica o privada
);

var requestOptions = {
  method: "GET",
  headers: myHeaders,
  redirect: "follow",
};

fetch(
  "https://api.myjson.online/v1/collections/2ebf7382-6cfe-48f2-a1d6-26baf17f71f9/records", // cambia con el usuario
  requestOptions
)
  .then((response) => response.json())
  .then((result) => handleTableData(result))
  .catch((error) => console.log("error", error));

const handleTableData = (result) => {
  const data = result.records;
  for (let index = 0; index < data.length; index++) {
    const element = data[index].data;
    const row = document.createElement("tr");
    const nombreCell = document.createElement("td");
    const apellidoCell = document.createElement("td");
    const telefonoCell = document.createElement("td");
    const barrioCell = document.createElement("td");
    const direccionCell = document.createElement("td");
    const cargoCell = document.createElement("td");
    const bautizadoCell = document.createElement("td");

    nombreCell.textContent = element["nombre"];
    apellidoCell.textContent = element["apellido"];
    telefonoCell.textContent = element["telefono"];
    barrioCell.textContent = element["barrio"];
    direccionCell.textContent = element["direccion"];
    cargoCell.textContent = element["cargo"];
    bautizadoCell.textContent = element["bautizado"];

    row.appendChild(nombreCell);
    row.appendChild(apellidoCell);
    row.appendChild(telefonoCell);
    row.appendChild(barrioCell);
    row.appendChild(direccionCell);
    row.appendChild(cargoCell);
    row.appendChild(bautizadoCell);

    document.getElementById("tablaCuerpo").appendChild(row);
  }
};

const add = () => {
  const nombre = document.getElementById("nombre").value;
  const apellido = document.getElementById("apellido").value;
  const telefono = document.getElementById("telefono").value;
  const barrio = document.getElementById("barrio").value;
  const direccion = document.getElementById("direccion").value;
  const cargo = document.getElementById("cargo").value;
  const bautizado = document.getElementById("bautizado").value;

  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/x-www-form-urlencoded");
  myHeaders.append(
    "x-collection-access-token",
    "c7b04cd9-bcbd-46e4-b8fb-d45faa6e3422" // cambia con el usuario
  );

  const jsonReport = `{"nombre": "${nombre}", "apellido": "${apellido}", "telefono": "${telefono}", "barrio": "${barrio}", "direccion": "${direccion}", "cargo": "${cargo}", "bautizado": "${bautizado}"}`;
  const urlencoded = new URLSearchParams();
  urlencoded.append("jsonData", jsonReport);
  urlencoded.append("collectionId", "2ebf7382-6cfe-48f2-a1d6-26baf17f71f9"); // cambia con el usuario

  const requestOptions = {
    method: "POST",
    headers: myHeaders,
    body: urlencoded,
    redirect: "follow",
  };

  fetch("https://api.myjson.online/v1/records", requestOptions)
    .then((response) => response.json())
    .then((_) => handleTableDataCurrent(jsonReport))
    .catch((error) => console.log("error", error));
};

const handleTableDataCurrent = (jsonReport) => {
  const data = JSON.parse(jsonReport);
  const row = document.createElement("tr");
  const nombreCell = document.createElement("td");
  const apellidoCell = document.createElement("td");
  const telefonoCell = document.createElement("td");
  const barrioCell = document.createElement("td");
  const direccionCell = document.createElement("td");
  const cargoCell = document.createElement("td");
  const bautizadoCell = document.createElement("td");

  nombreCell.textContent = data["nombre"];
  apellidoCell.textContent = data["apellido"];
  telefonoCell.textContent = data["telefono"];
  barrioCell.textContent = data["barrio"];
  direccionCell.textContent = data["direccion"];
  cargoCell.textContent = data["cargo"];
  bautizadoCell.textContent = data["bautizado"];

  row.appendChild(nombreCell);
  row.appendChild(apellidoCell);
  row.appendChild(telefonoCell);
  row.appendChild(barrioCell);
  row.appendChild(direccionCell);
  row.appendChild(cargoCell);
  row.appendChild(bautizadoCell);

  document.getElementById("tablaCuerpo").appendChild(row);
};
