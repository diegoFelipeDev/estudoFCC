O Python é uma linguagem de programação de propósito geral que é dinamicamente tipada, interpretada e conhecida por sua fácil leitura com ótimos princípios de design.

O freeCodeCamp tem um dos cursos mais populares sobre Python. É totalmente gratuito. Você pode assisti-lo no YouTube aqui.

Algumas informações gerais sobre números de ponto flutuante e como eles funcionam em Python podem ser encontradas aqui.

Quase todas as implementações do Python seguem a especificação IEEE 754: Standard for Binary Floating-Point Arithmetic. Mais informações podem ser encontradas no site do IEEE (texto em inglês).

Objetos float podem ser criados usando literais de ponto flutuante:

>>> 3.14
3.14
>>> 314.   # Zeros à direita não são necessários.
314.0
>>> .314    # Zeros à esquerda não são necessários.
0.314
>>> 3e0
3.0
>>> 3E0     # 'e' ou 'E' podem ser usados.
3.0
>>> 3e1     # Um valor positivo após o 'e' move o decimal para a direita.
30.0
>>> 3e-1    # Um valor negativo após o 'e' move o decimal para a esquerda.
0.3
>>> 3.14e+2 # O sinal de '+' não é necessário, mas pode ser usado para a parte exponencial.
314.0
Literais numéricos não contêm um sinal. No entanto, a criação de objetos float negativos é possível prefixando com um operador unário - (sinal de menos) sem espaço antes do literal:

>>> -3.141592653589793
-3.141592653589793
>>> type(-3.141592653589793)
<class 'float'>
Da mesma forma, objetos float positivos podem ser prefixados com um operador unário + (mais) sem espaço antes do literal. Normalmente, o sinal de + é omitido:

>>> +3.141592653589793
3.141592653589793
Observe que zeros à esquerda e à direita são válidos para literais de ponto flutuante.

>>> 0.0
0.0
>>> 00.00
0.0
>>> 00100.00100
100.001
>>> 001e0010      # O mesmo que 1e10
10000000000.0
O construtor float é outra maneira de criar objetos float.

A criação de objetos float com literais de ponto flutuante é preferível quando possível:

>>> a = 3.14         # Prefira o literal de ponto flutuante quando possível.
>>> type(a)
<class 'float'>
>>> b = int(3.14)    # Funciona, mas é desnecessário.
>>> type(b)
<class 'float'>
No entanto, o construtor float permite criar objetos float de outros tipos de números:

>>> a = 4
>>> type(a)
<class 'int'>
>>> print(a)
4
>>> b = float(4)
>>> type(b)
<class 'float'>
>>> print(b)
4.0
>>> float(400000000000000000000000000000000)
4e+32
>>> float(.00000000000000000000000000000004)
4e-32
>>> float(True)
1.0
>>> float(False)
0.0
O construtor float também fará objetos float a partir de strings que representam literais numéricos:

>>> float('1')
1.0
>>> float('.1')
0.1
>>> float('3.')
3.0
>>> float('1e-3')
0.001
>>> float('3.14')
3.14
>>> float('-.15e-2')
-0.0015
O construtor float também pode ser usado para fazer representações numéricas de NaN (Not a Number – em português, não é um número), infinity negativo e infinity positivo (observe que as strings para estes não diferenciam maiúsculas de minúsculas):

>>> float('nan')
nan
>>> float('inf')
inf
>>> float('-inf')
-inf
>>> float('infinity')
inf
>>> float('-infinity')
-inf
Números complexos
Os números complexos têm uma parte real e uma parte imaginária, cada uma representada por um número de ponto flutuante.

A parte imaginária de um número complexo pode ser criada usando um literal imaginário, isso resulta em um número complexo com uma parte real de 0.0:

>>> a = 3.5j
>>> type(a)
<class 'complex'>
>>> print(a)
3.5j
>>> a.real
0.0
>>> a.imag
3.5
Não existe literal para criar um número complexo com partes reais e imaginárias diferentes de zero. Para criar um número complexo de parte real diferente de zero, adicione um literal imaginário a um número de ponto flutuante:

>>> a = 1.1 + 3.5j
>>> type(a)
<class 'complex'>
>>> print(a)
(1.1+3.5j)
>>> a.real
1.1
>>> a.imag
3.5
Ou use o construtor complex.

class complex([real[, imag]])
Os argumentos usados para chamar o construtor complex podem ser de tipo numérico (incluindo complex) para qualquer parâmetro:

>>> complex(1, 1)
(1+1j)
>>> complex(1j, 1j)
(-1+1j)
>>> complex(1.1, 3.5)
(1.1+3.5j)
>>> complex(1.1)
(1.1+0j)
>>> complex(0, 3.5)
3.5j
Uma string também pode ser usada como argumento. Nenhum segundo argumento é permitido se uma string for usada como argumento

>>> complex("1.1+3.5j")
(1.1+3.5j)
bool() é uma função embutida no Python 3. Essa função retorna um valor Booleano, ou seja, True ou False.

Argumentos
Ela aceita um argumento, x. x é convertido usando o Teste do valor verdade.

Valor de retorno
Se x for falso ou omitido, retorna False; do contrário, retorna True.

Exemplo de código
print(bool(4 > 2)) # Retorna True, pois 4 é maior que 2
print(bool(4 < 2)) # Retorna False, pois 4 não é menor que 2
print(bool(4 == 4)) # Retorna True, pois 4 é igual a 4
print(bool(4 != 4)) # Retorna False, pois 4 é igual a 4 e, portanto, não há desigualdade
print(bool(4)) # Retorna True, pois 4 é um valor diferente de zero
print(bool(-4)) # Retorna True, pois -4 é um valor diferente de zero
print(bool(0)) # Retorna False, pois ele é um valor diferente de zero
print(bool('dskl')) # Retorna True, pois a string é um valor diferente de zero
print(bool([1, 2, 3])) # Retorna True, pois a lista é um valor diferente de zero
print(bool((2,3,4))) # Retorna True, pois a tupla é um valor diferente de zero
print(bool([])) # Retorna False, pois a lista está vazia e é igual a 0, conforme o teste do valor verdade
and, or e not

Documentação do python – Operações booleanas

Estas são as operações booleanas, ordenadas por prioridade crescente:

OPERAÇÃO	RESULTADO
x ou y	se x for falso, então y, senão x (1)
x e y	se x for falso, então x, senão y (2)
não x	se x for falso, então True, senão False (3)
Observações:

Este é um operador de curto-circuito, portanto, ele só avalia o segundo argumento se o primeiro for False.
2. Este é um operador de curto-circuito, portanto, ele só avalia o segundo argumento se o primeiro for True.

3. not tem prioridade mais baixa do que os operadores não booleanos. Portanto, not a == b é interpretado como not (a == b) e a == not b é um erro de sintaxe.

