// must output 7

package main

func main () {
    var a = 1
    var b = 2
    var c = 3
    if a == b {
        if b > c {
            println(4)
        }
        if b <= c {
            println(5)
        }
    }
    if a != b {
        if a < b {
            if b > c {
                println(6)
            }
            if b <= c {
                println(7)
            }
        }
        if a >= b {
            println(8)
        }
    }
}
