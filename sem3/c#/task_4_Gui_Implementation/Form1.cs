using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace task_4_Gui_Implementation
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            AirlineDBEntities db = new AirlineDBEntities();
            if (UserText.Text != string.Empty && PasswordText.Text != string.Empty)
            {
                var user = db.Admin.Where(x => x.Username.Equals(UserText.Text)).SingleOrDefault();
                if (user != null)
                {
                    if (user.Password.Equals(PasswordText.Text))
                    {
                        MainForm mainForm = new MainForm();
                        this.Hide();
                        mainForm.ShowDialog();
                        this.Close();
                    }
                    else
                    {
                        MessageBox.Show("Wrong Password");
                    }
                }
                else
                {
                    MessageBox.Show("Wrong Username");
                }
            }
            else
            {
                MessageBox.Show("Please fill both fields");
            }
        }
    }
}
