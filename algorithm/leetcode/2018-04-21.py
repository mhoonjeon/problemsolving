# 637. Average of Levels in Binary Tree


# BFS
def averageOfLevels(self, root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    from collections import deque

    q = deque([root])
    res = []

    while q:
        sum = 0
        count = 0
        temp = deque([])
        while q:
            node = q.popleft()
            count += 1
            sum += node.val
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        q = temp
        res.append(sum / count)

        return res


# DFS
def averageOfLevels(self, root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    info = []

    def dfs(node, depth=0):
        if node:
            if len(info) <= depth:
                info.append([0, 0])
            # info[depth][sum, count]
            info[depth][0] += node.val
            info[depth][1] += 1
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
    dfs(root, 0)

    return [s/c for s, c in info]
