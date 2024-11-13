#include <iostream>

using namespace std;

int main() {
    int num_cases;
    cin >> num_cases;

    for (int x = 0; x < num_cases; x++) {
        int l, r, k;
        cin >> l >> r >> k;
        int output = 0;
        for (int i = l; r >= i; i++) {
            int temp = 1;
            int num_occurences = 0;
            while (i * temp <= r) {
                num_occurences += 1;
                temp += 1;
            }

            if(num_occurences >= k) output += 1;
        }

        cout << output << endl;
    }
}