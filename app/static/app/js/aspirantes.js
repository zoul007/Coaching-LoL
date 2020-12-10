let url = "http://127.0.0.1:8000/api/aspirante/"
$.get(url, function(respuesta) {


  let res = document.querySelector('#res');
  res.innerHTML = '';

  let aspirante = respuesta.forEach(function(item) {
  /*  console.log(item)*/
  res.innerHTML += `
      <tr>
      <td>${item.nombre_invocador}</td>
      <td>${item.nombre_liga}</td>
      <td>${item.nombre_servidor}</td>
      </tr>
    `
  })

}, "json")
