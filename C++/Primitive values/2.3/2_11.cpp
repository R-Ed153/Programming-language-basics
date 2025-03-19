#include<iostream>

int main(){
  std::cout << "Enter a base followed by an exponent" << std::endl;
  int base, exponent;
  int result = 1;
  std::cin >> base >> exponent;
  
  for(int counter = 0; counter < exponent; ++counter)
  {
    result *= base;
  }
 
 std::cout << "Answer = " << result << std::endl;
}