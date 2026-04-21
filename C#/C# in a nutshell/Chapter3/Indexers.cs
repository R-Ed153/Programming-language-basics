class Sentence
{
    string[] words = "The quick brown fox".Split();
    public string this[int wordNum]
    {
        get {return words[wordNum];}
        set{words [wordNum] = value;}
    }

    public static void Main()
    {
        Sentence s = new Sentence();
        Console.WriteLine(s[3]);
        s[3] = "kangaroo";
        Console.WriteLine(s[3]);
    }
}