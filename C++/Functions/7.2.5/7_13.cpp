/* functions to print sum of array elements*/
#include <iostream>
using std::cout;
using std::endl;

int arraySum(size_t arrayLength, const int array[])
{
  int result = 0;
  for (size_t i = 0; i < arrayLength; ++i)
  {
    result = result + array[i];
  }
  return result;
}

int arraySum1(const int *start, const int *end)
{
  int result = 0;
  while (start != end)
  {
    result = result + *start++;
  }
  return result;
}

int arraySum2(int (&arr)[4])
{
  int result = 0;
  for (int i = 0; i < 4; ++i)
  {
    result = result + arr[i];
  }
  return result;
}

int main()
{
  int testArray[4] = {7, 8, 9, 3};
  // cout << arraySum(sizeof(testArray)/sizeof(testArray[0]),testArray)<<endl;
  // cout << arraySum1(testArray,testArray + sizeof(testArray)/sizeof(testArray[0]))<<endl;
  cout << arraySum2(testArray) << endl;
  return 0;
}