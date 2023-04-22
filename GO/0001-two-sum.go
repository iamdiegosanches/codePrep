func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for idx, num := range nums {

		if val, found := m[target-num]; found {
			return []int{val, idx}
		}

		m[num] = idx
	}
	return nil
}

// or

func twoSum(nums []int, target int) []int {
    for i := 0; i < len(nums); i++ {
        for j := 0; j < len(nums); j++ {
            if i != j {
                if nums[i] + nums[j] == target {
                    return []int{i, j}
                }
            }
        }
    }
    return nil
}
