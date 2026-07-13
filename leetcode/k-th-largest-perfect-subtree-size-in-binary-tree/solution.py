class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        perfect_subtree_heights = []

        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = get_height(node.left)
            right_height = get_height(node.right)

            is_perfect = left_height == right_height and left_height >= 0
            if is_perfect:
                height = left_height + 1
                perfect_subtree_heights.append(height)
                return height

            return -1

        get_height(root)

        if k > len(perfect_subtree_heights):
            return -1

        kth_largest_height = sorted(perfect_subtree_heights)[-k]
        return (1 << kth_largest_height) - 1
