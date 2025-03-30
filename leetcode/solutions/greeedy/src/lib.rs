pub struct Solution;
pub mod partionlabels;

pub fn add(left: u64, right: u64) -> u64 {
    left + right
}

#[cfg(test)]
mod tests {
    use crate::partionlabels::PartitionLabels;

    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }

    #[test]
    fn it_works_example() {
        assert_eq!(
            Solution::partition_labels("ababcbacadefegdehijhklij".to_string()),
            vec![9, 7, 8]
        )
    }
}
