using System;
using System.Collections.Generic;

namespace oop_basics
{
	class SentenceComparer : IComparer<Sentence>
	{
		public int Compare(Sentence a, Sentence b)
		{
			if(a.Length < b.Length)
				return -1;
			if(a.Length == b.Length)
				return 0;
			return 1;
		}
	}
}
