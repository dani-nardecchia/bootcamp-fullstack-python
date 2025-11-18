$(document).ready(function(){
    $("#raulito").click(function addTask(){
    let tarea = $("#tarea").val()
    let prioridad = $("#prioridad").val() 



    let fila = $("<tr></tr>")
    let contTexto = $("<td></td>").append(tarea);
    let contPrioridad = $("<td></td>").append(prioridad);

    if (prioridad == "Alta") {
        contPrioridad.css({"background-color": "red", "color":"white"});        
    }else if (prioridad == "Media"){
        contPrioridad.css({"background-color": "orange", "color":"white"});
    }else if (prioridad == "Baja"){
        contPrioridad.css({"background-color": "green", "color":"white"})
    }

    let contCheck =$("<td></td>")
    let cajaTer = $("<div></div>")
    let milabel = $('<label>Terminada</label>')
    let micheck = $('<input type="checkbox" id="checkBox">')

    $("#tarea").val("");

    cajaTer.append(micheck, milabel);

    contCheck.append(cajaTer)

    fila.append(contTexto);
    fila.append(contPrioridad);
    fila.append(contCheck);


    $("#tabla").append(fila);

    cajaTer.css({
        "padding" : "1px", 
    })

    //esto dice
    //en tabla (elemento principal que se crea al comienzo)
    //si hay un cambio en el input checkbox, corre esta funcuion 
    $("#tabla").on("change","input[type=checkbox]", function(){
        $(this).closest("tr").fadeOut("slow");
    })




})
})


console.log("JS cargado!")
