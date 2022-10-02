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

class RootToNodePathFinder {
    
    public List<Integer> getRootToNodePath(TreeNode root, int node) {
        List<Integer> list = new ArrayList<>();
        traversFromRootToNode(root, node, list);
        return list;
    }

    public Boolean traversFromRootToNode(TreeNode root, int nodeVal, List<Integer> list) {
        
        if (root == null) {
            return false;
        }
        
        list.add(root.value);
        if (root.value == nodeVal) {
            return true;
        }

        Boolean lVal = traversFromRootToNode(root.left, nodeVal, list);
        Boolean rVal = traversFromRootToNode(root.right, nodeVal, list); 
        if (lVal || rVal) {
            return true;
        }

        list.remove(list.size() - 1);
        return false;
    }

}


class RootToNodePath {
    public static void main(String[] args) {
        TreeNode tr = new TreeNode(1);

        tr.left = new TreeNode(2);
        tr.left.left = new TreeNode(4);
        tr.left.right = new TreeNode(5);
        tr.left.right.left = new TreeNode(6);
        tr.left.right.right = new TreeNode(7);

        tr.right = new TreeNode(3);
        
        RootToNodePathFinder rnp = new RootToNodePathFinder();
        System.out.print(rnp.getRootToNodePath(tr, 7));
    }
}
