// @Introduce  :
// @File       : solution.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/02/06 19:16
// @Description:

impl Solution {
    pub fn tuple_same_product(nums: Vec<i32>) -> i32 {
        let numsLength = nums.len();
        let mut map = std::collections::HashMap::new();
        let mut totalNumberOfTuples = 0;
        let mut pairsOfEqualProduct = 0;

        for firstIndex in 0..numsLength {
            for secondIndex in (firstIndex + 1)..numsLength {
                let product = nums[firstIndex] * nums[secondIndex];

                map.entry(product)
                    .and_modify(|count| *count += 1)
                    .or_insert(1);
            }
        }

        for (_, val) in map {
            pairsOfEqualProduct = val * (val - 1) / 2;
            totalNumberOfTuples += 8 * pairsOfEqualProduct;
        }
        totalNumberOfTuples
    }
}
