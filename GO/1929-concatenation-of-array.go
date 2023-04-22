func getConcatenation(nums []int) []int {
    arr := make([]int, len(nums)*2)
    for i := 0; i < len(nums); i++ {
        arr[i] = nums[i]
        arr[i+len(nums)] = nums[i]
    }
    return arr
}
