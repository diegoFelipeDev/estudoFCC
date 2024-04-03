function soma(num1, num2, num3) {
    let resultado = num1 + num2 + num3;
    return resultado ;
}
    soma(5, 10, 2)
-----------------------------------------------
function soma(banana, maça, pera) {
    let totalDeFrutas = banana + maça + pera;
    return resultado ;
}
    soma(15, 12, 20)

-----------------------------------------------
function apresentar (nome) {
  let texto = "Olá," + nome;
  return texto;
}
apresentar ("Diego")

-----------------------------------------------
function calcularMedia (nota1, nota2, nota3) {
	let media = ((nota1 * 3) + (nota2 * 3) + (nota3 * 4)) / 10;
	let resultado = "Sua média foi: " + media;
	return resultado;
}
 calcularMedia (6, 7 ,3)
-----------------------------------------------
let notaDesafio = 150;

   if (notaDesafio >= 100) {
	console.log("aprovado");
} else {
	console.log("Não aprovado");
}

-----------------------------------------------
function determinarGeracao(anoDeNascimento) {
 
  let resultado;
  
  if(anoDeNascimento <= 1945){
    resultado = "Geração silenciosa";
  } else if(anoDeNascimento <= 1964){
      resultado = "Boomers";
  } else if(anoDeNascimento <= 1980){
      resultado = "Geração X";
  } else if(anoDeNascimento <= 1996){
      resultado = "Millennials";
  } else(anoDeNascimento > 1996){
      resultado = "Geração Z";
  }


  return resultado;
------------------------------------------------
let numero = 7

for (let contador = 1; contador <= 9; contador ++){
	console.log(numero * contador);
}
------------------------------------------------
var listaDeNomes = ["Diogo", "Felipe", "Rodrigues", "Silva"];

for(var indice = 0; indice < listaDeNomes.length; indice++){	
}
