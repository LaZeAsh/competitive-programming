#include <iostream>

using namespace std;

int main() {
    int input;
    cin >> input;
    int solutions = 0;
    for (int x = 0; x < input; x++) {
        int remainder = input - x;

        if (remainder < x || remainder > 5) {
            continue;
        } 

        solutions++;
    }

    cout << solutions;
}