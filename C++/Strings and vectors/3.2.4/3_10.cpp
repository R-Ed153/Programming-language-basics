#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;

using std::string;

int main(){
  string input,result;
  cout << "Input a string to strip it of all punctuation: " << endl;
  cin >> input ;
  for(string::size_type i = 0 ; i < input.size(); ++i){
    if(!ispunct(input[i])){
      result += input[i];
    }
  }
  cout << result << endl ;
  return 0;
}