#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;

using std::string;

int main()
{
  string v1,input;
  cout << "Enter string literals to add them." << endl;
  while(cin >> input){
    v1 = v1 + input + " ";
    cout << v1 << endl;
  }
  return 0;  
}