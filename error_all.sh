test_files="allError/*.go"

for eachfile in $test_files
do
    echo "Testing error $eachfile" 
    if python3 compiler.py $eachfile Test.j; then
        if java -jar jasmin-2.4.jar Test.j; then
            java -cp . Test
            rm -f Test.class Test.j
        else
            rm -f Test.class
        fi
    else
        rm -f Test.j
    fi
    echo "------------------------------------"
    echo "\n"
done