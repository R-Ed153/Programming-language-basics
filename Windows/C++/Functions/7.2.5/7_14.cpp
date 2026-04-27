/*sum of numbers in a vector*/
#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::cerr;

using std::vector;

int sumVector(vector<int>::const_iterator beg, vector<int>::const_iterator end){
 int count = 0;
  while(beg != end){
    count = count + *beg++;
  }
  return count;
}

int main(){
  vector<int> test = {1,2,3,4,5};
  vector<int>::iterator beg;
  vector<int>::iterator end;
  cout << "The sum of numbers: "<<sumVector(beg = test.begin(),end = test.end());
  return 0;
}