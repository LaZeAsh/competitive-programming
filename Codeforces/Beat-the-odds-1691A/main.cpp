#include <iostream>

using namespace std;

int main() {
    int num_cases = 0;
    cin >> num_cases;

    while(num_cases--) {
        int num_int = 0; cin >> num_int;
        // int total = 0;
        // int temp = 0; cin >> temp;
        int num_odd = 0;
        // while(num_int--) {
        for (int i = 0; i < num_int; i++) {
            int n; cin >> n;
            if(n % 2 != 0) num_odd += 1;
        }
        
        cout << min(num_odd, num_int - num_odd) << endl;
    }
}