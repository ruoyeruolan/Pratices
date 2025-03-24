// -*- encoding: utf-8 -*-*
// @Introduce  :
// @File       : freedays.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/24 18:20
// @Description:

use crate::Solution;

pub trait CountDays {
    fn count_days(days: i32, meetings: Vec<Vec<i32>>) -> i32;
}

impl CountDays for Solution {
    fn count_days(days: i32, meetings: Vec<Vec<i32>>) -> i32 {
        let mut meetings = meetings;
        meetings.sort();

        let (mut dys, mut lasted_end) = (0, 0);

        for meeting in meetings {
            if let [start, end] = meeting.as_slice() {
                if *start > lasted_end {
                    dys += start - lasted_end - 1;
                }
                lasted_end = lasted_end.max(*end);
            }
        }

        dys += days - lasted_end;
        dys
    }
}
