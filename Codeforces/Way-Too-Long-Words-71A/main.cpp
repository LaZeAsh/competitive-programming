#include <iostream>

using namespace std;

int main() {
    int num;
    // First input (Number of lines)
    cin >> num;

    for (int x = 0; x < num; x++) {
        string input;
        cin >> input;

        if(input.length() > 10) {
            char first_char = input[0];
            char last_char = input[input.length() - 1];
            string length = to_string(input.length() - 2);
            string final_string = first_char + length + last_char;
            cout << final_string << endl;
        } else {
            cout << input << endl;
        }
    }
}