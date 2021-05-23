package basics.graph;
import java.util.*;

public class Bfs {
    public static void main(String[] args) {
        Graph g = new Graph(4);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);

        g.printAdjList();

        System.out.print("\n");
        g.bfs(2);
    }
}

class Graph {
    private int v;
    private LinkedList<Integer> adj[];

    Graph(int v) {
        this.v = v;
        adj = new LinkedList[v];
        for (int i = 0; i < v; i++) {
            adj[i] = new LinkedList<Integer>();
        }
    }

    public void addEdge(int v, int w) {
        adj[v].add(w);
    }

    public void printAdjList() {
        for (int i = 0; i < this.v; i++) {
            System.out.print("Node - " + i + ": ");
            Iterator<Integer> it = adj[i].listIterator();
            while (it.hasNext()) {
                System.out.print(it.next() + " ");
            }
        }
    }

    public void bfs(int start) {
        boolean visited[] = new boolean[this.v];

        LinkedList<Integer> queue = new LinkedList<Integer>();

        queue.add(start);
        visited[start] = true;

        while (queue.size() != 0) {

            int s = queue.poll();
            System.out.print(s);

            Iterator<Integer> i = adj[s].listIterator();
            while (i.hasNext()) {
                int n = i.next();
                if (visited[n] == false) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }
}
