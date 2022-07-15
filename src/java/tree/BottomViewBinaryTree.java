import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.TreeMap;

class Touple {
    TreeNode node;
    int row;

    public Touple(TreeNode _node, int _row) {
        this.node = _node;
        this.row = _row;
    }
}

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


class BottomViewBinaryTree {
    
    private static List<Integer> getBottomView(TreeNode root) {
        Map<Integer, Integer> map = new TreeMap<>();
        Queue<Touple> q = new LinkedList<>();
        q.offer(new Touple(root, 0));
        while(!q.isEmpty()) {
            Touple current = q.poll();
            TreeNode cNode = current.node;
            int x = current.row;

            map.put(x, cNode.value);

            if (null != cNode.left) {
                q.offer(new Touple(cNode.left, x - 1));
            }

            if (null != cNode.right) {
                q.offer(new Touple(cNode.right, x + 1));
            }
        }

        List<Integer> list = new ArrayList<>();
        for (Map.Entry<Integer, Integer> vertical : map.entrySet()) {
            list.add(vertical.getValue());
        }

        return list;
    }

    public static void main(String[] args) {
        TreeNode tr = new TreeNode(1);

        tr.left = new TreeNode(2);
        tr.left.left = new TreeNode(4);
        tr.left.right = new TreeNode(5);
        tr.left.right.left = new TreeNode(8);

        tr.right = new TreeNode(3);
        tr.right.left = new TreeNode(6);
        tr.right.right = new TreeNode(7);
        tr.right.left.right = new TreeNode(9);
        
        System.out.print(BottomViewBinaryTree.getBottomView(tr));
    }
}
