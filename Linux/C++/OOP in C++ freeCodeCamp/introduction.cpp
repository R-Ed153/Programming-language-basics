#include <iostream>
using std::string;

class Employee{
public:    
    string Name;
    string Company;
    int Age;

    void introduceYourself(){
        std::cout<<"Name = "<< Name<< std::endl;
        std::cout<<"Company - "<< Company << std::endl;
        std::cout<<"Age -  "<< Age << std::endl;
    }
    Employee(string name, string company, int age){
        Name = name;
        Company = company;
        Age = age;

    }
};

int main(){
    //basic class initialization
    /*Employee employee1;
    employee1.Name = "Edmund";
    employee1.Company = "EdmundInc";
    employee1.Age = 25;
    employee1.introduceYourself();*/

    //default constructor
    //Employee employee2;
    /*employee2.Name = "John";
    employee2.Company = "Amazon";
    employee2.Age = 35;*/
    //employee2.introduceYourself();

    //classes with constructors
    Employee employee3 = Employee("Edmund","EdmundInc", 25);
    employee3.introduceYourself();
}