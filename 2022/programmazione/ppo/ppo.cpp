#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int controlla(string nuova, string vecchia) {
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
    string nuova, vecchia;

    cin >> N;

    for(int i=0; i<N; i++) {
        cin >> nuova >> vecchia;
        cout << controlla(nuova, vecchia) << endl;
    }

    return 0;
}
