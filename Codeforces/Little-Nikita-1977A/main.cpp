#include <iostream>
 
using namespace std;
 
int main() {
    int w;
    cin >> w;
 
    for (int x = 0; x < w; x++) {
        int a, b;
        cin >> a >> b;
        if(b > a) {
            cout << "No" << endl;
            continue;
        } else if(a == b) {
            cout << "Yes" << endl;
            continue;
        }
        
        int r = a - b;
 
        if(r % 2 == 0) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
}