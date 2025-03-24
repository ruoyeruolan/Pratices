// @Introduce  :
// @File       : main.go
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/24 18:46
// @Description:
package main

import (
	"fmt"
	"sort"
)

func countDays(days int, meetings [][]int) int {
	sort.Slice(
		meetings, func(i, j int) bool {
			if meetings[i][0] == meetings[j][0] {
				return meetings[i][1] < meetings[j][1]
			}
			return meetings[i][0] < meetings[j][0]
		})

	dys := 0
	lastedEnd := 0

	for _, meeting := range meetings {
		start, end := meeting[0], meeting[1]
		if start > lastedEnd {
			dys += start - lastedEnd - 1
		}

		if end > lastedEnd {
			lastedEnd = end
		}
	}
	dys += days - lastedEnd
	return dys
}

func main() {
	days := 5
	meetings := [][]int{{2, 4}, {1, 3}}
	result := countDays(days, meetings)
	fmt.Println(result)
}
