/*A prgram to build a vector from input integers and build an array from the vector*/
#include <iostream>
#include <vector>
#include <iterator>

using std::cerr;
using std::cin;
using std::cout;
using std::endl;

using std::vector;

int main()
{
  int input;
  vector<int> enteredInputs;
  vector<int>::iterator it = enteredInputs.begin();

  cout << "Enter integers to build a display an array from them" << endl;

  while(cin >> input || !cin.fail())
  {
    enteredInputs.push_back(input);
  }

  int *enteredInputArray = new int[enteredInputs.size()]();
  
  cout << "The entered integers are: ";
  for(vector<int>::iterator it = enteredInputs.begin(); it != enteredInputs.end(); ++it){
    *enteredInputArray = *it;
    cout << " " << *enteredInputArray;
    ++enteredInputArray;
    
  }
  delete enteredInputArray;
  return 0;

}