using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;


namespace WindowsFormsApp4
{
    public partial class TkCreator : Form
    {
        //primeiras linhas (chama a biblioteca e cria a tela)
        string patern = ("from tkinter import *" + "\r\n" + "from tkinter import font" + "\r\n\r\n" + "windowDesign = Tk()" + "\r\n\r\n" + "windowDesign.title('Design Window')" + "\r\n" + "windowDesign.geometry('960x687+426+321')" + "\r\n\r\n\r\n" + "windowDesign.mainloop()");
        
        //ler arquivo
        StreamReader read = null;

        public TkCreator()
        {
            InitializeComponent();

            //escreve as primeiras linhas
            txt_code.Text = patern;

            //adiciona scroll bars
            txt_code.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
        }




        //metodo pare salvar e criar pasta
        private void SaveFile(string ext)
        {
            saveFileDialog1.DefaultExt = ext;
            try
            {
                if (this.saveFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    FileStream fs = new FileStream(saveFileDialog1.FileName, FileMode.OpenOrCreate, FileAccess.Write);
                    StreamWriter sr = new StreamWriter(fs);
                    sr.Flush();
                    sr.BaseStream.Seek(0, SeekOrigin.Begin);
                    sr.Write(txt_code);
                    sr.Flush();
                    sr.Close();


                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("ERRO DE NA GRAVAÇÃO" + ex.Message, "ERRO", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        // cria pasta e txt
        private void txtToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SaveFile(".txt");
        }

        //cria pasta em .py
        private void pyToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SaveFile(".py");
        }



        //altera o ta nho da fonte 
        private void LatterSize(string x = "Microsoft Sans Serif", int y = 10)
        {
            txt_code.Font = new Font(x, y);
        }

        //aumenta x5
        private void xToolStripMenuItem_Click(object sender, EventArgs e)
        {
            LatterSize("Microsoft Sans Serif", 5);
        }

        //aumenta x10
        private void xToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            LatterSize("Microsoft Sans Serif", 10);
        }

        //aumenta x15
        private void xToolStripMenuItem2_Click(object sender, EventArgs e)
        {
            LatterSize("Microsoft Sans Serif", 15);
        }

        //aumenta x20
        private void xToolStripMenuItem3_Click(object sender, EventArgs e)
        {
            LatterSize("Microsoft Sans Serif", 20);
        }

        //aumenta x25
        private void xToolStripMenuItem4_Click(object sender, EventArgs e)
        {
            LatterSize("Microsoft Sans Serif", 25);
        }

        //aumenta x50
        private void xToolStripMenuItem5_Click(object sender, EventArgs e)
        {
            LatterSize("Microsoft Sans Serif", 50);
        }



        //copia o codigo 
        private void copyToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Clipboard.SetText(txt_code.Text);
        }

        // abilita a escrita no codigo
        private void enableEditingToolStripMenuItem_Click(object sender, EventArgs e)
        {
            txt_code.ReadOnly = false;
        }

        //desabilita a escrita no codigo 
        private void disableEditingToolStripMenuItem_Click(object sender, EventArgs e)
        {
            txt_code.ReadOnly = true;
        }

        private void toolStripContainer1_ContentPanel_Load(object sender, EventArgs e)
        {

        }


        private void CreateButton_Click(object sender, EventArgs e)
        {
            // Creating and setting the properties of Button
            Button Mybutton = new Button();
            Mybutton.Location = new Point(225, 198);
            Mybutton.Text = "Submit";
            Mybutton.AutoSize = true;
            Mybutton.BackColor = Color.LightBlue;
            Mybutton.Padding = new Padding(6);
            Mybutton.Font = new Font("French Script MT", 18);

            // Adding this button to form
            this.Controls.Add(Mybutton);

            // Creating and setting the properties of Button
            Button Mybutton1 = new Button();
            Mybutton1.Location = new Point(360, 198);
            Mybutton1.Text = "Cancel";
            Mybutton1.AutoSize = true;
            Mybutton1.BackColor = Color.LightPink;
            Mybutton1.Padding = new Padding(6);
            Mybutton1.Font = new Font("French Script MT", 18);

            // Adding this button to form
            this.Controls.Add(Mybutton1);
        }

        private void CreateLabel_Click(object sender, EventArgs e)
        {
            teste_2 tst2 = new teste_2();
            tst2.Show();
        }
    }
}
