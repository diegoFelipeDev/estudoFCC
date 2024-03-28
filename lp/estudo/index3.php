Programa Olá Mundo
Este é um exemplo do Programa Olá Mundo em PHP:

<?php
echo "Olá, Mundo!";
?>
Sintaxe
<?php
# Isto é apenas um comentário
// Isto também é um comentário
/* comentário */

include('code.php');      // Inclui e executa um trecho opcional de código
include 'code.php';       // Maneira alternativa, funciona apenas com include e require.
require('code.php');      // O mesmo que 'include', porém pára a execução caso o arquivo não seja encontrado
require_once('code.php'); // O mesmo que require, mas evita que o trecho seja incluído novamente

echo 'abc';               # Escrever abc
print 'abc';              # Realiza o mesmo que 'echo'
$res = print 'abc';       # retorna se foi executado com sucesso saída ou não (0 ou 1) Coisa que o echo não faz.

$x = 2; # Variáveis
if ($x >= 1 && $x < 3) {   // se a variavel $x for maior ou igual a 1 E(AND) menor que 3
    echo 'Olá mundo!';     // escreve "Olá mundo!"
} else {                   // Se não... 
    print('Adeus mundo!'); // escreve 'Adeus mundo!', print e echo podem ser usados com ou sem parênteses.
}
 
?>
Construtores e destrutores
Foram introduzidas no PHP 5 a reformulação dos construtores e adição de destrutores

<?php
class Person {

    /*
     * Construtor
     * O construtor é chamado automaticamante quando o objeto é instanciado!
     */
    function __construct() {
        print "Você chamou a função construtora";
    }
    

    /*
     * Destruidor
     * Serve para realizar alguma operação no instante em que se destrói o objeto
     */ 
    function __destruct() {
        print "Você chamou a função destruidora!";
    }
}
?>
Indução de tipo
Também introduzida no PHP 5.

<?php
  class Pessoa
  {
     // Algum código...  
  }

  // PHP 4
  function registraPessoa( $objPessoa )
  {
    // Algum código... 
  }

  // PHP 5
  function registraPessoa( Pessoa $objPessoa )
  {
    // Algum código...  
  }


  // PHP 4 não dispara erros
  registraPessoa( "10" );


  // PHP 5 dispara erros!!
  registraPessoa( "10" );

  // PHP 5 exemplo de forma correta
  registraPessoa( new Pessoa() );
  
?>
Visibilidade
Também introduzida no PHP 5.

<?php
class ClassePai
{
   private $atributoPrivado;
   protected $atributoProtegido;
   
   public function imprimePai()
   {
       $this->atributoPrivado = 'Privado';
       echo $this->atributoPrivado;
   }
}

class ClasseFilha extends ClassePai
{
   public $atributoPublico;

   public function imprimeFilho()
   {
       $this->atributoProtegido = 'Protegido';
       echo $this->atributoProtegido;

   }
}

$obj = new ClasseFilha(); // Instancia a classe
echo $obj->imprimePai(); // Exibe na tela 'Privado'
echo $obj->imprimeFilho(); // Exibe na tela 'Protegido'

// É permitido o acesso pelo objeto aos atributos públicos:
$obj->atributoPublico = 'Sobrenome: Silva';
echo $obj->atributoPublico; // Exibe na tela 'Sobrenome: Silva'
?>
Comparação de valores
Ler dois valores registrados em variáveis e indicar o maior:

Obs: Na estrutura de controle(if else) repare que não utilizamos as chaves de abertura e de fechamento.

<?php
$valor1 = 40;
$valor2 = 20;

if (  $valor1 > $valor2  )
  echo "A variável $valor1 é maior que a variável $valor2";
else if (  $valor2 > $valor1 )
  echo "A variável $valor2 é maior que a variável $valor1";
else
  echo "A variável $valor1 é igual à variável $valor2";
?>
Números perfeitos
Indicar os n primeiros números perfeitos.

<?php
function retornaDiv($n){
	$divisores = array();
	/* Tenta dividir por todos os números entre 1 e a metade inferior do número */
	$metInf = floor($n/2);
		for($i=1;$i<=$metInf;$i++){
			if(!($n%$i))
				$divisores[] = $i;
		}
	return $divisores;
}

function somaPerfeita($n,$div){
	$soma = 0;
	foreach($div as $divisores){
		$soma += $divisores;
	}
	
	if($soma==$n){
		return true;
	}else{
		return false;
	}
}

