Criação de um compilador simples, que realiza as seguintes tarefas:
* com controle da stack
* Atribuição de variáveis (apenas inteiros e string)
* println
* função
* comentários
* detecção de erros
    -> variáveis redeclaradas
    -> variáveis não declaradas
    -> variáveis declaradas mas não utilizadas
    -> tipo da variável: se for String, não tem como atribuir um Int
    -> (10 * "w") => erro, apenas operandos inteiros
    -> função não declaradas
    -> sem return da função
    -> main com return
* Laços/repetições
    -> if
    -> else
    -> for
* operações sobre inteiros
    -> +
    -> -
    -> *
    -> /
    -> %
* comparações
    -> ==
    -> !=
    -> <
    -> <=
    -> >
    -> >=
------------------------------------------------OLD-----------------------------------------------------
Build compiler:

pip3 install antlr4-python3-runtime
java -jar antlr-4.9.3-complete.jar -Dlanguage=Python3 -no-listener Tiny.g4

Run program:
python3 compiler.py  > Test.j

python3 compiler.py input.txt Test.j
java -jar jasmin-2.4.jar Test.j
java Test


NEW -> 

java -jar antlr-4.9.3-complete.jar -Dlanguage=Python3 -no-listener Tiny.g4
DEPOIS QUE ALTERA, SÓ PRECISA RODAR OS COMANDOS ABAIXO
python3 compiler.py Test.go Test.j
java -jar jasmin-2.4.jar Test.j
java Test



Foi criado um script para realizar as tarefas. 
Primeiro, é necessário rodar

./build

para buildar o compilador em si.
Depois, para rodar algum teste, basta dar o seguinte comando:

./run <nome_do_arquivo.go>

Ele irá gerar o arquivo Test.j para a VM do Java (com o jasmin-2.4)

------------------------------------------------OLD-----------------------------------------------------

------------------------------------------------NEW-----------------------------------------------------
./test_all.sh   => testa todos os arquivos do dir allTestes

./error_all.sh  => Detecção de alguns erros ()


