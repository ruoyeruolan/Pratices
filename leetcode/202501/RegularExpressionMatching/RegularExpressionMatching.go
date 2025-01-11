// @Introduce  : 
// @File       : RegularExpressionMatching.go
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/01/11 17:45
// @Description: 
//				Given an input string s and a pattern p, implement regular expression 
//				matching with support for '.' and '*' where:

//				'.' Matches any single character.
// 				'*' Matches zero or more of the preceding element.
// 				The matching should cover the entire input string (not partial).

// # Example 1:

// # Input: s = "aa", p = "a"
// # Output: false
// # Explanation: "a" doesn't match the entire string "aa".
// # Example 2:

// # Input: s = "aa", p = "a*"
// # Output: true
// # Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
// # Example 3:

// # Input: s = "ab", p = ".*"
// # Output: true
// # Explanation: ".*" means "zero or more (*) of any character (.)".
package main

import "fmt"
import "regexp"

func isMatch(s string, p string) bool {
	return regexp.MustCompile("^" + p + "$").MatchString(s)
}

func isMatch_(s string, p string) bool {
	if p == "" {return s == ""}

	firstMatch := s != "" && (s[0] == p[0] || p[0] == '.')
	if len(p) >= 2 && p[1] == '*' {
		return isMatch_(s, p[2:]) || firstMatch && isMatch_(s[1:], p)
	} else {
		return firstMatch && isMatch_(s[1:], p[1:])
	}
}


func isMatchDp(s string, p string) bool {
    dp := make([][]bool, len(s)+1)
    for i := range dp {
        dp[i] = make([]bool, len(p)+1)
    }

    dp[len(s)][len(p)] = true

    for i := len(s); i >= 0; i-- {
        for j := len(p) - 1; j >= 0; j-- {
            firstMatch := i < len(s) && (s[i] == p[j] || p[j] == '.')

            if j+1 < len(p) && p[j+1] == '*' {
                dp[i][j] = dp[i][j+2] || (firstMatch && dp[i+1][j])
            } else {
                dp[i][j] = firstMatch && dp[i+1][j+1]
            }
        }
    }
    return dp[0][0]
}



func main() {
	s := "aa"
	p := "a"
	
	fmt.Printf("%v\n", isMatch(s, p))
	fmt.Printf("%v\n", isMatch_(s, p))
}