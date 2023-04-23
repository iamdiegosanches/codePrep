func romanToInt(s string) int {
    m := map[byte]int{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    var ans int = 0
    for i := 0; i < len(s); i++ {
        if i + 1 < len(s) && m[s[i]] < m[s[i + 1]] {
            ans -= m[s[i]]
        } else {
            ans += m[s[i]]
        }
    }
    return ans
}
