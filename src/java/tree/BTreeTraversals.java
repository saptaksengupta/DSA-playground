// Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
// (i.e., from left to right, then right to left for the next level and alternate between).

// Example 1:
// Input: root = [3,9,20,null,null,15,7]
// Output: [[3],[20,9],[15,7]]

// Example 2:
// Input: root = [1]
// Output: [[1]]

// Example 3:
// Input: root = []
// Output: []

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;

class TreeNode {
    TreeNode left;
    TreeNode right;
    int val;

    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

public class BTreeTraversals {
    List<List<Integer>> result = new ArrayList<>();
    Queue<TreeNode> queue = new LinkedList<TreeNode>();

    public List<List<Integer>> levelOrder(TreeNode root) {

        if (root == null) 
            return result;
        
        queue.add(root);

        while(!queue.isEmpty()) {

            List<Integer> list = new ArrayList<>();
            int length = queue.size();

            for(int i = 0; i < length; i++) {
                TreeNode node = queue.poll();
                list.add(node.val);
                if (node.left != null) {
                    queue.add(node.left);
                }
    
                if (node.right != null) {
                    queue.add(node.right);
                }
            }

            result.add(list);
        }

        return result;
    }

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) {
            return result;
        }
        boolean leftToRight = false;

        Stack<TreeNode> currentLevel = new Stack<>();
        Stack<TreeNode> nextLevel = new Stack<>();

        currentLevel.add(root);

        while (!currentLevel.isEmpty()) {
            int length = currentLevel.size();
            List<Integer> list = new ArrayList<>();
            for(int i = 0; i < length; i++) {
                TreeNode node = currentLevel.pop();
                list.add(node.val);

                if (leftToRight) {
                    if(node.left != null) {
                        nextLevel.add(node.left);
                    }

                    if(node.right != null) {
                        nextLevel.add(node.right);
                    }
                } else {
                    if(node.right != null) {
                        nextLevel.add(node.right);
                    }

                    if(node.left != null) {
                        nextLevel.add(node.left);
                    }
                }
            }

            result.add(list);

            if(currentLevel.size() == 0) {
                leftToRight = !leftToRight;
                Stack<TreeNode> temp = currentLevel;
                currentLevel = nextLevel;
                nextLevel = temp;
            }
        }
        
        return result;
    }

    public static void main(String[] args) {

        TreeNode tree = new TreeNode(1);
        tree.left = new TreeNode(2);
        tree.right = new TreeNode(3);
        tree.left.left = new TreeNode(4);
        tree.right.right = new TreeNode(5);

        BTreeTraversals bTreeOps = new BTreeTraversals();
        // List<List<Integer>> result = bTreeOps.levelOrder(tree);
        List<List<Integer>> resultSpiral = bTreeOps.zigzagLevelOrder(tree);
        // System.out.println("Level Order Traversal: Default");
        // System.out.println(result);
        System.out.println("Level Order Traversal: Spiral");
        System.out.println(resultSpiral);
    }

}