#include <iostream>
using std::cin;
using std::cout;
using std::endl;

int main()
{
  int exponent, base, result = 1;
  cout << "Enter a number and its exponent" << endl;
  cin >> base >> exponent;
  for(int counter = 0; counter <= exponent; counter++){
    result *= base;
  }
  cout << "Base: " << base << " exponent: " << exponent
   << " = " << result << endl;
  return 0;
}