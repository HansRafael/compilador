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
