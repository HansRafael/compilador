#!/bin/bash

if ! java -jar antlr-4.9.3-complete.jar -Dlanguage=Python3 -no-listener Tiny.g4; then
    rm -f Tiny*.py Tiny.interp Tiny*.tokens
fi


