using System;
namespace Rottytooth.Esolangs.Stasis
{
    public static class ValueBuilder
    {
        public static double[] Build(params double[] targets)
        {
            // assumes a holder var to start things off -- TODO: make that a param

            double[] output = new double[targets.Length];

            for(int i = targets.Length-1;i >= 0; i--)
            {
                double workVal = targets[i];
                for (int j = i + 1; j < targets.Length; j++)
                {
                    workVal += output[j] / (j + 1);
                }
                output[i] = workVal;
            }   

            return output;  
        }
    }
}

