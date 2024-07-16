import java.util.ArrayList;
import java.util.List;
    public class Main {
        public static void main(String[] args) {
        List<String> nomes = new ArrayList<>();
        nomes.add("João");
        nomes.add("Maria");
        nomes.add("Pedro");
        // Loop foreach para percorrer a lista de nomes
        for (String nome : nomes) {
         System.out.println(nome);
        }
    }
}
