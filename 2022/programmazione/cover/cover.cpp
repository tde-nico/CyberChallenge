#include <stdio.h>
#include <iostream>
#include <vector>
#include <array>

using namespace std;

int conta(int N, int K, const vector<array<long long int, 2>> &ranges) {
    // SCRIVI QUA IL TUO CODICE
    return 0;
}

int main() {

    // freopen("input.txt", "r", stdin); // DECOMMENTA QUA SE VUOI LEGGERE DA FILE
    // freopen("output.txt", "w", stdout); // DECOMMENTA QUA SE VUOI SCRIVERE DA FILE

    int N, K;
    cin >> N >> K;
    vector<array<long long int, 2>> ranges(N);

    for(int i=0; i<N; i++) {
        cin >> ranges[i][0];
        cin >> ranges[i][1];
    }

    cout << conta(N, K, ranges);

    return 0;
}
