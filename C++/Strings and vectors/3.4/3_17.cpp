#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;

using std::string;
using std::vector;

// returns the sum of the outer digits going inside and so on...
int main()
{
  vector<int> numberSet({10, 2, 3, 7, 78});
  vector<int> results;
  vector<int>::iterator iterStart = numberSet.begin();
  vector<int>::iterator iterEnd = (numberSet.end()) - 1;
  while (results.size() < numberSet.size() / 2)
  {
    results.push_back(*iterStart + *iterEnd);
    ++iterStart;
    --iterEnd;
  }
  if (numberSet.size() % 2 == 1)
  {
    results.push_back(*iterStart);
  }
  for (vector<int>::iterator printMembers = results.begin(); printMembers != results.end(); ++printMembers)
  {
    cout << *printMembers << endl;
  }
  return 0;
}