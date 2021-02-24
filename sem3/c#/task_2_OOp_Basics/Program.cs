using System;

namespace oop_basics
{
	class Program
	{

		static void Main(string[] args)
		{
			Console.Write("Input file: ");
			string input = "kira.txt";//Console.ReadLine();
			Text text = TextParser.ParseFile(input);
			text.Print();
			/* text.concordance.Sort(); */
			/* text.concordance.Print(); */
			/* Concordance c = new Concordance(); */
			/* c.Parse(text); */
			/* c.Sort(); */
			/* c.Print(); */
			Task2(text);
		}

		static void Task1(Text text)
		{
			text.Sort();
			text.Print();
		}

		static void Task2(Text text)
		{
			Sentence result = new Sentence();
			Console.Write("Input word length: ");
			int wl = 2;//Convert.ToInt32(Console.ReadLine());
			foreach(Sentence s in text)
			{
				Word eos = s.GetEndOfSentence();
				if(eos.FullLength == 1 && eos[0].IsEqualTo('?'))
				{
					foreach(Word w in s)
					{
						if(w.Length == wl && !result.Contains(w))
						{
							result.Add(w);
						}
					}
				}
			}
			Console.WriteLine(result.Length);
			result.PrintWords('\n');
		}

		static void Task3(Text text)
		{
			foreach(Sentence s in text)
			{
				for(int i = 0; i < s.Length;)
				{
					if(s[i][0].IsConsonant())
					{
						s.RemoveAt(i);
						continue;
					}
					i++;
				}
			}
			text.Print();
		}

		static void Task4(Text text)
		{
			Console.Write("Input substring: ");
			string substring = Console.ReadLine();
			Console.Write("Input word length: ");
			int wl = Convert.ToInt32(Console.ReadLine());
			foreach(Sentence s in text)
			{
				foreach(Word w in s)
				{
					if(w.Length == wl)
					{
						w.ReplaceWith(substring);
					}
				}
			}
			text.Print();
		}

		void Debug(Text text)
		{
			/* foreach(Sentence s in text) */
			/* { */
			/* 	for(int i = 0; i < s.Length; i++) */
			/* 	{ */
			/* 		if(s[i][0].IsConsonant()) */
			/* 		{ */
			/* 			s[i].Print(); */
			/* 			Console.Write(" -- starts with a consonant"); */
			/* 		} */
			/* 		else */
			/* 		{ */
			/* 			s[i].Print(); */
			/* 			Console.Write(" -- starts with a vowel"); */
			/* 		} */
			/* 		Console.Write('\n'); */
			/* 	} */
			/* } */
			/* tp.text.PrintAllWords('\n'); */
		}
	}
}
