#include <iostream>
using std::string;

class AbstractEmployee
{
    virtual void askForPromotion() = 0;
};

class Employee : AbstractEmployee
{
private:
    string Company;
    int Age;

protected:
    string Name;

public:
    void introduceYourself()
    {
        std::cout << "My name is " << Name << " and I'm " << Age << "years old" << std::endl;
    }
    void setName(string name)
    {
        Name = name;
    }
    string getName()
    {
        return Name;
    }

    void setCompany(string company)
    {
        Company = company;
    }
    string getCompany()
    {
        return Company;
    }

    void setAge(int age)
    {
        if (age >= 18)
        {
            Age = age;
        }
        else
        {
            std::cout << "Age cannot be less than 18 yrs" << std::endl;
        }
    }
    int getAge()
    {
        return Age;
    }

    void askForPromotion()
    {
        if (Age > 30)
        {
            std::cout << Name << " got promoted" << std::endl;
        }
        else
        {
            std::cout << Name << ",sorry no promotion for You!" << std::endl;
        }
    }
    virtual void work()
    {
        std::cout << Name << " is checking email, task backlog, performing tasks..." << std::endl;
    }
    Employee(string name, string company, int age)
    {
        Name = name;
        Company = company;
        Age = age;
    }
};

class Developer : public Employee
{
public:
    string FavProgrammingLanguage;
    Developer(string name, string company, int age, string favProgrammingLanguage) : Employee(name, company, age)
    {
        FavProgrammingLanguage = favProgrammingLanguage;
    }
    void fixBug()
    {
        std::cout << Employee::Name << " fixed bug using " << FavProgrammingLanguage << std::endl;
    }
    void work()
    {
        std::cout << Name << " is writing " << FavProgrammingLanguage << " code." << std::endl;
    }
};

class Teacher : public Employee
{
public:
    string Subject;
    void prepareLesson()
    {
        std::cout << Name << " is preparing " << Subject << " lesson." << std::endl;
    }
    void work()
    {
        std::cout << Name << " is teaching " << Subject << std::endl;
    }
    Teacher(string name, string company, int age, string subject) : Employee(name, company, age)
    {
        Subject = subject;
    }
};

int main()
{
    Employee employee1 = Employee("Edmund", "EdmundInc", 25);
    employee1.introduceYourself();
    employee1.askForPromotion();

    employee1.setAge(39);
    std::cout << employee1.getName() << " is " << employee1.getAge() << " years old" << std::endl;
    employee1.askForPromotion();

    employee1.setAge(15);
    std::cout << employee1.getName() << " is " << employee1.getAge() << " years old" << std::endl;

    Developer d = Developer("Ed", "Ed-Toons", 25, "C++");
    d.fixBug();
    d.askForPromotion();

    Teacher t = Teacher("Mom", "Thangira", 58, "English");
    t.prepareLesson();
    t.askForPromotion();

    /*d.work();
    t.work();*/

    // base class object
    Employee *e1 = &employee1;
    // derived class object
    Employee *e2 = &d;
    Employee *e3 = &t;

    (*e1).work();

    e2->work();
    e3->work();
}
