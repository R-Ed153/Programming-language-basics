#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;

using std::string;
using std::vector;

int main()
{
  vector<int> numberSet(10, 42);
  for (vector<int>::iterator setIndex = numberSet.begin(); setIndex != numberSet.end(); ++setIndex)
  {
    *setIndex = *setIndex * 2;
  }
  for (vector<int>::iterator setIndex = numberSet.begin(); setIndex != numberSet.end(); ++setIndex)
  {
    cout << *setIndex << endl;
  }
  return 0;
}