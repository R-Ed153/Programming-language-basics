public class Asset
{
    public string Name;
}

public class Stock : Asset
{
    public long SharesOwned;
}
public class House : Asset
{
    public decimal Mortgage;

}
public class Test
{
    //Polymorphism
    public static void Display(Asset asset)
    {
        Console.WriteLine(asset.Name);
    }
    public static void Main()
    {

        //Inheritance
        Stock msft = new Stock { Name = "MSFT", SharesOwned = 1000 };
        Console.WriteLine(msft.Name);
        Console.WriteLine(msft.SharesOwned);
        House mansion = new House { Name = "Mansion", Mortgage = 250000 };
        Console.WriteLine(mansion.Name);
        Console.WriteLine(mansion.Mortgage);
        //Polymorphism
        Display(mansion);


        //Upcasting and downcasting
        Stock NSC = new Stock { Name = "NSC", SharesOwned = 5000 };
        Asset a = NSC;
        Console.WriteLine(a == NSC);
        Console.WriteLine(a.Name);
        Console.WriteLine(NSC.SharesOwned);
       //Error code
       /* House s = a as House;
        Console.WriteLine(s.Name);*/

    }
}