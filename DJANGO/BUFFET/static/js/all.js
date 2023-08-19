document.addEventListener('DOMContentLoaded', function() {
    alert("El HTML se ha cargado completamente");
});
function login() {
    var log = document.getElementById("login");
    var sig = document.getElementById("sign-in");
    var window = document.getElementById("ventana");
    log.style.display = "none";
    sig.style.display = "none";
    window.style.display = "flex";
}