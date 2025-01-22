// @Introduce  : 
// @File       : ReverseInteger.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/01/10 17:20
// @Description:

fn main() {
    let x = 123;
    let res = reverse(x);
    println!("{}", res);
}

pub fn reverse(x: i32) -> i32 {
    let mut res: i32 = 0;
    let mut cur: i32 = x;
        
    while cur != 0 {
        match res.checked_mul(10) {
            None => return 0,
            Some(tmp) => match tmp.checked_add(cur % 10) {
                None => return 0,
                Some(fine) => {
                    res = fine;
                }
            } 
        }
        cur = cur / 10;
    }
    res
}