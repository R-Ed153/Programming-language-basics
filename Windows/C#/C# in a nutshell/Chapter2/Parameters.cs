using System.Text;
//parameter passed by value
/*class Test
{
    static void Foo(int p)
    {
        p++;
        Console.WriteLine(p);
    }
    static void Main()
    {
        int x = 8;
        Foo(x);
        Console.WriteLine(x);
    }
}*/


//parameter passed a copy of reference
/*class Test
{
    static void Foo(StringBuilder fooSB)
    {
        fooSB.Append("test");
        fooSB = null;
    }
    static void Main()
    {
        StringBuilder sb = new StringBuilder();
        Foo(sb);
        Console.WriteLine(sb.ToString());
    }
}*/

//parameter passed using ref modifier
/*
class Test
{
    static void Foo(ref int p)
    {
        p = p + 1;
        Console.WriteLine(p);
    }

    static void Swap(ref string a, ref string b)
    {
        string temp = a;
        a = b;
        b = temp;
    }

    static void Main()
    {
        int x = 8;
        Foo(ref x);
        Console.WriteLine(x);

        string a = "Penn";
        string b = "Teller";
        Swap(ref a, ref b);
        Console.WriteLine(a);
        Console.WriteLine(b);
    }
}*/

//parameter passed by the out modifier
/*class Test
{
    static void Split(string name, out string firstNames,out string lastName)
    {
        int i = name.LastIndexOf(' ');
        firstNames = name.Substring(0,i);
        lastName = name.Substring(i+1);

    }

    static void Main()
    {
        Split("Stevie Ray Vaughan",out string a,out string b);
        Console.WriteLine(a);
        Console.WriteLine(b);
    }
}*/

//Named arguments
class Test
{

    static void Foo(int x, int y)
    {
        Console.WriteLine(x + ", " + y);
    }

    static void Main()
    {
        int a = 0;
        Foo(y: ++a, x: --a);
    }
}