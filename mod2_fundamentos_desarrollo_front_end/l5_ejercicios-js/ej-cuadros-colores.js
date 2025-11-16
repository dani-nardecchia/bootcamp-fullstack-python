let seccionBody= document.getElementById("cuerpo");

function entrar(seccion){
    let colorSeccion = seccion.style.backgroundColor;
    seccionBody.style.backgroundColor = colorSeccion;
}

function salir(){
    document.getElementById("cuerpo").style.backgroundColor ="white";
}

console.log("JS cargado, al fin.");