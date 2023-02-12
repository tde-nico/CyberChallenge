import java.util.*;
import java.io.File;
import java.io.PrintStream;
import java.io.FileNotFoundException;

public class ppo {

    public static int controlla(int N, int V[]) {
        // SCRIVI QUA IL TUO CODICE
        return 0;
    }

    public static void main(String[] args) throws FileNotFoundException {

        // Se vuoi leggere/scrivere da linea di comando decommenta qua
        Scanner scanner = new Scanner(System.in);

        // Se vuoi leggere/scrivere da file decommenta qua
        // Scanner scanner = new Scanner(new File("input.txt")); // Input fornito dalla piattaforma
        // PrintStream fileStream = new PrintStream("output.txt"); // Output da inviare alla piattaforma
        // System.setOut(fileStream);

        int N = scanner.nextInt();
        scanner.nextLine(); // Move scanner to the next line
        int[] V = new int[N];

        for(int i=0; i<N; i++) {
            V[i] = scanner.nextInt();
        }

        System.out.println(swap(N, V));
    }
}
