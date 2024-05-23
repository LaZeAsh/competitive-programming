#include <iostream>

using namespace std;

int main() {
    int num;
    cin >> num;
    int counter = 0;

    for (int x = 0; x < num; x++) {
        int a, b, c;
        cin >> a >> b >> c;

        if((a + b + c) >= 2) {
            counter += 1;
        }
    }

    cout << counter;
}