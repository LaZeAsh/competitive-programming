#include <iostream>
#include <algorithm> // Include for transform

using namespace std;

int main() {
    string input1;
    cin >> input1;
    string input2;
    cin >> input2;
    transform(input1.begin(), input1.end(), input1.begin(), [](unsigned char c) {return tolower(c);});
    transform(input2.begin(), input2.end(), input2.begin(), [](unsigned char c) {return tolower(c);});

    if(input1 < input2) {
        cout << -1;
    } else if(input1 > input2) {
        cout << 1;
    } else {
        cout << 0;
    }
}