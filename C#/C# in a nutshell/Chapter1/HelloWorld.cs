using System;

class Test
{
    static void Main()
    {
        int x = 12 * 30;
        Console.WriteLine(x);
        Console.WriteLine(FeetToInches(100));

        UnitConvertor feetToInchesConvertor = new UnitConvertor(30);
        UnitConvertor milesToFeetConvertor = new UnitConvertor(5280);

        Console.WriteLine(feetToInchesConvertor.Convert(100));
        Console.WriteLine(feetToInchesConvertor.Convert(milesToFeetConvertor.Convert(1)));
    }

    static int FeetToInches(int feet)
    {
        int inches = feet * 12;
        return inches;
    }

    public class UnitConvertor
    {
        int ratio;
        public UnitConvertor(int unitRatio)
        {
            ratio = unitRatio;
        }
        public int Convert (int unit){return unit * ratio;}
    }
}

