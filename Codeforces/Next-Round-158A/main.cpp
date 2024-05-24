#include <iostream>

using namespace std;

int main() {
    int n = 0;
    int k = 0;
    cin >> n;
    cin >> k;
    int arr[n];
    int counter = 0;
    for (int x = 0; x < n; x++) {
        cin >> arr[x];
    }

    if (arr[k - 1] == 0) {
        // backward for loop
        for (int x = k-2; x > -1; x--) {
            if (arr[x] != 0) {
                counter = x+1;
                break;
            }
        }
    } else {
        // forward for loop
        counter = k;
        for (int x = k; x < n; x++) {
            if(arr[x] == arr[k-1]) {
                counter++;
            } 
        }
    }

    cout << counter;
}