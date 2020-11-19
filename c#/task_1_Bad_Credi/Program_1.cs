using System;

namespace task
{
    class Program
    {
        public enum CardType
        {
            VISA,
            AMEX,
            MASTERCARD,
            INVALID
        }
        static bool IsAllDigits(string c_num)
        {
            foreach (char c in c_num)
            {
                if (!char.IsDigit(c))
                    return false;
            }

            return true;
        }
        static bool IsValidCheckSum(string c_num)
        {
            int sum = 0;

            for (int i = 1; i < c_num.Length; i += 2)
            {
                int product = (c_num[i] - '0') * 2;
                sum += product / 10 + product % 10;
            }

            for (int i = 0; i < c_num.Length; i += 2)
                sum += c_num[i] - '0';

            if (sum % 10 == 0)
                return true;

            return false;
        }
        public static CardType GetCardType(string number)
        {
            if (IsValidCheckSum(number))
                if (number.Length == 15 && number.StartsWith("34") || number.StartsWith("37"))
                    return CardType.AMEX;
                else if (number.Length == 16 && number[0] == '5' && (number[1] >= '1' && number[1] <= '5'))
                    return CardType.MASTERCARD;
                else if ((number.Length == 13 || number.Length == 16) && number.StartsWith('4'))
                    return CardType.VISA;

            return CardType.INVALID;
        }
        static void Main(string[] args)
        {
            while (true)
            {
                Console.Write("Number: ");
                string c_num = Console.ReadLine();

                while (!IsAllDigits(c_num))
                {
                    Console.Write("Retry: ");
                    c_num = Console.ReadLine();
                }

                CardType card_type = GetCardType(c_num);


                switch (card_type)
                {
                    case CardType.AMEX:
                        Console.Write("AMEX\n");
                        break;
                    case CardType.MASTERCARD:
                        Console.Write("MASTERCARD\n");
                        break;
                    case CardType.VISA:
                        Console.Write("VISA\n");
                        break;
                    default:
                        Console.Write("INVALID\n");
                        break;
                }
            }
        }
    }
}
