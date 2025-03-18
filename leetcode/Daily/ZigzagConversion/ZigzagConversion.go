package main

import "strings"

func main() {
	// 测试用例
	input := "PAYPALISHIRING"
	numRows := 3
	result := convert(input, numRows)
	println(result) // 输出: "PAHNAPLSIIGYIR"
}

func convert(s string, numRows int) string {
	
	if numRows == 1 || numRows >= len(s) {
		return s
	}

	zigzag := make([]string, numRows)
	row, step := 0, 1

	for _, i := range s {
		zigzag[row] += string(i)

		if row == 0 {
			step = 1
		} else if row == numRows - 1 {
			step = -1
		}
		row += step
	}
	// return strings.Join(zigzag, "")
	var res strings.Builder
	for i := 0; i < numRows; i++ {
		res.WriteString(zigzag[i])
	}
	return res.String()
}