#include <iostream>

using namespace std;

int main() {
    int arr[5][5];
    int row = 0;
    int col = 0;

    for (int x = 0; x < 5; x++) {
        for (int i = 0; i < 5; i++) {
            cin >> arr[x][i];
            if(arr[x][i] == 1) {
                row = x+1;
                col = i+1;
                break;
            }
        }
    }

    int min_steps = abs(3 - row) + abs(3-col);

    cout << min_steps;
}