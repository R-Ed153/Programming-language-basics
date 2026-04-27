#include <iostream>

int main()
{
  int val1;
  int counter = 0;
  std::cout << "Enter a series of numbers." << std::endl;
  while(std::cin >> val1)
  {
    if(val1 < 0){
      counter += 1;
    }
  } 
  std::cout << "Negative numbers entered = " << counter << std::endl;
  return 0;
}