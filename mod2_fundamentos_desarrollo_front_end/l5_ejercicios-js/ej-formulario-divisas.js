

function convertir(){
    let pesos = document.getElementById("pesos").value;
    let dolares = document.getElementById("dolar").value;
    
    let pesosNum= Number(pesos);
    let dolarNum = Number(dolares);

    if (!isNaN(pesosNum)) {
    document.getElementById("dolar").value = pesosNum*0.001081
}
    if (!isNaN(dolarNum)) {
    document.getElementById("pesos").value = dolarNum/0.001081
}
}

function limpiar(){
    document.getElementById("pesos").value = "";
    document.getElementById("dolar").value = "";
}