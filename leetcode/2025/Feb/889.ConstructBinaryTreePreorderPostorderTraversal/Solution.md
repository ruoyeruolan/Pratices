
# 889. Construct Binary Tree from Preorder and Postorder Traversal

Given two integer arrays, `preorder` and `postorder` where `preorder` is the `preorder` traversal of a binary tree of distinct values and `postorder` is the `postorder` traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can **return any** of them.

**Example 1:**

![ex1](./static/lc-prepost.jpg)

**Input**: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]

**Output**: [1,2,3,4,5,6,7]

**Example 2**:

**Input**: preorder = [1], postorder = [1]

**Output**: [1]

**Constraints**:

- `1 <= preorder.length <= 30`
- `1 <= preorder[i] <= preorder.length`
- All the values of `preorder` are unique.
- `postorder.length == preorder.length`
- `1 <= postorder[i] <= postorder.length`
- All the values of `postorder` are unique.
- It is guaranteed that `preorder` and `postorder` are the `preorder` traversal and `postorder` traversal of the same binary tree.

# Solution

## Overview

We are given two integer arrays that represent the `preorder` and `postorder` traversals of a binary tree. Our task is to rebuild the tree and return its root. First, let's clarify the key terms involved in this task:

A binary tree is a tree data structure where each node has at most two children, called `left` and `right`. Tree traversal means visiting all the nodes in a specific order. In this problem, we use two common types of binary tree traversal:

- **Preorder traversal**: We visit the current node first, then go to the left child, and finally to the right child. This means that the parent node will appear before its children in the preorder array.

- **Postorder traversal**: We temporarily ignore the current node and move directly to its children, visiting the left child first and then the right. After that, we return to the node and process it last. In other words, the parent node always appears after its children in the postorder array.

> Similar problems:
>
> - [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
> - [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
> - [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
> - [285. Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)
> - [510. Inorder Successor in BST II](https://leetcode.com/problems/inorder-successor-in-bst-ii/)
> - [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
> - [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