Exemplos:
not:
>>> not True
False
>>> not False
True
and:
>>> True and False    # Curto-circuito no primeiro argumento.
False
>>> False and True    # O segundo argumento é avaliado.
False
>>> True and True     # O segundo argumento é avaliado.
True
or:
>>> True or False    # Curto-circuito no primeiro argumento.
True
>>> False or True    # Segundo argumento é avaliado.
True
>>> False or False   # Segundo argumento é avaliado.
False
Três constantes embutidas comumente usadas:

True: o valor verdadeiro do tipo bool. Atribuições a True levantam a exceção SyntaxError.
False: o valor falso do tipo bool. Atribuições para False levantam SyntaxError.
None: o único valor do tipo NoneType. O None é frequentemente usado para representar a ausência de um valor, como quando os argumentos padrão não são passados para uma função. Atribuições a None levantam SyntaxError.
Outras constantes embutidas:

NotImplemented: valor especial que deve ser retornado pelos métodos especiais binários, como __eg__(), __add__(), __rsub__() etc.) para indicar que a operação não foi implementada em relação ao outro tipo.
Ellipsis: valor especial usado principalmente em conjunto com a sintaxe de fatiamento estendida para tipos de dados de contêiner definidos pelo usuário.
__debug__: verdadeiro se o Python não tiver sido iniciado com uma opção -o.
Constantes adicionadas pelo módulo site. O módulo site (que é importado automaticamente durante a inicialização, exceto se a opção de linha de comando -S for fornecida) adiciona várias constantes ao espaço de nomes interno. Elas são úteis para o shell do interpretador interativo e não devem ser usadas em programas.

Objetos que, quando exibidos, exibem uma mensagem como "Use quit() or Ctrl-D (i.e. EOF) to exit" e, quando chamados, levantam SystemExit com o código de saída especificado:

quit(code=None)
exit(code=None)
Objetos que, quando exibidos, exibem uma mensagem como "Type license() to see the full license text" e , quando chamados, exibem o texto correspondente em forma de paginador (uma tela de cada vez):

copyright
license
credits
Uma instrução de definição de função não executa a função. A execução (chamada) de uma função é feita usando o nome da função seguido por parênteses entre os argumentos necessários (se houver).

>>> def say_hello():
...     print('Olá')
...
>>> say_hello()
Olá
A execução de uma função introduz uma nova tabela de símbolos usada para as variáveis locais da função. Mais precisamente, todas as atribuições de variáveis em uma função armazenam o valor na tabela de símbolos local.

Por outro lado, as referências de variáveis primeiro procuram na tabela de símbolos local, depois nas tabelas de símbolos locais das funções delimitadoras, depois na tabela de símbolos globais e, finalmente, na tabela de nomes embutidos. Assim, variáveis globais não podem receber diretamente um valor dentro de uma função (a menos que sejam nomeadas em uma instrução global), embora possam ser referenciadas.

>>> a = 1
>>> b = 10
>>> def fn():
...     print(a)    # "a" local não foi atribuído, sem função de fechamento, "a" global referenciado.
...     b = 20      # "b" local foi atribuído na tabela de símbolos locais da função.
...     print(b)    # "b" local é referenciado.
...
>>> fn()
1
20
>>> b               # "b" global não foi alterado pela chamada da função.
10
Os parâmetros (argumentos) reais para uma chamada de função são introduzidos na tabela de símbolos local da função chamada quando ela é chamada. Desse modo, os argumentos são passados usando a chamada pelo valor (onde o valor é sempre uma referência de objeto, não o valor do objeto). Quando uma função chama outra função, uma nova tabela de símbolos local é criada para essa chamada.

>>> def cumprimentar(s):
...     s = "Olá, " + s    # s na tabela de símbolos local é reatribuída.
...     print(s)
...
>>> pessoa = "João"
>>> cumprimentar(pessoa)
Olá, João
>>> pessoa # pessoa usado para chamar continua vinculado ao objeto original, ou seja, 'João'.
'João'
Os argumentos usados para chamar uma função não podem ser reatribuídos pela função, mas os argumentos que fazem referência a objetos mutáveis podem ter seus valores alterados:

>>> def fn(arg):
...     arg.append(1)
...
>>> a = [1, 2, 3]
>>> fn(a)
>>> a
[1, 2, 3, 1]
As classes fornecem um meio de agrupar dados e funcionalidades. A criação de uma nova classe cria um outro tipo de objeto, permitindo que novas instâncias desse tipo sejam feitas. Cada instância de classe pode ter atributos anexados a ela para manter seu estado. As instâncias de classe também podem ter métodos (definidos por sua classe) para modificar seu estado.

Comparado com outras linguagens de programação, o mecanismo de classe do Python adiciona classes com um mínimo de nova sintaxe e semântica. É uma mistura dos mecanismos de classe encontrados no C++.

As classes do Python fornecem todos os recursos padrão da Programação Orientada a Objetos: o mecanismo de herança de classe permite várias classes base, uma classe derivada pode substituir qualquer método de sua classe ou classes base e um método pode chamar o método de uma classe base com o mesmo nome.

Os objetos podem conter quantidades e tipos de dados arbitrários. Como acontece com os módulos, as classes participam da natureza dinâmica do Python: elas são criadas em tempo de execução e podem ser modificadas ainda mais após a criação.

Sintaxe de definição de classe:
A forma mais simples da definição de classe tem esta aparência:

class NomeClasse:
    <instrução-1>
        ...
        ...
        ...
    <instrução-N>
Objetos de classe:
Objetos de classe oferecem suporte a dois tipos de operações: referências de atributo e instanciação.

As referências de atributo usam a sintaxe padrão usada para todas as referências de atributo em Python: obj.name. Os nomes de atributos válidos são todos os nomes que estavam no espaço de nomes da classe quando o objeto de classe foi criado. Então, se a definição da classe ficou assim:

class MinhaClasse:
    """ Um exemplo de classe simples """
    i = 12345

    def f(self):
        return 'olá, mundo'
Então MinhaClasse.i e MinhaClasse.f são referências de atributo válidas, retornando um inteiro e um objeto de função, respectivamente. Atributos de classe também podem ser atribuídos, para que você possa alterar o valor de MyClass.i por atribuição. __doc__ também é um atributo válido, retornando a docstring pertencente à classe: "Um exemplo de classe simples".

A instanciação de classe usa notação de função. Apenas finja que o objeto de classe é uma função sem parâmetros que retorna uma nova instância da classe. Por exemplo (assumindo a classe acima):

x = MinhaClasse()
Cria uma instância da classe e atribui esse objeto à variável local x.

A operação de instanciação ("chamar" um objeto de classe) cria um objeto vazio. Muitas classes gostam de criar objetos com instâncias personalizadas para um estado inicial específico. Portanto, uma classe pode definir um método especial, chamado init(), assim:

def __init__(self):
    self.data = []
Quando uma classe define um método __init__(), a instanciação de classe invoca automaticamente __init__() para a instância de classe recém-criada. Portanto, nesse exemplo, uma nova instância inicializada pode ser obtida por:

