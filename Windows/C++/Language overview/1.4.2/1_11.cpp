#include<iostream>

int main(){
 /*for(int val = 10; val >= 0; --val){
    std::cout << val << std::endl;
  }*/
 int val = 10;
 while(val >= 0){
  std::cout << val << std::endl;
  val = val - 1;
 }
  return 0;
}