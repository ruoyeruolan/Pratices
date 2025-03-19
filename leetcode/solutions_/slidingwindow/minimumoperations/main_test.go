package main

import (
	"testing"
)

func TestMinimumOperations(t *testing.T) {
	testCases := []struct {
		name     string
		nums     []int
		expected int
	}{
		{
			name:     "Example 1",
			nums:     []int{0, 1, 1, 1},
			expected: -1,
		},
		{
			name:     "Example 2",
			nums:     []int{0, 1, 1, 1, 0, 0},
			expected: 3,
		},
	}

	for _, tc := range testCases {
		res := minimumOperations(tc.nums)

		if res != tc.expected {
			t.Errorf("Res: %d, expected %d", res, tc.expected)
		}
	}
}

func TestMinimumOperationsSlidingWindows(t *testing.T) {
	testCases := []struct {
		name     string
		nums     []int
		excepted int
	}{
		{
			name:     "Example 1",
			nums:     []int{0, 1, 1, 1},
			excepted: -1,
		},
		{
			name:     "Example 2",
			nums:     []int{0, 1, 1, 1, 0, 0},
			excepted: 3,
		},
	}

	for _, tc := range testCases {
		res := minimumOperations_sliding_window(tc.nums)

		if res != tc.excepted {
			t.Errorf("Res: %d, expected %d", res, tc.excepted)
		}
	}
}
