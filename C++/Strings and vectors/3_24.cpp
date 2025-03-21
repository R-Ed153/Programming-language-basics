/*set the bits of a bitset to the fibonacci pattern*/
#include <iostream>
#include <vector>
#include <bitset>
#include <cstddef>

using std::cin;
using std::cout;
using std::endl;

using std::bitset;
using std::string;
using std::vector;

using std::size_t;

int main()
{
  const int bitsetSize = 32;
  bitset<bitsetSize> fibonacci;
  int previousValue = 0;
  int currentValue = 1;
  while (currentValue + previousValue < bitsetSize)
  {
    int placeHolder = previousValue + currentValue;
    previousValue = currentValue;
    fibonacci.set(currentValue - 1);
    currentValue = placeHolder;
  }
  
  cout << fibonacci;
  cout << endl;
  return 0;
}