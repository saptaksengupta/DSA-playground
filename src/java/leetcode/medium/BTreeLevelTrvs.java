import java.lang.System.Logger.Level;
import java.util.ArrayList;
import java.util.List;

// Generated By lexicon-dsa CLI tool.
// Author: Saptak Sengupta(deeps.sengupta@gmail.com)
// Github: https://github.com/saptaksengupta/

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

public class BTreeLevelTrvs {

    public List<List<Integer>> solution(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        int height = getHeight(root);
        for (int i = 1; i < height + 1; i++) {
            List<Integer> innerList = new ArrayList<Integer>();
            res.add(levelTravers(root, i, innerList));
        }
        return res;
    }

    public List<Integer> levelTravers(TreeNode root, int level, List<Integer> list) {
        if (root != null) {
            if (level == 1) {
                list.add(root.val);
                return list;
            } else if (level > 1) {
                list = levelTravers(root.left, level - 1, list);
                list = levelTravers(root.right, level - 1, list);
            }
        }
        return list;
    }

    public int getHeight(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int lHeight = getHeight(root.left) + 1;
        int rHeight = getHeight(root.right) + 1;

        return lHeight > rHeight ? lHeight : rHeight;
    }

    public static void main(String[] args) {

        TreeNode tree = new TreeNode(3);
        tree.left = new TreeNode(9);
        tree.right = new TreeNode(20);
        tree.right.left = new TreeNode(15);
        tree.right.right = new TreeNode(7);

        BTreeLevelTrvs bTreeOps = new BTreeLevelTrvs();
        List<List<Integer>> result = bTreeOps.solution(tree);
        System.out.println(result);
    }
}