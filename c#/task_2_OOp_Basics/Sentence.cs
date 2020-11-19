using System;
using System.Collections.Generic;
using System.Collections;

namespace oop_basics
{
	class Sentence : IEnumerable
	{
		private List<Word> sentence = new List<Word>();
		public int Length
		{
			get
			{
				return sentence.Count;
			}
		}

		public IEnumerator GetEnumerator()
		{
			foreach(Word w in sentence)
			{
				yield return w;
			}
		}

		public bool Contains(Word a)
		{
			foreach(Word w in sentence)
			{
				if(a.IsEqualTo(w))
				{
					return true;
				}
			}
			return false;
		}

		public void RemoveAt(int index)
		{
			if(Length != 1 && index == Length - 1)
			{
				Word eos = sentence[index].GetPunctuation();
				if(sentence[index - 1].HavePunctuation())
				{
					for(int i = sentence[index - 1].GetPunctuationIndex(); i < sentence[index - 1].Length; i++)
						sentence[index - 1].RemoveAt(i);
				}
				foreach(Character c in eos)
				{
					sentence[index - 1].Add(c);
				}
			}
			sentence.RemoveAt(index);

		}

		public void Add(Word w)
		{
			sentence.Add(w);
		}

		public void PrintWords(char delimiter)
		{
			foreach(Word w in sentence)
			{
				w.PrintWithoutPunctuation();
				Console.Write(delimiter);
			}
		}

		public void Print()
		{
			foreach(Word w in sentence)
			{
				w.Print();
				Console.Write(' ');
			}
		}

		public Word GetEndOfSentence()
		{
			return sentence[Length - 1].GetPunctuation();
		}

		public Word this[int index]
		{
			get
			{
				return sentence[index];
			}
		}

	}

}
