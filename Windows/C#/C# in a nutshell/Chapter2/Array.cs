using System;
using System.Drawing;

class Test
{
    public struct Point_S{public int X,Y;};
    public class Point_C{public int X,Y;};
    int [,] matrix_R = new int [3,3];
    int [][] matrix_J = new int[3][];
    
    public static void Main()
    {
        char[] vowels = {'a','e','i','o','u'};  
        int[] a = new int[1000];
        Console.WriteLine(a[123]); 

        Point_S[] ab= new Point_S[1000];
        Console.WriteLine(ab[500].X); 

        Point_C[] ac= new Point_C[1000];
        Console.WriteLine(ac[500].X);

        /*for (int i = 0; i < vowels.Length; i++)
        {
            Console.WriteLine(vowels[i]);
        }*/
    }
}