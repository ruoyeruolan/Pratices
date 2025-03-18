// @Introduce  : 
// @File       : ContainerWithMostWater.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/01/19 15:54
// @Description:

// # You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
// # Find two lines that together with the x-axis form a container, such that the container contains the most water.
// # Return the maximum amount of water a container can store.
// # Notice that you may not slant the container.

// # Input: height = [1,8,6,2,5,4,8,3,7]
// # Output: 49
// # Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
use std::cmp::{min,max};

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        
        let mut left = 0;
        let mut right = height.len() as i32 - 1;
        let mut area = 0;

        while left < right {
            area = max(area, (right - left) * min(height[left as usize], height[right as usize]));

            if height[left as usize] < height[right as usize] {
                left += 1;
            } else {
                right -= 1;
            }
        }
        area
    }
}