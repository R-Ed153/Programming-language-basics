#include <iostream>

int main()
{
  int val1, val2;
  std::cout << "Enter two numbers" << std::endl;
  std::cin >> val1 >> val2;
  if(val1 >= val2){
    std::cout << "val1: " << val1 << std::endl;
  }
  else{
    std::cout << "val2: " << val2 << std::endl;
  }
  return 0;
}