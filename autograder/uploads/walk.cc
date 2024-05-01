#include <iostream>
#include <string>
using namespace std;

int main()
{
    string name1, name2;
    cout << "Enter a name:";
    getline(cin, name1);
    cout << "Enter a name:";
    getline(cin, name2);
    cout << name1 << " and " << name2 << " went for a walk.\n";
    return 0
}
