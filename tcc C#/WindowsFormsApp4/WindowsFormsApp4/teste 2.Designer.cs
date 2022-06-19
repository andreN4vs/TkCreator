namespace WindowsFormsApp4
{
    partial class teste_2
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.telinha = new System.Windows.Forms.Panel();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 0;
            this.button1.Text = "button1";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            this.button1.DragOver += new System.Windows.Forms.DragEventHandler(this.button1_DragOver);
            this.button1.DragLeave += new System.EventHandler(this.button1_DragLeave);
            this.button1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.button1_MouseDown);
            // 
            // telinha
            // 
            this.telinha.AllowDrop = true;
            this.telinha.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.telinha.Location = new System.Drawing.Point(583, 12);
            this.telinha.Name = "telinha";
            this.telinha.Size = new System.Drawing.Size(205, 199);
            this.telinha.TabIndex = 1;
            this.telinha.DragDrop += new System.Windows.Forms.DragEventHandler(this.telinha_DragDrop);
            this.telinha.DragEnter += new System.Windows.Forms.DragEventHandler(this.telinha_DragEnter);
            // 
            // teste_2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.telinha);
            this.Controls.Add(this.button1);
            this.Name = "teste_2";
            this.Text = "teste_2";
            this.Load += new System.EventHandler(this.teste_2_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Panel telinha;
    }
}