#include <iostream>

int main(){
  int sum = 0;
  int i = 50;
  /*for(int i = 50; i <= 100; i++){
    sum = sum + i;
  }  */
  while(i <= 100){
    sum = sum + i;
    i = i + 1; 
  }
  std::cout << "Sum = " << sum << std::endl;
  return 0;
}