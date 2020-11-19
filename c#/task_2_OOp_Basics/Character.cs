using System;

namespace oop_basics
{
	class Character
	{
		enum charType
		{
			NUMERIC = 1,
			ALPHABETIC = 2,
			CAPITAL = 4,
			LOWER = 8,
			WHITESPACE = 16,
			PUNCTUATION = 32,
			END_OF_SENTENCE = 64,
			OTHER = 128
		}

		charType type = 0;
		public char symbol;

		public Character(char c)
		{
			symbol = c;
			if(c >= '0' && c <= '9')
				type |= charType.NUMERIC;
			else if(c >= 'A' && c <= 'Z')
				type |= charType.ALPHABETIC | charType.CAPITAL;
			else if(c >= 'a' && c <= 'z')
				type |= charType.ALPHABETIC | charType.LOWER;
			else if(c == ' ' || c == '\t' || c == '\n')
				type |= charType.WHITESPACE;
			else if(c == ',' || c == ';' || c == ':')
				type |= charType.PUNCTUATION;
			else if(c == '!' || c == '?' || c == '.')
				type |= charType.PUNCTUATION | charType.END_OF_SENTENCE;
			else
				type |= charType.OTHER;
		}

		/* public static bool operator ==(Character a, Character b) */
		/* { */
		/* 	return a.GetValue() == b.GetValue(); */
		/* } */

		/* public static bool operator !=(Character a, Character b) */
		/* { */
		/* 	return a.GetValue() != b.GetValue(); */
		/* } */

		/* public static bool operator ==(Character a, char b) */
		/* { */
		/* 	return a.GetValue() == b; */
		/* } */

		/* public static bool operator !=(Character a, char b) */
		/* { */
		/* 	return a.GetValue() != b; */
		/* } */


		public bool IsEqualTo(Character a)
		{
			return a.IsEqualTo(symbol);
		}

		public bool IsEqualTo(char a)
		{
			return Char.ToLower(symbol) == Char.ToLower(a);
		}

		public char GetValue()
		{
			return symbol;
		}

		public bool IsNumeric()
		{
			return (type & charType.NUMERIC) == charType.NUMERIC;
		}

		public bool IsAlphabetic()
		{
			return (type & charType.ALPHABETIC) == charType.ALPHABETIC;
		}

		public bool IsLower()
		{
			return (type & charType.LOWER) == charType.LOWER;
		}

		public bool IsCapital()
		{
			return (type & charType.CAPITAL) == charType.CAPITAL;
		}

		public bool IsWhitespace()
		{
			return (type & charType.WHITESPACE) == charType.WHITESPACE;
		}

		public bool IsPunctuation()
		{
			return (type & charType.PUNCTUATION) == charType.PUNCTUATION;
		}

		public bool IsEndOfSentence()
		{
			return (type & charType.END_OF_SENTENCE) == charType.END_OF_SENTENCE;
		}

		public bool IsVowel()
		{
			switch(symbol)
			{
				case 'A':
				case 'E':
				case 'I':
				case 'O':
				case 'U':
				case 'a':
				case 'e':
				case 'i':
				case 'o':
				case 'u': return true;
				default: return false;
			}
		}

		public bool IsConsonant()
		{
			return IsAlphabetic() && !IsVowel();
		}

		public bool IsNewline()
		{
			return symbol == '\n';
		}

		public void Print()
		{
			Console.Write(symbol);
		}
	}
}
