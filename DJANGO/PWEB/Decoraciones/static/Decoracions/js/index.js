let imgzoom,Img,Img_D,Img_N,Img_P,Catg
window.onload = function() {
    imgzoom=document.getElementById("zoom")
    Img=document.getElementById("zImagen")
    Img_D = document.getElementById("descripcion")
    Img_N = document.getElementById("nombre")
    Img_P = document.getElementById("precio")
    Catg = document.getElementById("Abe")
}

function cerrar(){
    imgzoom.style.display = "none";
}
function Open(ubi,nombre,des,precio,categoria){
    // Asignar los valores a los campos ocultos de input
    document.getElementById("nombre_input").value = nombre;
    document.getElementById("descripcion_input").value = des;
    document.getElementById("precio_input").value=parseFloat(precio);
    document.getElementById("imagen_url").value=ubi;
    Img.src = ubi
    Catg.textContent = categoria
    Img_N.textContent = nombre
    Img_D.innerHTML = des
    Img_P.textContent = 'S/.' + precio
    imgzoom.style.display="flex";
}
$(document).ready(function() {
    $("#btn-descargar").click(function() {
      $.ajax({
        type: "GET",
        url: descargarPDFURL, // Utilizar la variable global que contiene la URL
        success: function(data, textStatus, jqXHR) {
          var link = document.createElement("a");
          link.href = window.URL.createObjectURL(data);
          link.download = "archivo.pdf";
          link.click();
        },
        error: function(jqXHR, textStatus, errorThrown) {
          alert("Error al descargar el archivo PDF.");
        }
      });
    });
  });
  