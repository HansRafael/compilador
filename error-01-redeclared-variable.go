// error for undefined variables

package main

func main() {
    var z = 2
    var z = 3  // error: 'z' is redeclared
    println(z)
}
