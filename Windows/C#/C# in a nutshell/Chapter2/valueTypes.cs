using System;


class Test{
    
public struct PointStruct{public int X,Y;};
public class PointClass{public int X,Y;};

static void Main()
{
    PointStruct p1_s = new PointStruct();
    p1_s.X = 7;

    PointStruct p2_s = p1_s;
    Console.WriteLine(p1_s.X);
    Console.WriteLine(p2_s.X);

    p1_s.X = 9;
    Console.WriteLine(p1_s.X);
    Console.WriteLine(p2_s.X);

    PointClass p1_c = new PointClass();
    p1_c.X = 7;

    PointClass p2_c = p1_c;
    Console.WriteLine(p1_c.X);
    Console.WriteLine(p2_c.X);

    p1_c.X = 9;
    Console.WriteLine(p1_c.X);
    Console.WriteLine(p2_c.X);

    Console.WriteLine(double.NegativeInfinity);
}
}


