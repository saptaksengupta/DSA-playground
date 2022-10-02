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

class RightView {
    private List<Integer> list = new ArrayList<>();
    private void travers(TreeNode node, int level) {
        if (node == null) {
            return;
        }

        if (list.size() == level) {
            list.add(node.value);
        }

        travers(node.right, level + 1);
        travers(node.left, level + 1);
    }

    public List<Integer> getRightView(TreeNode root) {
        travers(root, 0);
        return list;
    }
}

class LeftView {
    private List<Integer> list = new ArrayList<>();
    private void travers(TreeNode node, int level) {
        if (node == null) {
            return;
        }

        if (list.size() == level) {
            list.add(node.value);
        }

        travers(node.left, level + 1);
        travers(node.right, level + 1);
    }

    public List<Integer> getLeftView(TreeNode root) {
        travers(root, 0);
        return list;
    } 
}


class RightAndLeftViewBinaryTree {
    public static void main(String[] args) {
        TreeNode tr = new TreeNode(1);

        tr.left = new TreeNode(2);
        tr.left.left = new TreeNode(4);
        tr.left.right = new TreeNode(5);
        tr.left.right.left = new TreeNode(10);

        tr.right = new TreeNode(3);
        tr.right.right = new TreeNode(7);
        
        RightView rv = new RightView();
        System.out.print(rv.getRightView(tr));

        LeftView lv = new LeftView();
        System.out.print(lv.getLeftView(tr));
    }
}
