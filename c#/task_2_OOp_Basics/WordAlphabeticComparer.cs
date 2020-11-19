using System;
using System.Collections.Generic;

namespace oop_basics
{
	class WordAlphabeticComparer : IComparer<ConcordanceItem>
	{
		public int Compare(ConcordanceItem a, ConcordanceItem b)
		{
			int len = Math.Min(a.word.Length, b.word.Length);
			for(int i = 0; i < len; i++)
			{
				if(Char.ToLower(a.word[i].GetValue()) < Char.ToLower(b.word[i].GetValue()))
					return -1;
				if(Char.ToLower(a.word[i].GetValue()) > Char.ToLower(b.word[i].GetValue()))
					return 1;
			}
			if(a.word.Length == b.word.Length)
				return 0;
			return a.word.Length < b.word.Length ? -1 : 1;
		}
	}
}