x = MinhaClasse()
Claro, o método __init__() pode ter argumentos para maior flexibilidade. Nesse caso, os argumentos fornecidos ao operador de instanciação de classe são passados para __init__(). Por exemplo:

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
              ...

x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
Geralmente, é uma boa prática não misturar tabulações e espaços ao codificar em Python. Fazer isso pode causar um TabError e seu programa travará. Seja consistente ao codificar – opte por recuar usando tabulações ou espaços e siga a convenção escolhida em todo o programa.

Blocos de código e indentação
Uma das características mais distintivas do Python é o uso de indentação para marcar blocos de código. Considere a instrução if do nosso programa simples de verificação de senha:

if pwd == 'maçã':
    print('Iniciando sessão ...')
else:
    print('Senha incorreta.')

print('Tudo pronto!')
As linhas print('Iniciando sessão…') e print('Senha incorreta.') são dois blocos de código separados. Eles têm apenas uma única linha, mas o Python permite que você escreva blocos de código que consistam em um número qualquer de instruções.

Para indicar um bloco de código em Python, você deve indentar cada linha do bloco na mesma quantidade. Os dois blocos de código em nossa instrução if de exemplo são ambos recuados com quatro espaços, que é uma quantidade típica de indentação do Python.

Na maioria das outras linguagens de programação, a indentação é usada apenas para ajudar a deixar o código bonito. No Python, contudo, ela é necessária para indicar a qual bloco de código uma instrução pertence. Por exemplo, o print('Tudo pronto!') final não é indentado e, portanto, não faz parte do bloco else.

Programadores familiarizados com outras linguagens muitas vezes se irritam com o pensamento de que a indentação é importante: muitos programadores gostam da liberdade de formatar seu código como quiserem. No entanto, as regras de indentação do Python são bastante simples, e a maioria dos programadores já usa a indentação para tornar seu código legível. Python simplesmente leva essa ideia um passo adiante e dá significado à indentação.

Instruções if/elif
Uma instrução if/elif é uma instrução if generalizada com mais de uma condição. É usada para tomar decisões complexas. Por exemplo, suponha que uma companhia aérea tenha as seguintes tarifas de passagens para "crianças": crianças de 2 anos ou menos voam de graça, crianças com mais de 2 anos e menores de 13 anos pagam uma tarifa de criança com desconto e qualquer pessoa com 13 anos ou mais paga uma tarifa normal de adulto. O programa a seguir determina quanto um passageiro deve pagar:

# tarifaAerea.py
idade = int(input('Quantos anos você tem? '))
if idade <= 2:
    print(' grátis')
elif 2 < idade < 13:
    print(' tarifa de criança')
else:
    print(' tarifa de adulto')
Depois que o Python obtém a idade do usuário, ele insere a instrução if/elif e verifica cada condição uma após a outra na ordem em que são fornecidas.

Então, primeiro ele verifica se a idade é menor que 2 e, em caso positivo, indica que o voo está livre e salta da condição elif. Se a idade não for menor que 2, então ele verifica a próxima condição elif para ver se idade está entre 2 e 13. Em caso afirmativo, ele imprime a mensagem apropriada e salta para fora da instrução if/elif. Se nem a condição if nem a condição elif forem True, ele executa o código no bloco else.

Expressões condicionais
Python tem mais um operador lógico do qual alguns programadores gostam (e outros não!). É essencialmente uma notação abreviada para instruções if que podem ser usadas diretamente dentro de expressões. Considere este código:

food = input("Qual é a sua comida favorita? ")
reply = 'eca' if food == 'cordeiro' else 'delícia'
A expressão no lado direito de = na segunda linha é chamada de expressão condicional e é avaliada como 'eca' ou 'delícia'. É equivalente ao seguinte:

food = input("Qual é a sua comida favorita? ")
if food == 'cordeiro':
   reply = 'eca'
else:
   reply = 'delícia'
As expressões condicionais são geralmente mais curtas do que as instruções if/else correspondentes, embora não sejam tão flexíveis ou fáceis de ler. Em geral, você deve usá-las quando elas tornarem seu código mais simples.

Exemplo de operador de comparação do Python
Há oito operações de comparação em Python. Todas elas têm a mesma prioridade (que é maior que a das operações booleanas). As comparações podem ser encadeadas arbitrariamente; por exemplo, x < y <= z é equivalente a x < y and y <= z, exceto que y é avaliado apenas uma vez (mas, em ambos os casos, z não é avaliado quando x < y é considerado falso).

A seguir, um resumo as operações de comparação:

OPERAÇÃO	SIGNIFICADO
<	estritamente menor que
<=	menor ou igual a
>	estritamente maior que
>=	maiorque ou igual a
==	igual a
!=	diferente de
is	identidade do objeto
is not	identidade do objeto negada
Objetos de tipos diferentes, exceto tipos numéricos diferentes, nunca se comparam iguais. Além disso, alguns tipos (por exemplo, objetos de função) oferecem suporte a apenas uma noção um tanto distorcida de comparação onde dois objetos quaisquer desse tipo são desiguais. Os operadores <, <=, > e >= vão levantar uma exceção TypeError ao comparar um número complexo com outro tipo numérico embutido, quando os objetos são de tipos diferentes que não podem ser comparados, ou em outros casos onde não há ordem definida.

Instâncias não idênticas de uma classe normalmente são comparadas como diferentes, a menos que a classe defina o método __eq__().

As instâncias de uma classe não podem ser ordenadas em relação a outras instâncias da mesma classe, ou outros tipos de objeto, a menos que a classe defina os métodos __lt__(), __le__(), __gt__() e __ge__() suficientemente (em geral , __lt__() e __eq__() são suficientes se você quiser os significados convencionais dos operadores de comparação).

O comportamento dos operadores is e is not não pode ser personalizado; eles também podem ser aplicados a dois objetos quaisquer e nunca levantarão uma exceção.

Também podemos encadear operadores < e >. Por exemplo, 3 < 4 < 5 retornará True, mas 3 < 4 > 5 não. Também podemos encadear o operador de igualdade. Por exemplo, 3 == 3 < 5 retornará True, mas 3 == 5 < 5 não.

Comparações de igualdade – "is" x "=="
Em Python, existem dois operadores de comparação que nos permitem verificar se dois objetos são iguais. O operador is e o operador ==. No entanto, há uma diferença fundamental entre eles!

A principal diferença entre "is" e "==" pode ser resumida como:

is é usado para comparar identidade
== é usado para comparar igualdade
Exemplo
Primeiro, crie uma lista no Python.

minhaListaA = [1,2,3]
Em seguida, crie uma cópia dessa lista.

minhaListaB = minhaListaA
Se nós usarmos o operador "==" ou o operador "is", ambos vão resultar na saída True.

>>> minhaListaA == minhaListaB # as duas listas contêm elementos similares
True
>>> minhaListaB is minhaListaA # myListB contém os mesmos elementos
True
Isso ocorre porque minhaListaA e minhaListaB estão apontando para a mesma variável de lista, que definimos no início do programa em Python. Ambas as listas são exatamente iguais, tanto em identidade quanto em conteúdo.

