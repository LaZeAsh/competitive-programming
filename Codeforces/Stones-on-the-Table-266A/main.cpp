#include <iostream>

using namespace std;

int main() {
    int num;
    cin >> num;
    string s;
    cin >> s;
    int counter = 0;
    char last = 'a';

    for (int x = 0; x < num; x++) {
        if(s[x] == last) {
            counter++;
        }
        last = s[x];
    }

    cout << counter;
}