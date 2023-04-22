func isPalindrome(x int) bool {
	numStr := strconv.Itoa(x)
	reversedStr := ""
	for i := len(numStr) - 1; i >= 0; i-- {
		reversedStr += string(numStr[i])
	}

  return numStr == reversedStr
}