No entanto, e se eu agora criar uma nova lista?

minhaListaC = [1,2,3]
Executar o operador == ainda mostra que as duas listas são iguais, em termos de conteúdo.

>>> minhaListaA == minhaListaC
True
Porém, ao executar o operador is, agora teremos uma saída False. Isso ocorre porque minhaListaA e minhaListaC são duas variáveis diferentes, apesar de conterem os mesmos dados. Apesar de parecerem iguais, são diferentes.

>>> minhaListaA is minhaListaC
False # as listas têm referências diferentes
Para resumir:

Uma expressão is retorna True se ambas variáveis estão apontando para a mesma referência
Uma expressão == retorna True se ambas variáveis contêm os mesmos dados
Dicionários
Um dicionário (também conhecido como "dict") no Python é um tipo de dados embutido que pode ser usado para armazenar pares chave-valor. Isso permite que você trate um dict como se fosse um banco de dados para armazenar e organizar dados.

O que há de especial sobre dicionários é o modo como eles são implementados. A estrutura semelhante a uma tabela de hash facilita a verificação da existência – o que significa que podemos determinar facilmente se uma chave específica está presente no dicionário sem precisar examinar todos os elementos. O interpretador Python pode simplesmente ir para a chave de localização e verificar se a chave está lá.

Os dicionários podem usar quase todos os tipos de dados arbitrários, como strings, inteiros, etc., como chaves. No entanto, valores que não são hasheáveis, ou seja, valores contendo listas, dicionários ou outros tipos mutáveis (que são comparados por valor e não por identidade de objeto) não podem ser usados como chaves. Os tipos numéricos usados para chaves obedecem às regras normais para comparação numérica: se dois números são iguais (como 1 e 1.0), eles podem ser usados alternadamente para indexar a mesma entrada do dicionário. (Observe, no entanto, que, como os computadores armazenam números de ponto flutuante como aproximações, geralmente não é aconselhável usá-los como chaves de dicionário.)

Um dos requisitos mais importantes de um dicionário é que as chaves devem ser únicas.

Para criar um dicionário vazio, basta usar um par de chaves, { }:

    >>> times = {}
    >>> type(times)
    >>> <class 'dict'>
Para criar um dicionário não vazio com alguns valores iniciais, coloque uma lista separada por vírgulas de pares chave-valor:

    >>> times = {'barcelona': 1875, 'chelsea': 1910}
    >>> times
    {'barcelona': 1875, 'chelsea': 1910}
É fácil adicionar pares chave-valor a um dicionário existente:

    >>> times['santos'] = 1787
    >>> times
    {'chelsea': 1910, 'barcelona': 1875, 'santos': 1787} # Repare a ordem – os dicionários não estão ordenados !
    >>> # extraindo o valor – Só foneça a chave
    ...
    >>> times['barcelona']
    1875
O operador del é usado para excluir um par chave-valor do dict. Em cenários em que uma chave que já está em uso é novamente usada para armazenar valores, o valor antigo associado a essa chave é completamente perdido. Além disso, lembre-se de que é um erro extrair o valor usando uma chave inexistente.

    >>> del times['santos']
    >>> times
    {'chelsea': 1910, 'barcelona': 1875}
    >>> times['chelsea'] = 2017 # sobrescrevendo
    >>> times
    {'chelsea': 2017, 'barcelona': 1875}
A palavra-chave in pode ser usada para verificar se uma chave existe ou não no dicionário:

    >>> 'sanots' in times
    False    
    >>> 'barcelona' in times
    True
    >>> 'chelsea' not in times
    False
keys é um método embutido que pode ser usado para obter as chaves de um determinado dicionário. Para extrair as chaves presentes nele como listas:

    >>> nomes_de_clubes = list(times.keys())    
    >>> nomes_de_clubes
    ['chelsea', 'barcelona']
Outra maneira de criar um dicionário é usando o método dict():

    >>> jogadores = dict( [('messi','argentina'), ('ronaldo','portugal'), ('kaka','brasil')] ) # sequência de pares chave-valor é passada
    >>> jogadores
    {'ronaldo': 'portugal', 'kaka': 'brasil', 'messi': 'argentina'}
    >>> 
    >>> # se as chaves forem strings simples, é bem mais fácil especificar pares usando argumentos nomeados
    ...
    >>> dict( totti = 38, zidane = 43 )
    {'zidane': 43, 'totti': 38}
Compreensões de dicionário (ou dictionary comprehensions, em inglês) também podem ser usadas para criar dicionários a partir de expressões de chave e valor arbitrárias:

    >>> {x: x**2 for x in (2, 4, 6)}
    {2: 4, 4: 16, 6: 36}
Laços em dicionários
Para simplesmente fazer um laço sobre as chaves no dicionário, em vez de chaves e valores:

    >>> d = {'x': 1, 'y': 2, 'z': 3} 
    >>> for key in d:
    ...     print(key) # faz alguma coisa
    ...
    x
    y
    z
Para fazer um laço sobre a chave e o valor, você pode usar o seguinte:

Para o Python 2.x:

    >>> for key, item in d.iteritems():
    ...     print items
    ...
    1
    2
    3
Use items() para o Python 3.x:

    >>> for key, item in d.items():
    ...     print(key, items)
    ...
    x 1
    y 2
    z 3
No Python, tudo é objeto.

Objetos representam um agrupamento lógico de atributos. Atributos são dados e/ou funções. Quando um objeto é criado no Python, ele é criado com uma identidade, tipo e valor.

Em outras linguagens, primitivos são valores que não possuem propriedades (atributos). Por exemplo, em JavaScript  undefined, null, boolean, string, number e symbol (novos no ECMAScript 2015) são primitivos.

Em Python, não há primitivos. None, booleanos, strings, números e até funções são todos objetos, independentemente de como são criados.

Podemos demonstrar isso usando algumas funções embutidas:

id
type
dir
issubclass
As constantes embutidas None, True e False são objetos:

Testamos o objeto None aqui.