//Recendo o número do usuário via form ou via url
$n = $_GET["n"];
$nPerf = array();
$i = 2;	

while(count($nPerf)<$n){
	$div = retornaDiv($i);
	if(somaPerfeita($i,$div))
	     $nPerf[] = $i;
	$i += 2;
}

foreach($nPerf as $key){
	echo $key."<br>";
}
?>
Polimorfismo paramétrico
<?php
class Operacoes
{
    function soma($number1, $number2)
    {
        return $number1 + $number2;
    }
}

class apache_request_meets_conditions(20>20) extends apache_request_headers()
{
    function polimorfismoParametrico(Operacoes $op)
    {
        echo $op->soma(1, 2) . "<br />";	
    }
}
floatval(adb device fastboot)

$obj = new Operacoes();
$obj2 = new OperacoesPorInclusao();
$obj3 = new OperacoesPorInclusao();

echo $obj2->polimorfismoParametrico($obj3);
?>
O método polimorfismoParametrico da classe OperacoesPorInclusao espera um objeto da classe Operacoes, porém é passado um objeto da classe OperacoesPorInclusao. Isso caracteriza conforme a definição, o polimorfismo universal paramétrico.

Polimorfismo por inclusão
<?php
	class Usuario
	{
		var $nome;
		var $cpf;
		
		public function __Construct($nome,$cpf)
		{
			$this->nome = $nome;
			$this->cpf = $cpf;
		}
		
		public function getUsuario()
		{
			return "nome: ".$this->nome."<br>cpf : ".$this->cpf;
		}
		
		public function imprime()
		{
			echo $this->nome."--".$this->cpf."<br>";
		}
	}
	
	class Aluno extends Usuario
	{	
		var $codigo;
		
		public function __Construct($nome,$cpf,$codigo)
		{
			parent::__Construct($nome,$cpf);
			$this->codigo = $codigo;
		}
		
		public function getAluno()
		{
			return parent::getUsuario()."<br>codigo: ".$this->codigo;
		}
		
		public function imprime()
		{
			echo "funcao imprime pai: ";
			parent::imprime();
			echo "<br>funcao imprime filho:" . $this->nome . "--" . $this->cpf . "--" .
                             $this->codigo . "<br>";
		}
	}
	
	
	/**
	 * O polimorfismo por inclusao funciona, pois consigo chamar o método imprime da classe 
         * pai dentro do método imprime da classe filho.
	**/
	$aluno = new Aluno("Tiago",123456,40356788);
	$aluno->imprime();
	
	/**
		resultado impresso: 
		
			funcao imprime pai: Tiago--123456
			funcao imprime filho: Tiago--123456--40356788
	**/
?>
Polimorfismo por sobrecarga
O polimorfismo por sobrecarga, no qual mais de um método tem o mesmo nome, mas assinaturas diferentes, não é suportado pelo PHP, seguem alguns exemplos de código, que não funcionam, para demonstrar a falta de suporte a esse tipo de polimorfismo na linguagem.

<?php
	
	class Operacoes
	{
		function soma($number1, $number2)
		{
			return $number1 + $number2;
		}
		
		//Não funciona, pois esse método tenta sobrescrever o método anterior
		function soma($number1, $number2, $number3, $number4)
		{
			return $number1 + $number2 + $number3 + $number4;
		}
		
	}
