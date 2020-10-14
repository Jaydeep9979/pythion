class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverse(node,n):
            if n==1:
                succesor=node.next    
                return node
            last=reverse(node.next,n-1)
            node.next.next=node
            node.next=succesor
            return last
        def reverse_between(node,m,n):
            if m==1:
                return reverse(node,n)
            head.next=reverse_between(node.next, m-1,n-1)
            return head

        