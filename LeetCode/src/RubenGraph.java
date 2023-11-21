import java.util.ArrayList;
import java.util.LinkedList;

public class RubenGraph {
    ArrayList< ArrayList<Integer> > RubenGraph; // create a ArrayList of ArrayLists
    int nodes;

    public RubenGraph(int nodes){
        RubenGraph=new ArrayList<>();  //Initiliaze ArrayList of ArrayLists
        this.nodes=nodes;
        for(int i=0; i<nodes;i++){
            RubenGraph.add(new ArrayList<>()); //Inittilize inner arraylist
        }
    }

    public void addEdge(int nodes, int source){
        RubenGraph.get(nodes).add(source);
        RubenGraph.get(source).add(nodes);
    }
    public void printRubenList(){ 
        
        for(int i=0; i<RubenGraph.size();i++){
            System.out.print("Node "+ i+ "-->");
            for(int j=0;j<RubenGraph.get(i).size();j++){
                System.out.print(RubenGraph.get(i).get(j)+"---");
            };
            System.out.println();
        }

    }
}
