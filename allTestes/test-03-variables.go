// results: 10, 8 and 6

package main

func main() {
    var x = 2
    println(x * 5)
    var y = x / 2
    println(4 + x * (3 - y))
    x = 6
    println(x)

    // number of locals: 2
    // symbol table: ['x', 'y']
}
