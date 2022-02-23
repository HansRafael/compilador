// errors for functions

package main

func fx(a int) int {
    return a
}

func fx(a int) int {  // error: function 'fx' already declared
    return a
}

func fy(b int) int {
    b = 0
    return "b"        // error: return value must be of integer type
}

func fz(c int) int {
    println(c)        // error: missing return statement in function
}

func main() {
    var d = fx("d")   // error: argument must be integer

    var e = "e"
    e = fx(1)         // error: types not matching in attribution

    var f = fw(2)     // error: function 'fw' not declared

    return 3          // error: return statement cannot be used inside main
}

