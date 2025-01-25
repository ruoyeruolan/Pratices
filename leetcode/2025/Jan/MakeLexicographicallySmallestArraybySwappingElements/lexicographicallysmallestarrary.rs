// @Introduce  :
// @File       : lexicographicallysmallestarrary.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/01/25 21:30
// @Description:

impl Solution {
    pub fn lexicographically_smallest_array(nums: Vec<i32>, limit: i32) -> Vec<i32> {
        use std::collections::{HashMap, VecDeque};

        let mut curr_group = 0;
        let mut num_to_group = HashMap::new();
        let mut group_to_list = HashMap::new();

        let mut num_sorted = nums.clone();
        num_sorted.sort();

        num_to_group.insert(num_sorted[0], curr_group);
        group_to_list.insert(curr_group, VecDeque::from(vec![num_sorted[0]]));

        for i in 1..num_sorted.len() {
            if (num_sorted[i] - num_sorted[i - 1]).abs() > limit {
                curr_group += 1;
            }
            num_to_group.insert(num_sorted[i], curr_group);
            group_to_list
                .entry(curr_group)
                .or_insert_with(VecDeque::new)
                .push_back(num_sorted[i]);
        }

        let mut result = nums.clone();
        for i in 0..nums.len() {
            let num = nums[i];
            let group = num_to_group.get(&num).unwrap();
            result[i] = group_to_list.get_mut(group).unwrap().pop_front().unwrap();

            // if let Some(&group) = num_to_group.get(&num) {
            //     if let Some(deque) = group_to_list.get_mut(&group) {
            //         result[i] = deque.pop_front().unwrap();
            //     }
            // }
        }
        result
    }
}
