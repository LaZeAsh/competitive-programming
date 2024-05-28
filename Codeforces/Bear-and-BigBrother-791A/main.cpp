#include <iostream>

using namespace std;

int main() {
    int limak;
    cin >> limak;
    int bob;
    cin >> bob;

    for (int x = 1; true; x++) {
        limak = limak * 3;
        bob = bob * 2;
        if (limak > bob) {
            cout << x;
            break;
        }
    }
}