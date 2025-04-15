/* Function to print options passed to a program*/
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(int argc, char *argv[])
{
  for (int a = 1; a < argc; a++)
  {
    cout << argv[a] << endl;
  }
  return 0;
}
