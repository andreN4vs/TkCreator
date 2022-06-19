using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp4
{
    public partial class teste_2 : Form
    {
        public teste_2()
        {
            InitializeComponent();
        }

 
        
        private void teste_2_Load(object sender, EventArgs e)
        {

        }

        private void CreatButton() 
        {

            // Creating and setting the properties of Button
            Button Mybutton = new Button();
            Mybutton.Location = new Point(225, 198);

            // Adding this button to form
            this.Controls.Add(Mybutton);

            ControlExtension.Draggable(Mybutton, true);

        }

        private void button1_Click(object sender, EventArgs e)
        {

           
            
        }

        private void button1_MouseDown(object sender, MouseEventArgs e)
        {
            
        }

        private void telinha_DragEnter(object sender, DragEventArgs e)
        {
                
        }

        private void telinha_DragDrop(object sender, DragEventArgs e)
        {
            CreatButton();
        }

        private void button1_DragLeave(object sender, EventArgs e)
        {

        }

        private void button1_DragOver(object sender, DragEventArgs e)
        {

        }
    }
}
