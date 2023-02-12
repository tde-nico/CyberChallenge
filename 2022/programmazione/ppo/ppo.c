#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#define MAXLEN 32

int controlla(char *nuova, char *vecchia) {
    // SCRIVI QUA IL TUO CODICE
    // RITORNA 0 SE LA NUOVA PASSWORD NON SEGUE LE SPECIFICHE
    // RITORNA 1 SE LA NUOVA PASSWORD SEGUE LE SPECIFICHE 
    return 1;
}

int main() {

    // DECOMMENTA QUA SE VUOI LEGGERE DA FILE
    // freopen("input.txt", "r", stdin);   // File di input fornito dalla piattaforma
    // freopen("output.txt", "w", stdout); // File di output da caricare in piattaforma

    int N;
    char *nuova = (char *) malloc(MAXLEN * sizeof(char));
    char *vecchia = (char *) malloc(MAXLEN * sizeof(char));

    assert(1 == scanf("%d\n", &N));

    for(int i=0; i<N; i++) {
        assert(2 == scanf("%s %s\n", nuova, vecchia));
        printf("%s %s\n", nuova, vecchia);
        printf("%d\n", controlla(nuova, vecchia));
    }

    free(nuova);
    free(vecchia);
    return 0;
}
