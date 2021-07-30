import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;

public class TopologicalSort {

    static Map<Integer, List<Integer>> createGraph(int v) {
        Map<Integer, List<Integer>> adj = new HashMap<Integer, List<Integer>>();
        for (int i = 0; i < v; i++) {
            adj.put(i, new ArrayList<>());
        }

        adj.get(2).add(3);

        adj.get(3).add(1);

        adj.get(4).add(0);
        adj.get(4).add(1);

        adj.get(5).add(0);
        adj.get(5).add(2);

        return adj;
    }

    static void dfsSort(Map<Integer, List<Integer>> adj, Integer item, int[] visited, Stack<Integer> list) {
        visited[item] = 1;
        List<Integer> adjItems = adj.get(item);
        for (int i = 0; i < adjItems.size(); i++) {
            if (visited[adjItems.get(i)] != 1) {
                dfsSort(adj, adjItems.get(i), visited, list);
            }
        }
        list.push(item);
    }

    static Stack<Integer> topoSort(Map<Integer, List<Integer>> adj, Integer n) {
        Stack<Integer> list = new Stack<Integer>();

        int visited[] = new int[n];

        for (int i = 0; i < n; i++) {
            if (visited[i] != 1) {
                dfsSort(adj, i, visited, list);
            }
        }

        return list;
    }

    public static void main(String[] args) {
        Map<Integer, List<Integer>> adj = createGraph(6);
        Stack<Integer> result = topoSort(adj, 6);
        System.out.println("One of it's Topological order is:  ");
        while (!result.empty()) {
            System.out.print(result.pop() + " ");
        }
    }
}