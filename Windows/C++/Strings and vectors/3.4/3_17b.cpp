#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;

using std::string;
using std::vector;

int main()
{
  vector<string> totalUserInput;
  string userInput;

  cout << "Enter words to add and capitalize them:" << endl;
  while (cin >> userInput)
  {
    if (isdigit(userInput[0]))
    {
      break;
    }
    totalUserInput.push_back(userInput);
  }

  // Capitalize every letter of input words
  for (vector<string>::iterator userInputWords = totalUserInput.begin(); userInputWords != totalUserInput.end(); userInputWords++)
  {
    string words = *userInputWords;
    for (string::iterator wordsLetters = words.begin(); wordsLetters != words.end(); wordsLetters++)
    {
      *wordsLetters = toupper(*wordsLetters);
    }
    *userInputWords = words;
  }
  // Arrange and print every input word
  vector<string>::size_type counter = 0; // for formatting the output
  for (vector<string>::iterator userInputWords = totalUserInput.begin(); userInputWords != totalUserInput.end(); userInputWords++)
  {
    cout << *userInputWords;
    if ((counter + 1) % 8 == 0)
    {
      cout << "\n";
    }
    else 
    {
     cout << ","; 
    }
    counter++;
  }
  cout << std::endl;
  return 0;
}