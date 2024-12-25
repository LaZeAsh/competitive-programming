#include <iostream>
#include <math.h>
#include <unordered_map>

using namespace std;

int helper(long long number, unordered_map<long long, long long>& arr) {
    if(number / 4 < 1) return 1;

    if(arr[number]) return arr[number];

    arr[number] = helper(floor(number / 4), arr);
    return 2 * arr[number];
}

int main() {
    int t; cin >> t;

    while(t--) {
        long long n; cin >> n;
        unordered_map<long long, long long> arr;
        cout << helper(n, arr) << endl;
    }
}
