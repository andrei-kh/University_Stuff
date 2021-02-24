using System;
using System.Collections.Generic;
using System.Collections;

namespace oop_basics
{
	class Text : IEnumerable
	{
		List<Sentence> text = new List<Sentence>();
		public Concordance concordance = new Concordance();

		public int Length
		{
			get
			{
				return text.Count;
			}
		}

		public IEnumerator GetEnumerator()
		{
			// foreach(Sentence s in text)
			// {
			// 	yield return s;
			// }
			return text.GetEnumerator();
		}

		public void Add(Sentence s)
		{
			text.Add(s);
		}

		public void Print()
		{
			foreach(Sentence s in text)
			{
				s.Print();
			}
			Console.Write('\n');
		}

		public void PrintAllWords(char delimiter)
		{
			foreach(Sentence s in text)
			{
				s.PrintWords(delimiter);
			}
		}

		public void Sort()
		{
			SentenceComparer sc = new SentenceComparer();
			text.Sort(sc);
		}

		public void PrintEOS()
		{
			Word eos;
			foreach(Sentence s in text)
			{
				eos = s.GetEndOfSentence();
				eos.Print();
				Console.Write('\n');
			}
		}

		public Sentence this[int index]
		{
			get
			{
				return text[index];
			}
		}
	}

}
