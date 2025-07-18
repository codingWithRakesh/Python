#include <iostream>
using namespace std;

int main() {
    int n = 5;
    int marks[n];
    
    for(int i = 0; i < n; i++){
        cout << "enter marks : ";
        cin >> marks[i];
    }
    
    for(int i = 0; i < n; i++){
        cout << marks[i] << " ";
    }
    cout << endl;
    
    int f = 0;
    int l = n -1;
    while(f<l){
        swap(marks[f++],marks[l--]);
    }
    
    for(int i = 0; i < n; i++){
        cout << marks[i] << " ";
    }
    

    return 0;
}
