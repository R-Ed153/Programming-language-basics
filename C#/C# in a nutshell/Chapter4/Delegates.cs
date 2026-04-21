using System.Security.Cryptography;

public delegate int Transformer(int x);
public delegate void ProgressReporter(int percentComplete);

class Util
{
    public static void Transform(int[] values,Transformer t)
    {
        for(int i = 0; i < values.Length; i++)
            values[i] = t(values[i]);
    }
    public static void Hardwork(ProgressReporter p)
    {
        for(int i = 0; i < 10; i++)
        {
            p(i*10);
            System.Threading.Thread.Sleep(10);
        }
    }
}

class Test
{
    
    //Single-cast example
    /*
    static void Main()
    {
        int[] values = {1,2,3};
        Util.Transform(values,Square);
        foreach(int i in values)
        {
            Console.Write(i + " ");
        }
    }
    static int Square(int x){ return x * x;}*/

    //Multi-cast example
    
    static void Main()
    {
        ProgressReporter p = WriteProgressToConsole;
        p+= WriteProgressToFile;
        Util.Hardwork(p);
    }
    static void WriteProgressToConsole(int percentComplete)
    {
        Console.WriteLine(percentComplete);
    }
    static void WriteProgressToFile(int percentComplete)
    {
        System.IO.File.WriteAllText("Multicast Delegate Example.txt",percentComplete.ToString());
    }

    //a delegate to an instace method example
    /*
    static void Main(){
    X x = new X();
    ProgressReporter p_Instance = x.InstanceProgress;
    p_Instance(99);
    Console.WriteLine(p_Instance.Target == x);
    Console.WriteLine(p_Instance.Method);}
*/
}

class X
{
    public void InstanceProgress(int percentComplete)
    {
        Console.WriteLine(percentComplete);
    }
}