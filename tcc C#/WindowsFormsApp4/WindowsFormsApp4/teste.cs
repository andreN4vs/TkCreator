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
    public partial class teste : Form
    {
        public teste()
        {
            InitializeComponent();
            string patern = ("from tkinter import *" + "\r\n" + "from tkinter import font" + "\r\n\r\n" + "windowDesign = Tk()" + "\r\n\r\n" + "windowDesign.title('Design Window')" + "\r\n" + "windowDesign.geometry('960x687+426+321')" + "\r\n\r\n\r\n" + "windowDesign.mainloop()");
            StreamReader read = null;
        }

        //metodo salvar e criar pasta
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

        private void txtToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }
    }
}
