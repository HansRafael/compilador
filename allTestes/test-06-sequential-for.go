// results in 1, 2, 3, 2, 1

package main

func main () {
    var n = 1
    for n <= 2 {
        println(n)
        n = n + 1
    }
    for n >= 1 {
        println(n)
        n = n - 1
    }
}
