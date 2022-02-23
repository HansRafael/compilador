// must output 2, 4 and 6

package main

func main () {
    var x = 77
    var y = 88
    if x == y {
        println(1)
    }
    if x != y {
        println(2)
    }
    x = 88
    if x < y {
        println(3)
    }
    if x <= y {
        println(4)
    }
    if x > y {
        println(5)
    }
    y = 77
    if x >= y {
        println(6)
    }
}
