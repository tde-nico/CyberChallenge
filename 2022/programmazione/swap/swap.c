#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#define MAXLEN 32

int swap(int N, int *V) {
    // SCRIVI QUA IL TUO CODICE
    return 0;
}

int main() {

    // DECOMMENTA QUA SE VUOI LEGGERE DA FILE
    // freopen("input.txt", "r", stdin);   // File di input fornito dalla piattaforma
    // freopen("output.txt", "w", stdout); // File di output da caricare in piattaforma

    int N;
    assert(1 == scanf("%d\n", &N));

    int *V = (int *) malloc(N * sizeof(int));

    for(int i=0; i<N; i++) {
        assert(1 == scanf("%d", &V[i]));
    }

    printf("%d\n", swap(N, V));
    free(V);
    return 0;
}
