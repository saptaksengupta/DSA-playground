import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;

    public TreeNode(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class LcaUtil {
    public TreeNode getLca(TreeNode root, TreeNode p, TreeNode q ) {
        if (root == null) {
            return root;
        }

        if (root.value == p.value || root.value == q.value) {
            return root;
        }

        TreeNode left = getLca(root.left, p, q);
        TreeNode right = getLca(root.right, p, q);

        if (left != null && right != null) {
            return root;
        }

        return left != null ? left : right;
    }

}


class LowestCommonAncestor {
    public static void main(String[] args) {
        TreeNode tr = new TreeNode(1);

        tr.left = new TreeNode(2);
        tr.left.left = new TreeNode(4);
        tr.left.right = new TreeNode(5);
        tr.left.right.left = new TreeNode(6);
        tr.left.right.right = new TreeNode(7);

        tr.right = new TreeNode(3);
        tr.right.left = new TreeNode(8);
        tr.right.right = new TreeNode(9);
        
        LcaUtil lca = new LcaUtil();
        TreeNode res = lca.getLca(tr, new TreeNode(2), new TreeNode(6));
        System.out.print(res.value);
    }
}
