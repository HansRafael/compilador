package main

func main() {
    var a = 1
    var x = "X"
    var b = 2
    var y = "Y"
    var cassa = 2

    a = 3
    b = a
    a = "Z"           // error: 'a' is integer
    b = x             // error: 'b' in integer
    a = read_str()    // error: 'a' is integer

    x = "Q"
    y = x
    x = 4             // error: 'x' is string
    y = b             // error: 'y' is string
    x = read_int()    // error: 'x' is string

    println(123)
    println("xyz")
    println(a + x)    // error: operands must be integers
    println(b - y)    // error: operands must be integers
    println(x * "W")  // error: operands must be integers
    println(y / x)    // error: operands must be integers
    println(8 % (x))  // error: operands must be integers

    if a == x {       // error: operands must be integers
        println(456)
    }

}

