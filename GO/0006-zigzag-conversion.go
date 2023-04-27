func convert(s string, numRows int) string {
    ans := make([][]rune, numRows)
    i:= 0
    for i < len(s) {
        j := 0
        for j < numRows && i < len(s) {
            ans[j] = append(ans[j], rune(s[i]))
            j++
            i++
        }

        j = numRows - 2
        for j > 0 && i < len(s) {
            ans[j] = append(ans[j], rune(s[i]))
            j--
            i++
        }
    }
    result := ""
    for _, row := range ans {
        result += string(row)
    }
    return result
}
