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
    public partial class Search_flight : Form
    {
        public Search_flight()
        {
            InitializeComponent();
        }

        private void Search_flight_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'airlineDBDataSet1.Flight_Details' table. You can move, or remove it, as needed.
            this.flight_DetailsTableAdapter.Fill(this.airlineDBDataSet1.Flight_Details);

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            ((BindingSource)dataGridView1.DataSource).Filter = "Convert(Id, 'System.String') like '%" + textBox1.Text + "%'";
        }
        private void dataGridView1_CellClick_1(object sender, DataGridViewCellEventArgs e)
        {
            int id = Convert.ToInt32(dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Cells[0].Value);
            Flight_info f_form = new Flight_info(id);
            f_form.ShowDialog();
            this.flight_DetailsTableAdapter.Fill(this.airlineDBDataSet1.Flight_Details);
        }
    }
}
