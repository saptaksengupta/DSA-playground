import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

public class Bipartite {

    static Map<Integer, List<Integer>> createGraph(int v) {
        Map<Integer, List<Integer>> adj = new HashMap<Integer, List<Integer>>();
        for(int i = 1; i <= v; i++) {
            adj.put(i, new ArrayList<>());
        }

       adj.get(1).add(2);

       adj.get(2).add(1);
       adj.get(2).add(3);
       adj.get(2).add(8);

       adj.get(3).add(2);
       adj.get(3).add(4);

       adj.get(4).add(2);
       adj.get(4).add(5);

       adj.get(5).add(4);
       adj.get(5).add(6);
       adj.get(5).add(8);

       adj.get(6).add(5);
       adj.get(7).add(6);

       adj.get(8).add(2);
       adj.get(8).add(5);

       return adj;
    }
    
    static Boolean isBipertite(int n) {
        Map<Integer, List<Integer>> adj = createGraph(n);
        int colors[] = new int[n + 1];

        for(int i = 0; i <= n; i++) {
            colors[i] = -1;
        }

        for (int i = 0; i < n; i++) {
            if (colors[i] == -1) {
                if(!checkBfs(i + 1, adj, colors)){
                    return false;
                }
            }
        }
        return true;
    }

    static boolean checkBfs(int v, Map<Integer, List<Integer>> adj, int[] colors) {
        Queue<Integer> queue = new LinkedList<Integer>();
        
        queue.add(v);
        colors[v] = 1;

        while(!queue.isEmpty()) {
            int top = queue.poll();
            List<Integer> list = adj.get(top);

            for(int i = 0; i < list.size(); i++) {
                if(colors[list.get(i)] == -1) {
                    colors[list.get(i)] = 1 - colors[top];
                    queue.add(list.get(i));
                } else if (colors[list.get(i)] == colors[top]){
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int n = 8;
        Boolean result = isBipertite(n);
        System.out.println(result);
    }
}