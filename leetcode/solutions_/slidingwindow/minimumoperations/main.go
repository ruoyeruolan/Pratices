// @Introduce  :
// @File       : mian.go
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/19 18:24
// @Description:

package main

func minimumOperations(nums []int) int {

	n := len(nums)
	var count int

	for idx := 0; idx < n-2; idx++ {
		if nums[idx] == 0 {
			nums[idx] = 1
			nums[idx+1] ^= 1
			nums[idx+2] ^= 1

			count += 1
		}
	}

	if nums[n-2] == 0 || nums[n-1] == 0 {
		return -1
	}
	return count
}

func minimumOperations_sliding_window(nums []int) int {
	n := len(nums)
	var count int

	for idx := 0; idx < n-2; idx++ {
		if nums[idx] == 0 {
			nums[idx] = 1
			nums[idx+1] ^= 1
			nums[idx+2] ^= 1

			count += 1
		}
	}

	if nums[n-2] == 0 || nums[n-1] == 0 {
		return -1
	}
	return count
}

func main() {
	println("Result:", minimumOperations([]int{0, 1, 1, 1}))

}
