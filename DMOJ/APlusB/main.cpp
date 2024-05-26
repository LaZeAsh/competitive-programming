#include <iostream>

using namespace std;

int main() {
    int num;
    cin >> num;

    for (int x = 0; x < num; x++) {
        int input1, input2;
        cin >> input1 >> input2;

        cout << (input1 + input2) << endl;
    }
}