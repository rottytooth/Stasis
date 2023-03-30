using System;
using System.Text;

namespace Rottytooth.Esolangs.Stasis
{
    public abstract class Variable
    {
        internal double _rawValue = 0.0;
        internal virtual double RawValue {
            get { return _rawValue; }
            set { _rawValue = value; }
        }

        public virtual int Size
        {
            get { return 1; }
        }

        public void Adjust(double offset)
        {
            this.RawValue -= offset;
        }

        public virtual void ApplyOffset(double offset)
        {
            this.RawValue -= offset;
        }
    }

    public class Float : Variable
    {
        public Float() { }
        public Float(double value)
        {
            this.Value = value;
        }
        public double Value
        {
            set
            {
                this.RawValue = Convert.ToDouble(value);
                Runtime.Register(this);
            }
            get
            {
                return this.RawValue;
            }
        }
        public static implicit operator Float(double value)
        {
            return new Float(value);
        }
        public override string ToString()
        {
            return this.Value.ToString();
        }
    }

    public class Char : Variable
    {
        public Char() { }
        public Char(char value)
        {
            this.Value = value;
        }

        public char Value
        {
            set
            {
                this.RawValue = value;
                Runtime.Register(this);
            }
            get
            {
                return (char)Convert.ToInt32(Math.Round(this.RawValue, MidpointRounding.AwayFromZero));
            }
        }
        public static implicit operator Char(char value)
        {
            return new Char(value);
        }
        public override string ToString()
        {
            return this.Value.ToString();
        }
    }

    public class String : Variable
    {
        private List<Char> RawValues = new List<Char>();

        public String() { }
        public String(string value)
        {
            this.Value = value;
        }
        public String(params double[] value)
        {
            this.RawValues = new List<Char>();
            foreach (char v in value)
            {
                this.RawValues.Add(new Char(v));
            }
        }

        public override int Size
        {
            get { return this.RawValues.Count; }
        }

        public string Value
        {
            set
            {
                this.RawValues = new List<Char>();
                foreach (char v in value)
                {
                    this.RawValues.Add(new Char(v));
                }
            }
            get
            {
                var sb = new StringBuilder();
                for (int i = 0; i < this.RawValues.Count; i++)
                {
                    sb.Append(this.RawValues[i].Value);
                }
                return sb.ToString();
            }
        }
        public static implicit operator String(string value)
        {
            return new String(value);
        }
        public override void ApplyOffset(double offset)
        {
            this.RawValues.ForEach(e => e.ApplyOffset(offset));
        }
        public override string ToString()
        {
            return this.Value;
        }
    }
}
