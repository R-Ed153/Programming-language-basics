#include <iostream>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;

using std::string;
using std::vector;

//Takes all the words input by the user and capitalizes them
int main()
{
  vector<string> totalUserInput;
  string userInput;
  cout << "Enter words to add and capitalize them:" << endl;
  while (cin >> userInput)
  {
    // input any number to break out of loop
    if (isdigit(userInput[0]))
    {
      break;
    }
    totalUserInput.push_back(userInput);
  }
  for (vector<string>::size_type word = 0; word != totalUserInput.size(); word++)
  {
    for (string::size_type letter = 0; letter != totalUserInput[word].size(); letter++)
    {
      totalUserInput[word][letter] = toupper(totalUserInput[word][letter]);
    }
  }
  for (vector<string>::size_type word = 0; word != totalUserInput.size(); word++)
  {
    if (word < totalUserInput.size() - 1)
    {
      totalUserInput[word] = totalUserInput[word] + ", ";
    }
    cout << totalUserInput[word]; 
    if ((word + 1) % 8 == 0)
    {
      cout << endl;
    }
  }
  cout << std::endl;
  return 0;
}