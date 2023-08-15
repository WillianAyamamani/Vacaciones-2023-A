let imgzoom,Img,Img_D,Img_N,Img_P
window.onload = function() {
    imgzoom=document.getElementById("zoom"),
    Img=document.getElementById("zImagen");
    Img_D = document.getElementById("descripcion")
    Img_N = document.getElementById("nombre")
    Img_P = document.getElementById("precio")
}

function cerrar(){
    imgzoom.style.display = "none";
}
function Open(ubi,nombre,des,precio){
    // Asignar los valores a los campos ocultos de input
    document.getElementById("nombre_input").value = nombre;
    document.getElementById("descripcion_input").value = des;
    document.getElementById("precio_input").value=precio;
    document.getElementById("imagen_url").value=ubi
    Img.src = ubi
    Img_N.textContent = nombre
    Img_D.innerHTML = des
    Img_P.textContent = 'S/.' + precio
    imgzoom.style.display="flex";
}