class Test{
    static int Calc(int x){
        return 10/x
    }
    static void Main(){
        try{
            int y= Calc(0)
            Console.WriteLine(y);
        }
        catch(DivideByZeroException ex){
            Console.WriteLine("x cannot be zero");
        }
        finally{
            Console.WriteLine("program completed.")
        }
    }
}