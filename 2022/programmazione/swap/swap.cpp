#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

int swap(int N, vector<int> &V) {
    // SCRIVI QUA IL TUO CODICE
    return 0;
}

int main() {

    // DECOMMENTA QUA SE VUOI LEGGERE DA FILE
    // freopen("input.txt", "r", stdin);   // File di input fornito dalla piattaforma
    // freopen("output.txt", "w", stdout); // File di output da caricare in piattaforma

    int N;
    cin >> N;
    vector<int> V(N);

    for(int i=0; i<N; i++) {
        cin >> V[i];
    }

    cout << swap(N, V) << endl;
    return 0;
}
