function prenderLuz(){
    imagenActual= document.getElementById("ampolleta");
    //el src de una imagen es una propiedad que tiene un valor
    //y que se puede cambiar 
    //aca vamos a ver cual es la source de la imagen
    console.log(imagenActual.src);

    //tambien podria usar una alerta para ver algo mas rapido q con console
    //aler(imagenActual.src);

    if(imagenActual.src.includes("off.jpg")){
        imagenActual.src = "on.jpg";

    } else {
        imagenActual.src = "off.jpg";
    }
}