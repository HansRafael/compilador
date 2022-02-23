// error for unused variables

package main

func main() {
    var a = 2
    var b = a * 3
    var c = 3
    return a
    println(a)

    // error: 'b' is defined but never used

    // number of locals: 2
    // symbol table: ['a', 'b']
    // used vars: [True, False]
}
