#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;

using std::string;

int main()
{
  string v1, v2;
  cout << "Enter two string literals to compare them:" << endl;
  cin >> v1 >> v2;

  if(v1 == v2){
    cout << "The two strings: v1 and v2 are equal";
  }
  else if(v1 > v2){
    cout << "v1 is greater than v2";
  }
  else{
    cout << "v2 is greater than v1";
  }
  return 0;
}