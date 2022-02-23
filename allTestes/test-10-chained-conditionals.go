// must println 1

package main

func main () {
    var a = 1
    var b = 2
    var c = 3
    if a == b {
        if b != c {
            println(b)
        } else {
            println(c)
        }
    } else {
        if a > b {
            println(b)
        } else {
            if a < b {
                if b > c {
                    println(c)
                } else {
                    println(a)
		        }
	        }
        }
    }
}
