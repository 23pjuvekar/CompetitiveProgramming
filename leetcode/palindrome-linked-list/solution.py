# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        string = ""
        curr = head

        while head != None:
            string += str(head.val)
            head = head.next

        print(string)

        return self.isPalindromeString(string)

    def isPalindromeString(self, string):
        f_p = 0
        s_p = len(string) - 1

        while f_p < s_p:
            if string[f_p] != string[s_p]:
                return False
            f_p += 1
            s_p -= 1
        
        return True
