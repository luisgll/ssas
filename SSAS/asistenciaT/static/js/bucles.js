/**
 *Ciclos
 */

var nombre =prompt("Ingrese su nombbre");
while (nombre ==''){
    nombre = prompt("Ingrese Su nombre")
}

document.write("Bienvenido "+nombre);

for (var i=0; i<20; i++){
    document.write(i+")<br> Hola "+nombre+" esde el for ")

    }



var tabla = prompt("ingrese numero");
tabla = parseInt(tabla);
for (var i=0; i < 11; i++){
    document.write("<br>"+tabla+"*"+i+"=");
    document.write(tabla*i);}