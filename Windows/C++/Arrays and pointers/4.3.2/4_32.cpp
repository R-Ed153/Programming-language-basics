// program to initialize a vcetor from an array
#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;

using std::vector;
 
int main()
{
  const size_t arraySize = 10;
  int originArray[arraySize] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
  vector<int> targetVector;

  for (int *pStart = originArray, *pEnd = originArray + arraySize; *pStart != *pEnd; ++pStart)
  {
    cout << *pStart << endl;
  }
}