/*Function to initialize an array to a specific value*/
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(){
  const int arraySampleSize = 5;
  int arraySample[arraySampleSize];

  for(int *i_beg = arraySample, *i_end = i_beg + arraySampleSize ; i_beg != i_end; i_beg++){
    *i_beg = 10;
  }
  for(int *i_beg = arraySample, *i_end = i_beg + arraySampleSize ; i_beg != i_end; i_beg++){
    cout << *i_beg << "\n";
  }
  cout << endl;
}