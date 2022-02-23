// test for functions
// result:
// 120
// prime

package main

func factorial(i int) int {
    if i <= 1 {
        return 1
    }
    return i * factorial(i - 1)
}

func divisors(n int) int {
    var c = 0
    var d = 1
    for d <= n {
        if n % d == 0 {
            c = c + 1
        }
        d = d + 1
    }
    return c
}

func main() {
    println(factorial(5))
    if divisors(43) == 2 {
        println("prime")
    } else {
        println("not prime")
    }
}

