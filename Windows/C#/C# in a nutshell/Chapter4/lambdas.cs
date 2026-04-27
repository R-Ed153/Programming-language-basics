static void Main()
{
    int factor = 2;
    Func <int,int> multiplier = n => n * factor;
    factor = 10;
    Console.Write(multiplier(3));
}