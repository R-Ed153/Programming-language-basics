public delegate T Transformer<T>(T arg);

public class Util
{
    public static void Transform<T>(T[] values,Transformer<T> t)
    {
        for(int i= 0; i < values.Length; i++)
            values[i] = t(values[i]);
    }
}

class Test
{
    static void Main()
    {
        int[] values={1,2,3};
        Util.Transform(values.Square);
        foreach(int i in values)
            Console.Write(i+ " ");
    }
    static int Square(int x)
    {
        return x * x;
    }
}