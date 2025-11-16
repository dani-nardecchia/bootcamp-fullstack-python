//con JQ usamos el signo $ para llamar a algo por id añadiendo siempre ademas el # antes del nombre 
$("#caja").text("Hola a todos");
//si solo escribieramos esto con JS, no cargaria si 
//linkeamos el archivo js en head  xq no ha cargado el DOM, no hay una "caja" donde escribir

//en JQ se soluciona con esta otra instruccion 

//dentro del ready hay que crear una funcion con lo que queremos que pase 

$(document).ready(function(){
    $("#caja").text("Hola a todos");
    
    //la sintaxis aca es pasar el estilo como string
    //osea con comillas

    //con todo esto modifique directamente el estilo de mi pagina, gracias a JQ 
    $("#caja").css({
        "background-color": "cornflowerblue", 
        "border": "2px solid black", 
        "color": "white", 
        "width": "250px", 
        "height": "250px",
        //vamos a cambiar el cursor para q sepa q se puede hacer click
        "cursor":"pointer"
    });

    //ahora manipularemos eventos!
    // onclick es en HTML, click es en JS 
    //NO olvida # antes del id!!!!
    $("#caja").click(function(){
        //alert("Has hecho click a la caja!");

        //agregaremos un parrafo al clickear 
    //  $("#caja").append("<p>Nuevo texto</p>");

        //tmbn se podria hacer con this 
        //estamos dentro de una funcion q se ejecutara
        //al clickear en caja, asi q no necesito volver a llamarla por id 
        $(this).append("<p>Nuevo texto</p>");
    });

    //esto agarraria todos los botones de la pagina, aca solo hay uno
    //NO lleva # xq solo es para id, mis nombres 
    //sin # busca elementos de HTML  
    $("button").click(function(){
        //queremos que la caja desaparezca 
        $("#caja").fadeToggle("slow");

    })




});

//esto es solo para ver q mi js carga :P 
console.log("Js cargado!");