using Rottytooth.Esolangs.Stasis;

void HelloWorld(params double[] results)
{
    Float j = 0;
    //var hw = new Rottytooth.Esolangs.Stasis.String(results);
    var hw = new Rottytooth.Esolangs.Stasis.String(601, 420.6666666666667, 320.75, 256.6, 216.33333333333333, 128.85714285714286, 101.37499999999999, 139, 147.60000000000002, 136, 119.16666666666666, 103.53846153846153, 33);
    Console.WriteLine(hw);

    Console.WriteLine("\n");
    foreach (char c in hw.Value)
    {
        Console.Write((int)c);
        Console.Write(" ");
    }
}

void SampleTest123()
{
    Float holder = 0;
    Float fl_a = 3.5;
    Console.WriteLine("A: {0}", fl_a);
    Float fl_b = 3;
    Console.WriteLine("A: {0}", fl_a);
    Float fl_c = 3;
    Console.WriteLine("A: {0}", fl_a);
    //Rottytooth.Esolangs.Stasis.String str1 = "This is a test";

    Console.WriteLine();
    Console.WriteLine("A: {0}", fl_a);
    Console.WriteLine("B: {0}", fl_b);
    Console.WriteLine("C: {0}", fl_c);
}

void HelloWorldCalculateTest()
{
    double[] results = ValueBuilder.Build(71, 101, 108, 108, 111, 45, 32, 87, 112, 114, 108, 101, 33);

    HelloWorld(results);

    Console.WriteLine();
    foreach (double result in results)
    {
        Console.Write(" {0}", result);
    }
}


HelloWorld();

SampleTest123();
