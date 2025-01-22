// @Introduce  : 
// @File       : string2integer.go
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/01/10 18:30
// @Description:

package main

import (
	"fmt"
	"math"
	"strings"
	// "unicode"
)

func main() {
	x := "  -042"
	fmt.Println(string2integer(x))
}


func string2integer(s string) int {
	s = strings.TrimSpace(s)

	if s == "" {
		return 0
	}

	sign, res, i := 1, 0, 0
	if s[0] == '-' {
		sign = -1
		i++
	} else if s[0] == '+' {
		sign = 1
		i++
	}

	for ;(i < len(s)) && (s[i] >= '0') && (s[i] <= '9'); i++ {		
		res = res*10 + int(s[i] - '0')  // transfer string to int
		if res > math.MaxInt32 {
			if sign == 1 {
				return math.MaxInt32
			}
			return math.MinInt32
		}
	}
	return res * sign
}