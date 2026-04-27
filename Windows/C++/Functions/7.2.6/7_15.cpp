/*Function to print the sum of two numbers entered as program parameters*/
#include<iostream>
#include <string>

using std::string;
using std::stoi; 

using std::cin;
using std::cout;
using std::endl;

int main(int argc, char *argv[]){
  int result = 0;
  result = stoi(argv[1]) + stoi(argv[2]);  
  cout << "Result: "<< result << endl;
}