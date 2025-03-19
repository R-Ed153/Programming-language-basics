#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;

using std::string;

int main(){
  string result;
  while(getline(cin,result)){
    cout << result << endl;
  }
  return 0;
}