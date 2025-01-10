// @Introduce  :
// @File       : ReverseInteger.go
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/01/10 14:45
// @Description:

package main

import "fmt"

func main() {
	var x int = -123
	fmt.Printf("-123 %% 10: %v\n", x % 10)
}

func reverse(x int) int {
	var res int
	for x != 0 {
		res = res * 10 + x % 10
		x /= 10
	}
	if res > 1<<31-1 || res < -1<<31 {
		return 0
	}
	return res
}