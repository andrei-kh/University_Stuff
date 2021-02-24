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
    public partial class Search_Customer : Form
    {
        public Search_Customer()
        {
            InitializeComponent();
        }

        private void Search_Customer_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'airlineDBDataSet.Customer_Details' table. You can move, or remove it, as needed.
            this.customer_DetailsTableAdapter.Fill(this.airlineDBDataSet.Customer_Details);
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            ((BindingSource)dataGridView1.DataSource).Filter = String.Format("FirstName LIKE '%{0}%'", textBox1.Text);
        }

        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            int id = Convert.ToInt32(dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Cells[0].Value);
            Customer_Form c_form = new Customer_Form(id);
            c_form.ShowDialog();
            this.customer_DetailsTableAdapter.Fill(this.airlineDBDataSet.Customer_Details);
        }
    }
}
