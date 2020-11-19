using System;

namespace task
{
    class Program_1
    {
        static bool IsAllDigits(string c_num)
        {
            foreach (char c in c_num)
            {
                if(!char.IsDigit(c))
                    return false;
            }

            return true;
        }
        static bool CheckSum(string c_num)
        {
            int sum = 0;

            for (int i = 1; i < c_num.Length; i += 2)
            {
                int product = (c_num[i] - '0') * 2;
                sum += product / 10 + product % 10;
            }

            for (int i = 0; i < c_num.Length; i += 2)
                sum += c_num[i] - '0';

            //Console.Write(sum + "\n");

            if(sum % 10 == 0)
                return true;
            
            return false;
        }
        static void Ma1n(string[] args)
        {
            while(true)
            {
                Console.Write("Number: ");
                string c_num = Console.ReadLine();
                
                while(!IsAllDigits(c_num))
                {
                    Console.Write("Retry: ");
                    c_num = Console.ReadLine();
                }

                string card_name =  "INVALID";


                if(c_num.Length == 15 && c_num[0] == '3' && (c_num[1] == '4' || c_num[1] == '7'))
                    card_name = "AMEX\n";
                else if(c_num.Length == 16 && c_num[0] == '5' && (c_num[1] >= '1' && c_num[1] <= '5'))
                    card_name = "MASTERCARD\n";
                else if((c_num.Length == 13 || c_num.Length == 16) && c_num[0] == '4')
                    card_name = "VISA\n";
                                
                if(card_name != "INVALID\n" && !CheckSum(c_num))
                    card_name = "INVALID\n";

                Console.Write(card_name);   
            }
        }
    }
}
