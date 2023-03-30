using System;
using System.Text;

namespace Rottytooth.Esolangs.Stasis
{

    public static class Runtime
    {
        internal static List<Variable> Variables = new List<Variable>();

        public static void Register(Variable vbl)
        {
            // This should not be the case
            if (Variables.Contains(vbl))
                return; 

            // Get size of list
            int size = 0;
            Variables.ForEach(e => size += e.Size);

            if (size == 0)
            {
                vbl.RawValue = 0.0;
            }
            else
            {
                // Recalculate everything based on the new value
                Variables.ForEach(e => e.ApplyOffset(vbl.RawValue / Convert.ToDouble(size)));
            }

            Variables.Add(vbl);
        }
    }
}
