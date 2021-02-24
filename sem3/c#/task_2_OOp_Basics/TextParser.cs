using System;
using System.IO;

namespace oop_basics
{
	static class TextParser
	{
		static Text text = new Text();
		static Sentence sentence = new Sentence();
		static Word word = new Word();

		public static Text ParseFile(string filename)
		{
			StreamReader sr = File.OpenText(filename);
			int number = 1;
			string s;
			while((s = sr.ReadLine()) != null)
			{
				ParseString(s, number);
				number++;
			}
			return text;
		}

		public static Text ParseString(string s, int line_number = 1)
		{
			s += ' ';
			foreach(char c in s)
			{
				Character character = new Character(c);
				if(!character.IsWhitespace())
				{
					word.Add(character);
				}
				else
				{
					if(word.Length != 0)
					{
						text.concordance.Add(word, line_number);
						sentence.Add(word);
						if(word.IsEndOfSentence())
						{
							text.Add(sentence);
							sentence = new Sentence();
						}
						word = new Word();
					}
				}
			}
			return text;
		}
	}
}
