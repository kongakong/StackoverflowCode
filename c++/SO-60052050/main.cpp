#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
    int var;
    cout << "What size do you want to choose: "<< endl;
    cin >> var;

    int arr[var];
    arr[0] = 10;
    cout << arr[0] << endl;
}
