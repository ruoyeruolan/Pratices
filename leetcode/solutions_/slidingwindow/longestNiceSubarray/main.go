// @Introduce  :
// @File       : mian.go
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/18 22:34
// @Description:

package main

func longestNiceSubarray(nums []int) int {
	n := len(nums)
	var used, start, length int
	for end := 0; end < n; end++ {
		for (used & nums[end]) != 0 {
			used ^= nums[start]
			start++
		}
		used |= nums[end]

		if end-start+1 > length {
			length = end - start + 1
		}
	}
	return length
}

func main() {
	example := []int{1, 3, 8, 48, 10}
	result := longestNiceSubarray(example)
	println("Result:", result)
}
