using System;
using System.Runtime.CompilerServices;
using System.Text;

class Test
{
    /*static void Main()
    {
        StringBuilder ref1 = new StringBuilder("object1");
        Console.WriteLine(ref1);

        StringBuilder ref2 = new StringBuilder("object2");
        StringBuilder ref3 = ref2;

        Console.WriteLine(ref3);
    }*/
    static int x;
    static void Main()
    {
        // int x;
        Console.WriteLine(x);
        int[] ints = new int[2];
        Console.WriteLine(ints[0]);
    }
}