>>> id(None)
4550218168
>>> type(None)
<class 'NoneType'>
>>> dir(None)
[__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> issubclass(type(None), object)
True
Em seguida, inspecionamos True.

>>> id(True)
4550117616
>>> type(True)
<class 'bool'>
>>> dir(True)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> issubclass(type(True), object)
True
Vamos demonstrar também com o False!

>>> id(False)
4550117584
>>> type(False)
<class 'bool'>
>>> dir(False)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> issubclass(type(False), object)
True
Strings, mesmo quando criadas por literais de strings, também são objetos.

>>> id("Olá, campistas!")
4570186864
>>> type('Olá, campistas!')
<class 'str'>
>>> dir("Olá, campistas!")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> issubclass(type('Olá, campistas!'), object)
True
O mesmo ocorre com os números.

>>> id(42)
4550495728
>>> type(42)
<class 'int'>
>>> dir(42)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> issubclass(type(42), object)
True
Funções também são objetos
No Python, funções são primeiro objetos de classe.

Funções no Python também são objetos, criados com uma identidade, um tipo, e um valor. Elas também podem ser passados para outras funções:

>>> id(dir)
4568035688
>>> type(dir)
<class 'builtin_function_or_method'>
>>> dir(dir)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
>>> issubclass(type(dir), object)
True
Também é possível vincular funções a um nome e chamar a função vinculada usando esse nome:

>>> a = dir
>>> print(a)
<built-in function dir>
>>> a(a)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
Vinculação de nome e criação de apelido de funções
Quando você define uma função no Python, esse nome de função é introduzido na tabela de símbolos atual. O valor do nome da função tem, então, um tipo, que é reconhecido como uma função definida pelo usuário pelo interpretador:

>>> algo = 1
>>> type(algo)
<type 'int'>

>>> def algo():
...     pass
...
>>> type(algo)
<type 'function'>

>>> algo = []
>>> type(algo)
<type 'list'>
O valor da função pode então ser atribuído a outro nome. Após ter sido reatribuído, ele ainda pode ser usado como uma função. Use este método para renomear suas funções:

>>> def algo(n):
...     print(n)
...
>>> type(algo)
<type 'function'>

>>> a = algo
>>> a(100)
100
Tuplas
Uma tupla é uma sequência de objetos em Python. As tuplas são imutáveis, o que significa que não podem ser modificadas após a criação, ao contrário das listas.

Criação:

Uma tupla (tuple) vazia é criada usando um par de parênteses, ():

    >>> tupla_vazia = ()
    >>> print(tupla_vazia)
    ()
    >>> type(tupla_vazia)
    <class 'tuple'>
    >>> len(tupla_vazia)
    0
Uma tupla com elementos é criada separando os elementos com vírgulas (envolvê-los em parênteses, (), é opcional – com algumas exceções):

    >>> tupla_1 = 1, 2, 3       # Cria uma tupla sem parênteses.
    >>> print(tupla_1)
    (1, 2, 3)
    >>> type(tupla_1)
    <class 'tuple'>
    >>> len(tupla_1)
    3
    >>> tupla_2 = (1, 2, 3)     # Cria uma tupla com parênteses.
    >>> print(tupla_2)
    (1, 2, 3)
    >>> tupla_3 = 1, 2, 3,      # Uma vírgula à direita é opcional.
    >>> print(tupla_3)
    (1, 2, 3)
    >>> tupla_4 = (1, 2, 3,)    # Uma vírgula dentro dos parênteses também pe opcional.
    >>> print(tupla_4)
    (1, 2, 3)
Uma tupla com um único elemento deve ter a vírgula à direita (com ou sem os parênteses):

>>> nao_tupla = (2)    # Sem vírgula ao final, faz com que isso não seja tupla.
>>> print(nao_tupla)
2
>>> type(nao_tupla)
<class 'int'>
>>> uma_tupla = (2,)     # Tupla de um elemento. Requer vírgula à direita.
>>> print(uma_tupla)
(2,)
>>> type(uma_tupla)
<class 'tuple'>
>>> len(uma_tupla)
1
>>> tambem_tupla = 2,    # Parênteses omitidos. Requer vírgula à direita.
>>> print(tambem_tupla)
(2,)
>>> type(tambem_tupla)
<class 'tuple'>
Parênteses são necessários em casos de ambiguidade (se a tupla for parte de uma expressão maior).

Observe que, na verdade, é a vírgula que forma uma tupla, não os parênteses. Os parênteses são opcionais, exceto no caso de tupla vazia, ou quando são necessários para evitar ambiguidade sintática.

Por exemplo, f(a, b, c) é uma chamada de função com três argumentos, enquanto f((a, b, c)) é uma chamada de função com uma tupla de 3 como único argumento.

    >>> print(1,2,3,4,)          # Chama print com 4 argumentos: 1, 2, 3 e 4
    1 2 3 4
    >>> print((1,2,3,4,))        # Chama print com 1 argumento: (1, 2, 3, 4,)
    (1, 2, 3, 4)
    >>> 1, 2, 3 == (1, 2, 3)     # Equivalente a 1, 2, (3 == (1, 2, 3))
    (1, 2, False)
    >>> (1, 2, 3) == (1, 2, 3)   # Use parênteses quando houver ambiguidade.
    True
Uma tupla também pode ser criada com um construtor  tuple:

    >>> tupla_vazia = tuple()
    >>> print(tupla_vazia)
    ()
    >>> tupla_de_lista = tuple([1,2,3,4])
    >>> print(tupla_de_lista)
    (1, 2, 3, 4)
    >>> tupla_de_string = tuple("Olá, campistas!")
    >>> print(tupla_de_string)
    ('O', 'l', 'á', ',', ' ', 'c', 'a', 'm', 'p', 'i', 's', 't', 'a', 's', '!')
    >>> uma_tupla = 1, 2, 3
    >>> outra_tupla = tuple(uma_tupla)    # se o construtor é chamado com uma tupla para o iterável,
    >>> uma_tupla is outra_tupla          # o argumento da tupla é retornado.
    True
Acessando elementos de uma tupla:

Elementos das tuplas são acessados e indexados da mesma forma que as listas.

>>> minha_tupla = 1, 2, 9, 16, 25
>>> print(minha_tupla)
(1, 2, 9, 16, 25)
O índice começa em zero

    >>> minha_tupla[0]
    1
    >>> minha_tupla[1]
    2
    >>> minha_tupla[2]
    9
Índice invertido

    >>> minha_tupla[-1]
    25
    >>> minha_tupla[-2]
    16
Empacotamento e desempacotamento:

A instrução t = 12345, 54321, 'olá!' é um exemplo de empacotamento de tupla: os valores 12345, 54321 e 'olá!' são empacotados em uma tupla. A operação inversa também é possível:

    >>> x, y, z = t
Isso é chamado, apropriadamente, de desempacotamento de sequência e funciona para qualquer sequência do lado direito. O desempacotamento de sequência requer que haja tantas variáveis no lado esquerdo do sinal de igual quantos elementos na sequência. Observe que a atribuição múltipla é, na verdade, apenas uma combinação de empacotamento de tuplas e desempacotamento de sequência.

    >>> t = 1, 2, 3    # Empacotamento de tupla.
    >>> print(t)
    (1, 2, 3)
    >>> a, b, c = t    # Desempacotamento de sequência.
    >>> print(a)
    1
    >>> print(b)
    2
    >>> print(c)
    3
    >>> d, e, f = 4, 5, 6    # A atribuição múltipla combina empacotar e desempacotar.
    >>> print(d)
    4
    >>> print(e)
    5
    >>> print(f)
    6
    >>> a, b = 1, 2, 3       # A atribuição múltipla requer que cada variável (direita)
    tenha um elemento correspondente (esquerda).
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: too many values to unpack (expected 2)
Imutáveis:

Tuplas são contêineres imutáveis, garantindo que os objetos que elas contêm (sua sequência) não serão alterados. Isso não garante que os próprios objetos que elas contêm não serão alteráveis:

    >>> uma_lista = []
    >>> uma_tupla = (uma_lista,)    # Uma tupla (imutável) com um elemento lista (mutável).
    >>> print(uma_tupla)
    ([],)

    >>> uma_lista.append("Olá, campistas!")
    >>> print(uma_tupla)         # Elemento do imutável sofreu mutação.
    (['Olá, campistas!'],)
Usos:

As funções podem retornar apenas um único valor, no entanto, uma tupla heterogênea pode ser usada para retornar vários valores de uma função. Um exemplo é a função embutida enumerate, que retorna um iterável de tuplas heterogêneas:

    >>> cumprimentar = ["Olá", "campistas!"]
    >>> enumerador = enumerate(cumprimentar)
    >>> enumerador.next()
    >>> enumerador.__next__()
    (0, 'Olá')
    >>> enumerador.__next__()
    (1, 'campistas!')
O Python utiliza um laço for para iterar sobre uma lista de elementos. Isso é diferente do C ou do Java, que usam o laço for para alterar um valor em etapas e acessar algo como um array usando esse valor.

Os laços for iteram sobre estruturas de dados baseadas em coleção, como listas, tuplas e dicionários.

for valor in lista_de_valores:
  # use o valor dentro deste bloco
Em geral, você pode usar qualquer coisa como o valor do iterador, onde as entradas do iterável podem ser atribuídas. Por exemplo, você pode desempacotar tuplas de uma lista de tuplas:

lista_de_tuplas = [(1,2), (3,4)]

for a, b in lista_de_tuplas:
  print("a:", a, "b:", b)
Por outro lado, você pode fazer um laço sobre qualquer coisa que seja iterável. Você pode chamar uma função ou usar um literal de lista.

for pessoa in carregar_pessoas():
  print("O nome é:", pessoa.nome)
for caractere in ["P", "y", "t", "h", "o", "n"]:
  print("Me dê um '{}'!".format(caractere))
Algumas formas de uso dos laços for:

Iterar pela função range()

for i in range(10):
    print(i)
Em vez de ser uma função, range é, na verdade, um tipo de sequência imutável. A saída conterá resultados do limite inferior – ou seja, 0 (zero) – ao limite superior, – ou seja, 10 (dez), mas não incluindo o 10. Por padrão, o limite inferior ou o índice inicial é definido como zero. Resultado:

>
0
1
2
3
4
5
6
7
8
9
>
Além disso, pode-se especificar o limite inferior da sequência e até mesmo o passo da sequência adicionando um segundo e um terceiro parâmetro.

for i in range(4,10,2): #De 4 a 9, avançando de dois em dois
    print(i)
Resultado:

>
4
6
8
>
Função xrange()

Na maioria das vezes, xrange e range são exatamente os mesmos em termos de funcionalidade. Ambos fornecem uma maneira de gerar uma lista de números inteiros para você usar, como quiser. A única diferença é que range retorna um objeto de lista do Python e xrange retorna um objeto xrange. Isso significa que xrange, na verdade, não gera uma lista estática em tempo de execução como o range faz. Ela cria os valores conforme você precisa deles com uma técnica especial chamada de yielding. Essa técnica é usada com um tipo de objeto conhecido como gerador.

Mais uma coisa para adicionar. No Python 3.x, a função xrange não existe mais. A função range agora faz o que xrange fazia no Python 2.x

Iterar por valores em uma lista ou tupla

A = ["Olá", 1, 65, "obrigado", [2, 3]]
for valor in A:
    print(valor)
Resultado:

>
Olá
1
65
obrigado
[2, 3]
>
Iterar por chaves em um dicionário (ou hashmap)

frutas_para_cores = {"maçã": "#ff0000",
                     "limão": "#ffff00",
                     "laranja": "#ffa500"}

for chave in frutas_para_cores:
    print(chave, frutas_para_cores[chave])
Resultado:

>
maçã #ff0000
limão #ffff00
laranja #ffa500
>
Iterar por duas listas do mesmo tamanho um único laço com a função zip()

A = ["a", "b", "c"]
B = ["a", "d", "e"]

for a, b in zip(A, B):
  print(a, b, a == b)
  
Resultado:

>
a a True
b d False
c e False
>
Iterar por uma lista e obter o índice correspondente com a função enumerate()

A = ["isso", "é", "algo", "divertido"]

for indice,palavra in enumerate(A):
    print(indice, palavra)
Resultado:

>
0 isso
1 é
2 algo
3 divertido
>
Um caso de uso comum é iterar por um dicionário:

for nome, telefone in contatos.items():
  print(nome, "pode ser contatado por meio de", telefone)
Se você absolutamente precisar acessar o índice atual de sua iteração, NÃO use range(len(iterável))! Esta é uma prática extremamente ruim e vai fazer com que os desenvolvedores seniores de Python riam muito de você. Use a função interna enumerate():

for indice, item in enumerate(cesta_compras):
  print("O item", indice, "é um", item)
Instruções for/else do Python permitem que você use else com laços for. O caso else é executado quando nenhuma das condições no corpo do laço for tiver sido satisfeita. Para usar o else, temos que usar a instrução break para que possamos sair do laço em uma condição satisfeita. Se não sairmos, a parte do else será executada.

dias_de_semana = ['Segunda','Terça','Quarta','Quinta','Sexta']
hoje = 'Sábado'
for dia in dias_de_semana:
  if dia == hoje:
    print('hoje é um dia de semana')
    break
else:
  print('hoje não é um dia de semana')
No caso acima, o resultado será hoje não é um dia de semana já que o break dentro do laço nunca será executado.

Iterar por uma lista usando uma função inline de laço

Também poderíamos iterar inline (ou em linha) usando Python. Por exemplo, se precisarmos colocar em maiúsculas todas as palavras em uma lista a partir de outra lista, poderíamos simplesmente fazer o seguinte:

A = ["esta", "é", "uma", "estrela", "muito", "brilhante"]

MAIUSCULO = [palavra.upper() for palavra in A]
print (MAIUSCULO)
Resultado:

>
['ESTA', 'É', 'UMA', 'ESTRELA', 'MUITO', 'BRILHANTE']
Uma função permite que você defina um bloco de código reutilizável que pode ser executado várias vezes em seu programa.

As funções permitem que você crie soluções mais modulares e evite se repetir (veja Don't Repeat Yourself, ou DRY) para problemas complexos.

Embora o Python já forneça muitas funções embutidas, como print() e len(), você também pode definir suas próprias funções para usar em seus projetos.

Uma das grandes vantagens de usar funções em seu código é que isso reduz o número total de linhas de código em seu projeto.

Sintaxe
No Python, uma definição de função tem o seguinte:

A palavra-chave def
um nome de função
parênteses "()" e, dentro dos parênteses, parâmetros de entrada, apesar de eles serem opcionais.
um caractere de dois pontos ":"
um bloco de código para executar
uma instrução de retorno (opcional)
# uma função sem parâmetro ou valores de retorno
def dizOla():
  print("Olá!")

dizOla()  # chama a função, 'Olá!' é exibida no console

# uma função com um parâmetro
def olaComNome(nome):
  print("Olá, " + nome + "!")

olaComNome("Ada")  # chama a função e 'Olá, Ada!' é exibida no console

# uma função com vários parâmetros com uma instrução de retorno
def multiplicar(val1, val2):
  return val1 * val2

multiplicar(3, 5)  # exibe 15 no console
Funções são blocos de código que podem ser reutilizados simplesmente chamando a função. Isso permite a reutilização de código simples e elegante sem reescrever explicitamente seções de código. Isso torna o código mais legível, mais fácil de depurar e limita os erros de digitação.

As funções em Python são criadas usando a palavra-chave def, seguida por um nome de função e parâmetros de função entre parênteses.

Uma função sempre retorna um valor. A palavra-chave return é usada pela função para retornar um valor. Se você não quiser retornar nenhum valor, o valor padrão None será retornado.

O nome da função é usado para chamar a função, passando os parâmetros necessários entre parênteses.

# esta é uma função básica de soma
def soma(a, b):
  return a + b

resultado = soma(1, 2)
# resultado = 3
Você pode definir valores padrão para os parâmetros e, desse modo, o Python interpretará que o valor desse parâmetro é o padrão se nenhum for fornecido.

def soma(a, b=3):
  return a + b

resultado = soma(1)
# resultado = 4
Você pode passar os parâmetros na ordem que você quiser, usando o nome do parâmetro.

resultado = soma(b=2, a=2)
# resultado = 4
Porém, não é possível passar um argumento nomeado antes de um não nomeado.

resultado = soma(3, b=2)
# resultado = 5
resultado2 = soma(b=2, 3)
# vai levantar uma exceção SyntaxError
Funções também são objetos, então você pode atribuí-las a uma variável e usar aquela variável como uma função.

s = soma
resultado = s(1, 2)
# resultado = 3
Observações
Se uma definição de função inclui parâmetros, você deve fornecer o mesmo número de parâmetros ao chamar a função.

print(multiplicar(3))  # TypeError: multiplicar() aceita exatamente dois argumentos 2 (0 fornecido)

print(multiplicar('a', 5))  # 'aaaaa' exibido no console

print(multiplicar('a', 'b'))  # TypeError: Python não consegue multiplicar duas strings
O bloco de código que a função executará inclui todas as instruções indentadas dentro da função.

def minhaFunc():
  print('isso vai exibir')
  print('assim como isso aqui')

x = 7
# a atribuição de x não é parte da função já que a atribuição não está indentada
Variáveis definidas dentro de uma função existem apenas dentro do escopo daquela função.

def double(num):
  x = num * 2
  return x

print(x)  # erro – x não está definido
print(double(4))  # exibe 8
O Python interpreta o bloco de função apenas quando a função é chamada e não quando a função é definida. Portanto, mesmo que o bloco de definição da função contenha algum tipo de erro, o interpretador do Python apontará isso apenas quando a função for chamada.

Os geradores são um tipo especial de função que permite retornar valores sem encerrar uma função. Ele faz isso usando a palavra-chave yield. Semelhante a return, a expressão yield retornará um valor para o chamador. A principal diferença entre os dois é que o yield suspenderá a função, permitindo que mais valores sejam retornados no futuro.

Os geradores são iteráveis para que possam ser usados de forma limpa com laços for ou qualquer outro modo de iteração.

def meu_gerador():
    yield 'olá,'
    yield 'mundo'
    yield '!'

for item in meu_gerador():
    print(item)

# saída:
# olá,
# mundo
# !
Assim como os outros iteradores, os geradores podem ser passados para a função next para recuperar o próximo item. Quando um gerador não tem mais valores para produzir, um erro StopIteration é levantado.

g = meu_gerador()
print(next(g))
# 'olá,'
print(next(g))
# 'mundo'
print(next(g))
# '!'
print(next(g))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
Os geradores são particularmente úteis quando você precisa criar um grande conjunto de valores, mas não precisa mantê-los todos na memória ao mesmo tempo. Por exemplo, se você precisar exibir o primeiro milhão de números de Fibonacci, normalmente retornará uma lista de um milhão de valores e iterará sobre a lista para exibir cada valor. No entanto, com um gerador, você pode retornar cada valor, um de cada vez:

def fib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fib(1000000):
    print(x)
O Python oferece suporte a um conceito de iteração sobre contêineres. Isso é implementado usando dois métodos distintos. Eles são usados para permitir que classes definidas pelo usuário ofereçam suporte à iteração.

Documentação do Python – Tipos iteradores

Iteração é o processo de repetir programaticamente uma etapa um determinado número de vezes. Um programador pode fazer uso da iteração para realizar a mesma operação em cada item em uma coleção de dados, por exemplo, ao exibir cada item em uma lista.

Os objetos podem implementar um método __iter__() que retorna um objeto iterador para dar suporte à iteração.
Objetos iteradores devem implementar:

__iter__(): retorna o objeto iterador.
__next__(): retorna o próximo objeto do contêiner.
iteratorobject = 'abc'.iter()
print(iteratorobject)
print(id(iteratorobject))
print(id(iteratorobject.iter())) # Retorna o próprio iterador.
print(iteratorobject.next()) # Retorna o 1º objeto e avança o iterador.
print(iteratorobject.next()) # Retorna o 2º objeto e avança o iterador.
print(iteratorobject.next()) # Retorna o 3º objeto e avança o iterador.
print(iteratorobject.next()) # Levanta a exceção StopIteration.
Saída:

<str_iterator object at 0x102e196a0>
4343305888
4343305888
a
b
c
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-1-d466eea8c1b0> in <module>()
      6 print(iterator_object.__next__())     # Retorna o 2º objeto e avança o iterador.
      7 print(iterator_object.__next__())     # Retorna o 3º objeto e avança o iterador.
----> 8 print(iterator_object.__next__())     # Levanta a exceção StopIteration.

StopIteration:
As operações ternárias no Python, muitas vezes também chamadas de expressões condicionais, permitem que o programador realize uma avaliação e retorne um valor com base na verdade da condição fornecida.

O operador ternário difere de uma estrutura padrão if, else e elif no sentido de que não é uma estrutura de fluxo de controle e se comporta mais como outros operadores como == ou != na linguagem Python.

Exemplo
Neste exemplo, a string Par é retornada se a variável val for par, caso contrário, a string Ímpar é retornada. A string retornada é então atribuída à variável is_even e impressa no console.

Entrada
for val in range(1, 11):
    is_even = "Par" if val % 2 == 0 else "Ímpar"
    print(val, is_even, sep=' = ')
Saída
1 = Ímpar
2 = Par
3 = Ímpar
4 = Par
5 = Ímpar
6 = Par
7 = Ímpar
8 = Par
9 = Ímpar
10 = Par
Python utiliza o laço while de modo semelhante a outras linguagens populares. O laço while avalia uma condição e executa um bloco de código se a condição for verdadeira. O bloco de código é executado repetidamente até que a condição se torne falsa.

A sintaxe básica é:

contador = 0
while contador < 10:
   # Executa o bloco de código aqui desde
   # que o contador seja menor que 10
Um exemplo é mostrado abaixo:

dias = 0
semana = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'Sábado', 'Domingo']
while dias < 7:
   print("Hoje é " + semana[dias])
   dias += 1
Saída:

Hoje é segunda-feira
Hoje é terça-feira
Hoje é quarta-feira
Hoje é quinta-feira
Hoje é sexta-feira
Hoje é sábado
Hoje é domingo
Explicação linha a linha do código acima:

a variável dias é definida com um valor 0.
uma variável semana recebe atribuição de uma lista contendo todos os dias da semana.
o laço while inicia
o bloco de código será executado até que a condição retorne "true".
a condição é "dias<7" que, aproximadamente, diz: executar o laço while durante o tempo em que a variável dias for menor que 7
Então, quando dias = 7, o laço while para de ser executado.
a variável dias é atualizada em cada iteração.
Quando o laço while é executado pela primeira vez, a linha "Hoje é segunda-feira" é impressa no console e a variável dias se torna igual a 1.
Como a variável dias é igual a 1 que é menor que 7, o laço while é executado novamente.
Ele continua de novo e de novo e, quando o console imprime "Hoje é domingo", a variável dias passa a ser igual a 7 e o laço while interrompe a execução.
f-strings no Python
Na versão 3.6 do Python, um novo método de formatação de strings foi implementado. O novo método é chamado de interpolação de string literal (embora comumente referido como uma f-string).

O uso de f-string permite que o programador insira dinamicamente uma variável em uma string de maneira limpa e concisa. Além de inserir variáveis em uma string, esse recurso também fornece a capacidade de um programador avaliar expressões, juntar o conteúdo da coleção e até mesmo invocar funções dentro da f-string.

Para executar esses comportamentos dinâmicos dentro de uma f-string, nós os envolvemos dentro de chaves dentro da string e colocamos um f minúsculo no início da string (antes da aspa de abertura).

Exemplos
Inserir dinamicamente uma variável em uma string em tempo de execução:

name = 'Jon Snow'
cumprimentar = f'Olá, {name}!'
print(cumprimentar)
Avaliar uma expressão em uma string:

val1 = 2
val2 = 3
expr = f'A soma de {val1} + {val2} é {val1 + val2}'
print(expr)
Chamar uma função e inserção de saídas dentro de uma string:

def soma(*args):
    resultado = 0
    for arg in args:
        resultado += arg
    return resultado

func = f'A soma de 3 + 5 é {soma(3, 5)}'
print(func)
Unir o conteúdo de uma coleção dentro de uma string:

frutas = ['Banana', 'Maçã', 'Pera']

lista_str = f'Lista de frutas: {", ".join(frutas)}'
print(lista_str)
Você pode baixar o Python neste link oficial. Com base no seu sistema operacional (Windows ou Linux ou OSX), convém instalar o Python 3 seguindo estas instruções.

Usando ambientes virtuais
É sempre uma ótima ideia isolar (usando uma sandbox) da sua instalação do Python e mantê-la separada do seu Python do sistema. O Python do sistema é o caminho para o interpretador Python, que é usado por outros módulos instalados junto com seu sistema operacional.

Não é seguro instalar bibliotecas ou frameworks da Web do Python diretamente usando o Python do sistema. Em vez disso, você pode usar o Virtualenv para criar e gerar um processo do Python separado ao desenvolver aplicativos em Python.

Virtualenvwrapper
O módulo Virtualenvwrapper facilita o gerenciamento e isolamento (sandbox) de vários ambientes de sandbox do Python em uma máquina, sem corromper nenhum módulo ou serviço escrito em Python e usado por sua máquina.

É claro que a maioria dos ambientes de desenvolvimento hospedados na nuvem, como Nitrous ou Cloud9, também vêm com esses ambientes pré-instalados e prontos para você codificar! Você pode escolher rapidamente uma caixa do seu painel e começar a codificar depois de ativar um ambiente do Python 3.

No Cloud9, você precisa selecionar a caixa Django ao criar um novo ambiente de desenvolvimento.

Seguem alguns exemplos de comandos do shell. Se você deseja copiar e colar, observe que o sinal $ é uma abreviação para o prompt do terminal, não faz parte do comando. Meu prompt do terminal têm esta aparência:

alayek:~/workspace (master) $
E um ls seria algo como

alayek:~/workspace (master) $ ls
Mas, enquanto escrevo isso na documentação, eu escreveria o seguinte:

$ ls
Voltando para nossa discussão, você pode criar um isolamento que inclui o interpretador do Python 3 no Cloud9 executando em nosso terminal de nuvem:

$ mkvirtualenv py3 --python=/usr/bin/python3
Você precisa executá-lo apenas uma vez depois de criar uma nova sandbox para seu projeto. Uma vez executado, esse comando criaria um novo virtualenv isolado pronto para você usar, chamado py3.

Para visualizar os ambientes virtuais disponíveis, você pode usar

$ workon
Para ativar py3, você pode usar o comando workon com o nome do ambiente:

$ workon py3
Todos os três comandos de terminal acima também funcionariam em máquinas Linux locais ou máquinas OSX. Estes são comandos virtualenvwrapper; portanto, se você planeja usá-los, certifique-se de ter este módulo instalado e adicionado à variável PATH.

Se você estiver dentro de um ambiente virtual, pode descobrir isso facilmente verificando o prompt do terminal. O nome do ambiente será mostrado claramente no prompt do terminal.

Por exemplo, quando estou dentro do ambiente py3, estarei vendo isso como meu prompt do terminal:

(py3)alayek:~/workspace (master) $
Observe o (py3) entre parênteses! Se por algum motivo você não estiver vendo isso, mesmo se estiver dentro de um ambiente virtual, pode tentar fazer uma das coisas mencionadas aqui.

Para sair de um ambiente virtual ou desativar um – use este comando:

$ deactivate
Novamente, isso funciona apenas com o módulo virtualenvwrapper.

Pipenv
Uma alternativa ao uso do virtualenvwrapper é o Pipenv. Ele cria automaticamente ambientes virtuais para seus projetos e mantém um Pipfile que contém as dependências. Usar o Pipenv significa que você não precisa mais usar pip e virtualenv separadamente ou gerenciar seu próprio arquivo requirements.txt. Para aqueles familiarizados com JavaScript, o Pipenv é semelhante ao uso de uma ferramenta de empacotamento como o npm.

Para começar a usar o Pipenv, você pode seguir este guia (em inglês) muito detalhado. O Pipenv facilita a especificação de qual versão do Python você deseja usar para cada projeto, a importação de um arquivo requirements.txt existente e colocar suas dependências em um gráfico.
