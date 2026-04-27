public class Asset
{
    public string Name;
    public virtual decimal Liability {get{return 0;}}
}

public class Stock : Asset
{
    public long SharesOwned;
}

public class House : Asset
{
    public decimal Mortgage;
    public sealed override decimal Liability{get{return Mortgage;}}
}