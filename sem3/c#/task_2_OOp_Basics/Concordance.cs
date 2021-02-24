using System;
using System.Collections.Generic;

namespace oop_basics
{
	class ConcordanceItem
	{
		public Word word;
		public int count;
		public List<int> references;
	}

	class Concordance
	{
		List<ConcordanceItem> concordance = new List<ConcordanceItem>();

		public void Add(Word w, int sentence_number)
		{
			int index = IndexOf(w);
			if(index != -1)
			{
				concordance[index].count++;
				if(!concordance[index].references.Contains(sentence_number))
					concordance[index].references.Add(sentence_number);
			}
			else
			{
				ConcordanceItem ci = new ConcordanceItem();
				ci.word = w;
				ci.count = 1;
				ci.references = new List<int>();
				ci.references.Add(sentence_number);
				concordance.Add(ci);
			}
		}

		public bool Contains(Word w)
		{
			foreach(ConcordanceItem ci in concordance)
			{
				if(ci.word.IsEqualTo(w))
					return true;
			}
			return false;
		}

		public int IndexOf(Word w)
		{
			for(int i = 0; i < concordance.Count; i++)
			{
				if(concordance[i].word.IsEqualTo(w))
					return i;
			}
			return -1;
		}

		public void Parse(Text text)
		{
			for(int i = 0; i < text.Length; i++)
			{
				foreach(Word w in text[i])
				{
					Add(w, i);
				}
			}
		}

		public void Print()
		{
			char group_name = '\0';
			foreach(ConcordanceItem ci in concordance)
			{
				if(!ci.word[0].IsEqualTo(group_name))
				{
					group_name = Char.ToUpper(ci.word[0].GetValue());
					Console.Write("\n{0}\n\n", group_name);
				}
				ci.word.PrintWithoutPunctuation();
				Console.Write("..........{0:d}:", ci.count);
				foreach(int number in ci.references)
				{
					Console.Write("{0:d} ", number);
				}
				Console.WriteLine();
			}
		}

		public void Sort()
		{
			WordAlphabeticComparer wac = new WordAlphabeticComparer();
			concordance.Sort(wac);
		}
	}
}
