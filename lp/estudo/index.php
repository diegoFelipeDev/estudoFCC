<?php  echo"Hello Word";

//String


$mensagem = 'hello word';
	echo $mensagem;


//Operadores


$A = 2;
$B = 3;

$soma = $A + $B;
	print $soma; 


//Estruturas condicionais


$A = 5;
$B = 2;

if ($B % 2 == 1){
	echo 'Número Ímpar';
}

else{
	echo 'Número Par';
}


//Laços de repetição

#while

echo"while";
$i = 0;
while ($i<10){
	echo $i;
	$i++;
}

#do...while

echo'<br>do...while: ';

$i = 0;
do{
	echo $i;
	$i++;
} while ($i < 10 )

#for

echo '<br>for: ';

for($i = 0;$i < 10; $i++){
	echo $i;
}

#foreach

echo '<br>foreach: ';

$i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
foreach ($i as $j){
	echo $j;
}


//ARRAYS

<?php

$variavel = array(1, 2, 3, 4, 5);
foreach ($variavel as $v){
	echo $v;
}

$variavel = array("A"=>"Abacaxi", "B"=>"Bola", "C"=> "Cachorro");

foreach($variavel as $v){
	echo $v;
}

$variavel = array("A"=>"Abacaxi", "B"=>"Bola", "C"=> "Cachorro");
echo $variavel[B];

$variavel = array("Abacaxi", "Bola",  "Cachorro");
echo $variavel[1];
