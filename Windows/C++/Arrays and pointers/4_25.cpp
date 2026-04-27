/*Enter two strings, C++ and C, to compare them*/
#include <iostream>
#include <string>
#include <cstring>

using std::cin;
using std::cout;
using std::endl;

using std::string;

/*
C++
int main(){
  string v1,v2;
  cout<<"Enter two strings to compare them"<<endl;
  cin>>v1>>v2;
  if (v1 == v2){
    cout << "String " << v1 << " is equal to " << v2;
  }
  else if(v1 > v2){
    cout << "String " << v1 << " is greater than " << v2;
  }
  else{
    cout << "String " << v1 << " is smaller than " << v2;
  }
  return 0;
}
*/

int main()
{
  char *v1 = new char[20];
  char *v2 = new char[20];
  cout << "Enter two strings to compare them" << endl;
  cin >> v1 >> v2;
  if (strcmp(v1, v2) == 0)
  {
    cout << "String " << v1 << " is equal to " << v2;
  }
  else if (strcmp(v1, v2) > 0)
  {
    cout << "String " << v1 << " is greater than " << v2;
  }
  else
  {
    cout << "String " << v1 << " is smaller than " << v2;
  }
  delete v1;
  delete v2;
  return 0;
}
