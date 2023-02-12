import java.util.*;
import java.io.File;
import java.io.PrintStream;
import java.io.FileNotFoundException;

public class cover {

    public static int conta(int N, int K, long ranges[][]) {
        // SCRIVI QUA IL TUO CODICE
        return 0;
    }

    public static void main(String[] args) throws FileNotFoundException {

        // Se vuoi leggere/scrivere da linea di comando decommenta qua
        Scanner scanner = new Scanner(System.in);

        // Se vuoi leggere/scrivere da file decommenta qua
        // Scanner scanner = new Scanner(new File("input.txt"));
        // PrintStream fileStream = new PrintStream("output.txt");
        // System.setOut(fileStream);

        int N = scanner.nextInt();
        int K = scanner.nextInt();
        scanner.nextLine(); // Move scanner to the next line

        long[][] ranges = new long[N][2];

        for(int i=0; i<N; i++) {
            ranges[i][0] = scanner.nextLong();
            ranges[i][1] = scanner.nextLong();
            scanner.nextLine();
        }

        System.out.println(conta(N, K, ranges));

    }
}
