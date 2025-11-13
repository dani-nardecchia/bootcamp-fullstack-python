//function es palabra restringida
function suma(){
    //esto que esta entre los corchetes es la función
    return 2+2; //punto y coma indica que se acabo la linea
    // se recomienda usarlo siempre, excepto en las llaves 
}

//console log me deja verlo en la consola del inspector
//no es necesario para todo 
//Se llama la funcion dentro del log con su nombre 
console.log(suma());

//si abro la consola en el inspecto solo me saldra un 4 

function suma2(valorPrueba){
    return valorPrueba + 2
}

//ahora debo darle un parametro 
console.log(suma2(3))

//cuando reviso la consola en el navegador 
//ahora me sale un 4 de la primera funcion y un 5 de la segunda 

function suma2Valores (valor1, valor2){
    return valor1 + valor2
}

console.log(suma2Valores(5,6))

//ejemplos con operadores 
let a=10;

//este da falso porque es un true y un falso 
console.log((a>5) && (a<5));

let b=4;
//este da true porque es un true y un true 

console.log((a>5) && (b<5));

//probaremos condicionales 

let edad=15; 
 
if (edad>17){
    console.log("Mayor de edad")
}


//la primera linea lleva lo q se ejecita si es true
if (edad>17) {
    console.log("Mayor de edad")
} else { //esta lleva lo que se ejecuta si es false 
    console.log("No es mayor de edad")
}
//super importante respetar las {} y los punto y coma!!! 


//ciclos
//inicializamos el contador  
let i = 0; 

//la condicion va entre los parentesis 
//que ejecuto va dentro de las corchetes 
while(i <5){
    console.log("valor de i: ", i);
    //esto le suma uno a i 
    i++ 
}