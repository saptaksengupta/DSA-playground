import java.util.HashMap;
import java.util.Iterator;
import java.util.TreeSet;

public class HashRepresentation {

    HashMap<Integer, TreeSet<Integer>> graph;
    static int V;

    public HashRepresentation() {
        graph = new HashMap<>();
        for (int i = 0; i < V; i++) {
            graph.put(i, new TreeSet<>());
        }
    }

    public void addEdge(int src, int dest) {
        graph.get(src).add(dest);

        // Undirected graph, add an edge
        // from dest to src as well
        graph.get(dest).add(src);
    }

    public void printGraph() {
        for (int i = 0; i < V; i++) {
            System.out.println("Adjacency list of vertex " + i);
            Iterator<Integer> set = graph.get(i).iterator();

            while (set.hasNext())
                System.out.print(set.next());

            System.out.println();
        }
    }

    public void searchEdge(int src, int dest) {
        
        String resp = "Edge From " + src + " to " + dest;
        if (graph.get(src).contains(dest)) {
            resp += " found";
        } else {
            resp += " not found";
        }

        System.out.println(resp);
    }

    public static void main(String[] args) {
        V = 5;
        HashRepresentation graph = new HashRepresentation();
        graph.addEdge(0, 1);
        graph.addEdge(0, 4);
        graph.addEdge(1, 2);
        graph.addEdge(1, 3);
        graph.addEdge(1, 4);
        graph.addEdge(2, 3);
        graph.addEdge(3, 4);

        graph.printGraph();

        graph.searchEdge(1, 4);
    }
}