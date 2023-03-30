
# Stasis 2.0

First created 2011, version 2 2022

In Stasis, every program has an eternal balance. The average of all variables is always zero.
When one variable changes, all the others adjust to compensate. One can’t program in the language without accounting for every piece of data and how it relates to every other piece of data.

```c
void main()
{
	int a, b = 5;
	Console.WriteLine(a);
}
```
The program above is attempting to print the value of a, but a was never assigned. We might expect the result to be zero (or undefined), but instead we get:
```
-2.5
```

## Notes

This is a partial implementation for the language, making Stasis-aware variables available in C#. A full implementation would allow only these variables. 

Stasis 2.0 fixes a major issue with the language itself. Previously, arrays and strings were added at the same time, so that one character in a string would not affect another, but rather the entire string would shift collectively. In the new 