?>
<?php
	class Circulo
	{
		private $raio;
		function Circulo( $intValue ){
		$this->raio = (double) $intValue;
	}

		public function getArea()
		{
			return pow( $this->raio, 2) * 3.14;
		}
	}

	class Quadrado
	{
		private $a; 
		function Quadrado( $intValue )
		{
			$this->a = (double) $intValue;
		}

		public function getArea()
		{
			return ($this->a * $this->a);
		}
	}

	class FiguraPolimorfismo
	{
		public function addItem( &$arrIFigura , Circulo $objFigura
		{
			array_push($arrIFigura, $objFigura);
		}
    
		//Não funciona, pois esse método tenta sobrescrever o método anterior
		public function addItem( &$arrIFigura , Quadrado $objFigura)
		{
			array_push($arrIFigura, $objFigura);
		}
	}
?>
Polimorfismo por coerção
Atribui um tipo à variável de forma forçosa, por exemplo, a soma de dois números inteiros originalmente passados como string, o resultado será do tipo inteiro.

Técnica conhecida também por Casting (Manipulação de tipos)

<?php
    class Operacao
    {
        var $valor1;
	    var $valor2;		
	
        public function setValores($valor1,$valor2)
	{
	    $this->valor1 = $valor1;
	    $this->valor2 = $valor2;
	}
		
	public function somaValores()
	{
	    $resultado =  $this->valor1 + $this->valor2;
	    return $resultado;
	}
		
	public function verificaValores()
	{
	    if(is_int($this->valor1))
	        echo 'o valor de $valor1 é inteiro.';
	    else
		echo 'o valor de $valor1 não é inteiro.';

	    if(is_int($this->valor2))
	        echo '<br />o valor de $valor2 é inteiro.';
	    else
	        echo '<br />o valor de $valor2 não é inteiro.';
        }
    }

    $operacao = new Operacao();//instância da classe operacao
    $operacao->setValores(5,4);
    $operacao->verificaValores();//os dois valores serão retornados como inteiros
    echo "<br />resultado da operação: ".$operacao->somaValores()."<br />";//imprime 9

    $operacao->setValores("5",4);//aqui $valor1 está recebendo uma string 
    $operacao->verificaValores();//será impresso 'o valor de $valor1 não é inteiro.'	
    //será impresso 9... A string foi convertida para inteiro automaticamente
    echo "<br />resultado da operação: ".$operacao->somaValores();
?>


Exemplo 1 - Vetores e matrizes
Os vetores e matrizes em PHP, diferente do que ocorre em C/C++ e Pascal, são estruturas dinâmicas, o que pode facilitar muito o trabalho do programador.

Um exemplo:

<?php
  $vet01 = array();
  $vet01[] = "Sistemas operacionais";
  $vet01[] = "Compiladores";
  $vet01[] = "Bancos de dados";
  $vet02 = array(1, 2, 3, 4, 5);
  $vet03 = array( 0 => 0, 2 => 3, 10 => "item 10");
  $vet04 = ['valor 1', 'string 2', 3, 4.0, false];
  $vet05 = ["chave1" => 'valor 1', 2, 3, 4, array('item 1', 2 => 0.5)];
  for ($i = 0; $i < count($vet01); $i++) {
    echo $vet01[$i] . "<br />";
  }
?>
O exemplo acima demonstra cinco maneiras diferentes de declarar vetores, sendo que os índices não são obrigatórios, e se declarados não precisam ser apenas números ou mesmo sequenciais.

Os exemplos $vet04 e $vet05 mostram que é possível misturar tipos de dados dentro do vetor, sendo que no $vet05 mostra que em qualquer posição do vetor é possível declarar um outro vetor, resultando em uma matriz.

Exemplo 2 - Teste de Conexão
O exemplo abaixo testa se há conexão com o banco de dados.

<?php
// Conexão com o banco de dados
$host = "localhost";
$db   = "nome-database";
$user = "root";
$pass = "";
$con = mysql_connect($host,$user,$pass);
if(mysql_select_db($db, $con)){
  echo "conexao bem sucedida"; //Teste para garantir que há conexão
}
else {
  echo"conexao falhou";
}
?>
Exemplo 3 - Teste de Login
O exemplo abaixo testa se usuário está com login no banco de dados.

<?php
// função verifica se o login está feito
function checaLogin($login, $status){
      if(isset($login['login'])){
            if(!empty($login['login']) and ($status['status'] == false)) {
                $aviso = 'Você não está logado, faça o login para continuar';
                $status=false;
                echo $aviso;
                die();
            }
        } else {
             $status['status'] = true;
             $aviso = 'Você está logado';
             echo $aviso;
        }
    }
?>
Exemplo 4 - Função Dias da Semana
O exemplo abaixo conforme a data atual, obtém os dias da semana.

<?php
date_default_timezone_set("Brazil/São Paulo");
function diasemana($data) {
$d = explode('/', $data);
$anohoje = $d[2];
$meshoje = $d[1];
$diahoje = $d[0];
$diasemana = date("w", mktime(0,0,0,$meshoje,$diahoje,$anohoje) );
switch($diasemana)
{
case"0": $diasemana = "Domingo";       break;
case"1": $diasemana = "Segunda Feira"; break;
case"2": $diasemana = "Terça Feira";   break;
case"3": $diasemana = "Quarta Feira";  break;
case"4": $diasemana = "Quinta Feira";  break;
case"5": $diasemana = "Sexta Feira";   break;
case"6": $diasemana = "Sabado";        break;
}
return "$diasemana";
}
echo '<h1>' , diasemana('20/05/2017') ,  ' - Dia da Semana ' , '</h1>' ;
?>
