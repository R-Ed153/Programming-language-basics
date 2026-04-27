#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;

using std::string;
using std::vector;

//returns the sum of the outer digits going inside and so on...
int main()
{
  vector<int> numberSet({10, 2, 3, 45,78});
  vector<int> results;
  for (vector<int>::size_type i = 0; i != numberSet.size() / 2; ++i)
  {
    results.push_back(numberSet[i] + numberSet[numberSet.size() - 1 - i]);
  }
  if (numberSet.size() % 2 == 1)
  {
    results.push_back(numberSet[numberSet.size() / 2]);
  }
  for(vector<int>::size_type i = 0; i != results.size(); i++){
    cout << results[i] << endl ;
  }
  
  return 0;
}