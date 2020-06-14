#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # iteratively 迭代
    # recursively 递归
    # time: O(m+n) 其中 m 和 m 分别为两个链表的长度。
    # 因为每次循环迭代中，l1 和 l2 只有一个元素会被放进合并链表中， 
    # 因此 while 循环的次数不会超过两个链表的长度之和。
    # 所有其他操作的时间复杂度都是常数级别的
    # space：O(1) 只需要常数的空间存放若干变量

    # 定义一个dummy
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        cur.next = l1 or l2
        # cur.next = l1 if l1 is not None else l2
        # cur is the last node，so must use dummy
        return dummy.next


    # recursively 递归
    # time: O(m+n) 其中 m 和 m 分别为两个链表的长度。
    # 因为每次调用递归都会去掉 l1 或者 l2 的头节点（直到至少有一个链表为空），
    # 函数 mergeTwoList 至多只会递归调用每个节点一次。
    # 因此，时间复杂度取决于合并后的链表长度
    # space: O(m+n) 其中 m 和 m 分别为两个链表的长度。
    # 递归调用 mergeTwoLists 函数时需要消耗栈空间，
    # 栈空间的大小取决于递归调用的深度。
    # 结束递归调用时 mergeTwoLists 函数最多调用 n+mn+m 次。
    # 1130ms，40ms。。？？
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     # if one is empty, return the non-empty one
    #     if not l1 or not l2:
    #         return l1 or l2
    #     # find the smaller one
    #     if l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2

# s = Solution()
# l1 = ListNode(1)
# l1.next = ListNode(2)
# l1.next.next = ListNode(4)
# l2 = ListNode(1)
# l2.next = ListNode(3)
# l2.next.next = ListNode(4)

# print(s.mergeTwoLists(l1, l2))

# @lc code=end

