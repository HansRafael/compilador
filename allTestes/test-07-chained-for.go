// results in 1000000
//            1000000

package main

func main () {
    var total = 0
    var x = 0
    for x < 100 {
        var y = 1
        for y < 100 {
            total = total + y
            y = y + 1
        }
        var z = 100
        for z > 0 {
            total = total + z
            z = z - 1
        }
        x = x + 1
    }
    println(total)
}
