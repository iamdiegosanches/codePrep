/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var ans = new(ListNode)
    var l3 **ListNode = &ans
    var carry int = 0

    for l1 != nil || l2 != nil{
        l3 = &((*l3).Next)
		*l3 = new(ListNode)

        var sum int = 0

        if l1 != nil {
            sum += l1.Val
            l1 = l1.Next
        }

        if l2 != nil {
            sum += l2.Val
            l2 = l2.Next
        }

        (*l3).Val = (sum + carry) % 10
		carry = (sum + carry) / 10
    }

    if carry > 0 {
        l3 = &((*l3).Next)
		*l3 = new(ListNode)
        (*l3).Val = carry
    }

    return ans.Next
}
