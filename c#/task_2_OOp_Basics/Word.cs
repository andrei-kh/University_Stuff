using System;
using System.Collections.Generic;
using System.Collections;

namespace oop_basics
{
	class Word : IEnumerable
	{
		List<Character> word = new List<Character>();

		public int FullLength
		{
			get
			{
				return word.Count;
			}
		}

		public int Length
		{
			get
			{
				int counter = 0;
				foreach(Character c in word)
				{
					if(!c.IsPunctuation())
						counter++;
				}
				return counter;
			}
		}

		public bool IsEqualTo(Word a)
		{
			if(a.Length == Length)
			{
				for(int i = 0; i < Length; i++)
				{
					if(!a[i].IsEqualTo(this[i]))
						return false;
				}
				return true;
			}
			return false;
		}

		/* public static bool operator ==(Word a, Word b) */
		/* { */
		/* 	if(a.Length == b.Length) */
		/* 	{ */
		/* 		for(int i = 0; i < a.Length; i++) */
		/* 		{ */
		/* 			if(a[i] != b[i]) */
		/* 				return false; */
		/* 		} */
		/* 		return true; */
		/* 	} */
		/* 	return false; */
		/* } */

		/* public static bool operator ==(Word a, Word b) */
		/* { */
		/* 	if(a.Length != b.Length) */
		/* 	{ */
		/* 		for(int i = 0; i < a.Length; i++) */
		/* 		{ */
		/* 			if(a[i] == b[i]) */
		/* 				return false; */
		/* 		} */
		/* 		return true; */
		/* 	} */
		/* 	return false; */
		/* } */

		public Character this[int index]
		{
			get
			{
				return word[index];
			}
		}

		public IEnumerator GetEnumerator()
		{
			foreach(Character c in word)
			{
				yield return c;
			}
		}

		public int GetPunctuationIndex()
		{
			int i = word.Count - 1;
			while(word[i].IsPunctuation())
			{
				i--;
			}
			return i;
		}

		public void Add(Character c)
		{
			word.Add(c);
		}

		public void Insert(int index, Character c)
		{
			word.Insert(index, c);
		}

		public void RemoveAt(int index)
		{
			word.RemoveAt(index);
		}

		public bool IsEndOfSentence()
		{
			return word[word.Count - 1].IsEndOfSentence();
		}

		public void PrintWithoutPunctuation()
		{
			foreach(Character c in word)
			{
				if(!c.IsPunctuation())
				{
					c.Print();
				}
			}
		}

		public void Print()
		{
			foreach(Character c in word)
				c.Print();
		}

		public bool HavePunctuation()
		{
			return word[word.Count - 1].IsPunctuation();
		}

		public Word GetPunctuation()
		{
			Word punctuation = new Word();
			int i = word.Count - 1;
			while(word[i].IsPunctuation())
			{
				punctuation.Insert(0, word[i]);
				i--;
			}
			return punctuation;
		}

		public void ReplaceWith(string s)
		{
			if(HavePunctuation())
			{
				Word punct = GetPunctuation();
				word.Clear();
				foreach(char c in s)
				{
					Character ch = new Character(c);
					Add(ch);
				}
				foreach(Character c in punct)
				{
					Add(c);
				}
			}
			else
			{
				word.Clear();
				foreach(char c in s)
				{
					Character ch = new Character(c);
					Add(ch);
				}
			}
		}

	}

}
