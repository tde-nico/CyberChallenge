import java.util.*;
import java.io.File;
import java.io.PrintStream;
import java.io.FileNotFoundException;

public class ppo {

    public static int controlla(String nuova, String vecchia) {
        System.out.println(nuova);
        System.out.println(vecchia);
        // SCRIVI QUA IL TUO CODICE
        // RITORNA 0 SE LA NUOVA PASSWORD NON SEGUE LE SPECIFICHE
        // RITORNA 1 SE LA NUOVA PASSWORD SEGUE LE SPECIFICHE 
        return 1;
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

        for(int i=0; i<N; i++) {
            String[] line = scanner.nextLine().split(" ");
            String nuova = line[0];
            String vecchia = line[1];
            System.out.println(controlla(nuova, vecchia));
        }

    }
}
