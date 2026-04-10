public class Stock
{
    decimal currentPrice;
    public decimal CurrentPrice
    {
        get {return currentPrice;}
        set{currentPrice = value;}
    }

    public static void Main()
    {
        Stock NSC = new Stock();
        NSC.CurrentPrice = 20;
        Console.WriteLine(NSC.CurrentPrice);
    }
}