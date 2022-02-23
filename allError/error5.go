package main

func main() {
    var a = 1
    var x = "X"
    var b = 2
    var y = "Y"

    a = 3
    b = a + 10
    a = "Z"           // error: 'a' is integer
    b = x             // error: 'b' in integer
    a = read_str()    // error: 'a' is integer
	println(y)
	println(b)
	println(a)
}