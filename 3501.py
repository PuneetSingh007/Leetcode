##maximum-active-section-with-trade-2

from typing import List
from bisect import bisect_left


class Solution:
    def maxActiveSectionsAfterTrade(
        self,
        s: str,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(s)

        # Store positions where the character changes
        changes = []

        if s[0] == '0':
            changes.append(0)

        for i in range(1, n):
            if s[i] != s[i - 1]:
                changes.append(i)

        if s[-1] == '0':
            changes.append(n)

        # Calculate the gain for every pair
        # of adjacent zero sections
        gains = []

        for i in range(3, len(changes), 2):
            gain = (
                changes[i] - changes[i - 1]
                + changes[i - 2] - changes[i - 3]
            )
            gains.append(gain)

        seg_tree = SegmentTree(gains)

        result = []

        for l, r in queries:

            left = bisect_left(changes, l + 1)
            right = bisect_left(changes, r + 1)

            count = right - left

            # No possible trade
            if count < 2 or (
                count == 2 and left % 2 == 0
            ):
                result.append(0)

            # Pattern like "010"
            elif count == 2:

                gain = (
                    r + 1 - changes[right - 1]
                    + changes[left] - l
                )

                result.append(gain)

            # Pattern like "1010" or "0101"
            elif count == 3:

                if left % 2 == 0:

                    # "1010"
                    gain = (
                        r + 1 - changes[right - 1]
                        + changes[left + 1]
                        - changes[left]
                    )

                else:

                    # "0101"
                    gain = (
                        changes[right - 1]
                        - changes[left + 1]
                        + changes[left]
                        - l
                    )

                result.append(gain)

            else:

                best = 0

                # Left boundary cuts through a zero section
                if left % 2 == 1:

                    best = max(
                        best,
                        changes[left + 2]
                        - changes[left + 1]
                        + changes[left]
                        - l
                    )

                    left += 1

                # Right boundary cuts through a zero section
                if right % 2 == 1:

                    best = max(
                        best,
                        r + 1
                        - changes[right - 1]
                        + changes[right - 2]
                        - changes[right - 3]
                    )

                    right -= 1

                # Check complete zero-section pairs in the middle
                best = max(
                    best,
                    seg_tree.query(
                        left // 2 - 1,
                        right // 2 - 1
                    )
                )

                result.append(best)

        # Add original number of 1s
        ones = s.count('1')

        return [
            ones + gain
            for gain in result
        ]


class SegmentTree:

    def __init__(self, arr: List[int]):

        # Next power of 2
        self.n = 1 << len(arr).bit_length()

        self.tree = [0] * (2 * self.n)

        # Fill leaves
        for i, value in enumerate(arr):
            self.tree[self.n + i] = value

        # Build tree
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(
                self.tree[2 * i],
                self.tree[2 * i + 1]
            )

    def query(self, left: int, right: int) -> int:

        left += self.n
        right += self.n

        result = 0

        # IMPORTANT:
        # Keep the same indexing convention
        # as the original solution.
        while right - left > 1:

            if left % 2 == 0:
                result = max(
                    result,
                    self.tree[left + 1]
                )

            if right % 2 == 1:
                result = max(
                    result,
                    self.tree[right - 1]
                )

            left //= 2
            right //= 2

        return result