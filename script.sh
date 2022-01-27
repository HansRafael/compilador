#!/bin/bash

java -jar antlr-4.9.3-complete.jar -Dlanguage=Python3 -no-listener Tiny.g4
python3 compiler.py Test.go Test.j
java -jar jasmin-2.4.jar Test.j
java Test


