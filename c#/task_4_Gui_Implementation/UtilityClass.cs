using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace task_4_Gui_Implementation
{
    static class UtilityClass
    {
        static public bool TextBoxesAreNullorEmpty(Control control)
        {
            if(control.Controls.OfType<TextBox>().Any(t => string.IsNullOrEmpty(t.Text)))
                return true;
            return false;
        }
        static public void traverseControlsAndSetTextEmpty(Control control)
        {
            foreach(var c in control.Controls)
            {
                if (c is TextBox)
                    ((TextBox)c).Text = string.Empty;
            }
        }
    }
}
