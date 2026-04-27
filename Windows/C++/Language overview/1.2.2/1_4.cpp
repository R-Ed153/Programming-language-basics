#include<iostream>

int main(){
  int var1, var2;
  std::cout << "Enter two numbers:" << std::endl;
  std::cin >> var1 >> var2;
  std::cout << "The product of the two numbers " << var1 << " and " << var2; 
  std::cout << " is: " << var1 * var2
  << std::endl;
  return 0;
}