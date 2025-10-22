"""LeetCode 21: Merge Two Sorted Lists"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None

    @staticmethod
    def from_iterable(values: Iterable[int]) -> Optional["ListNode"]:
        head: Optional[ListNode] = None
        tail: Optional[ListNode] = None
        for value in values:
            node = ListNode(value)
            if head is None:
                head = node
                tail = node
            else:
                assert tail is not None
                tail.next = node
                tail = node
        return head

    def to_list(self) -> list[int]:
        node = self
        values: list[int] = []
        while node:
            values.append(node.val)
            node = node.next
        return values


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next


if __name__ == "__main__":
    first = ListNode.from_iterable([1, 2, 4])
    second = ListNode.from_iterable([1, 3, 4])
    merged = Solution().mergeTwoLists(first, second)
    print("Merged list:", merged.to_list() if merged else [])
