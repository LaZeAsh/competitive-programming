#include <iostream>

using namespace std;

int main() {
    int num;
    cin >> num;
    int a = 0;
    for (int x = 0; x < num; x++) {
        string input;
        cin >> input;
        if (input.find("++") != string::npos) {
            a++;
        } else if (input.find("--") != string::npos) {
            a--;
        }
    }

    cout << a;
}