import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.TreeMap;

class Touple {
    TreeNode node;
    int row;
    int col;

    public Touple(TreeNode _node, int _row, int _col) {
        this.node = _node;
        this.row = _row;
        this.col = _col;
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

public class VarticalTraversal {

    public static List<List<Integer>> getVarticalOrderList(TreeNode root) {
        TreeMap<Integer, TreeMap<Integer, PriorityQueue<Integer>>> map  = new TreeMap<>();
        Queue<Touple> q = new LinkedList<Touple>();
        q.offer(new Touple(root, 0, 0));
        
        while(!q.isEmpty()) {
            Touple current = q.poll();
            TreeNode cNode = current.node;
            int x = current.row;
            int y = current.col;
            
            if (!map.containsKey(x)) {
                map.put(x, new TreeMap<>());
            }
            if(!map.get(x).containsKey(y)) {
                map.get(x).put(y, new PriorityQueue<>());
            }

            // add the item in the pQueue.
            map.get(x).get(y).offer(cNode.value);

            if (null != cNode.left) {
                q.offer(new Touple(cNode.left, x - 1, y + 1));
            }

            if (null != cNode.right) {
                q.offer(new Touple(cNode.right, x + 1, y + 1));
            }
        }


        List<List<Integer>> list = new ArrayList<>();
        for(TreeMap<Integer, PriorityQueue<Integer>> verticals: map.values()) {
            list.add(new ArrayList<>());
            for (PriorityQueue<Integer> level : verticals.values()) {
                while (!level.isEmpty()) {
                    list.get(list.size() - 1).add(level.poll());
                }
            }
        }
        return list;
    }

    public static void main(String[] args) {
        TreeNode tr = new TreeNode(1);
        tr.left = new TreeNode(2);
        tr.left.left = new TreeNode(4);
        tr.left.right = new TreeNode(10);
        tr.left.left.right = new TreeNode(5);
        tr.left.left.right.right = new TreeNode(6);

        tr.right = new TreeNode(3);
        tr.right.left = new TreeNode(9);
        tr.right.right = new TreeNode(10);

        System.out.println(VarticalTraversal.getVarticalOrderList(tr));
    }
}
