#include <iostream>
#include <map>
using namespace std;

int main() {
    string input;
    cin >> input;
    map<char, int> distinct_chars;

    for (int x = 0; x < input.length(); x++) {
        if(distinct_chars.find(input[x]) == distinct_chars.end()) {
            distinct_chars.insert({input[x], 0});
        }
    }

    if(distinct_chars.size() % 2 == 0) {
        cout << "CHAT WITH HER!";
    } else {
        cout << "IGNORE HIM!";
    }
}