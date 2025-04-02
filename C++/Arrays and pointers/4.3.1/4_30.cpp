/*A program to cat together two strings (C and C++)*/
#include <iostream>
#include <string>
#include <cstring>

using std::cin;
using std::cout;
using std::endl;

using std::string;

/* C
int main()
{
  const char *v1 = "Edna";
  const char *v2 = "Edmund";
  char *catString = new char[strlen(v1) + strlen(v2) + 1]();
  strcat(catString,v2);
  strcat(catString,v1);
  // cout << strlen(v1) << " : " << strlen(v2) << endl;
  cout << catString;
  return 0;
}*/

/*C++*/
int main(){
  string v1 = "Edna";
  string v2 = "Edmund";

  string catString = v1 + v2;
  cout<<catString<<endl;

  return 0;
}