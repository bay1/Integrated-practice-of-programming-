namespace phonebook
{
    partial class Form_Search
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form_Search));
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.label1 = new System.Windows.Forms.Label();
            this.cb_searchitem = new System.Windows.Forms.ComboBox();
            this.txt_searchtext = new System.Windows.Forms.TextBox();
            this.btn_search = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridView1
            // 
            this.dataGridView1.BackgroundColor = System.Drawing.SystemColors.ButtonFace;
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.dataGridView1.Location = new System.Drawing.Point(0, 73);
            this.dataGridView1.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.RowTemplate.Height = 23;
            this.dataGridView1.Size = new System.Drawing.Size(829, 378);
            this.dataGridView1.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(120, 24);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(49, 19);
            this.label1.TabIndex = 1;
            this.label1.Text = "输入";
            // 
            // cb_searchitem
            // 
            this.cb_searchitem.FormattingEnabled = true;
            this.cb_searchitem.Items.AddRange(new object[] {
            "学号",
            "姓名"});
            this.cb_searchitem.Location = new System.Drawing.Point(226, 23);
            this.cb_searchitem.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.cb_searchitem.Name = "cb_searchitem";
            this.cb_searchitem.Size = new System.Drawing.Size(130, 26);
            this.cb_searchitem.TabIndex = 2;
            // 
            // txt_searchtext
            // 
            this.txt_searchtext.Location = new System.Drawing.Point(390, 21);
            this.txt_searchtext.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.txt_searchtext.Name = "txt_searchtext";
            this.txt_searchtext.Size = new System.Drawing.Size(148, 28);
            this.txt_searchtext.TabIndex = 3;
            // 
            // btn_search
            // 
            this.btn_search.Location = new System.Drawing.Point(611, 18);
            this.btn_search.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.btn_search.Name = "btn_search";
            this.btn_search.Size = new System.Drawing.Size(112, 35);
            this.btn_search.TabIndex = 4;
            this.btn_search.Text = "查询";
            this.btn_search.UseVisualStyleBackColor = true;
            this.btn_search.Click += new System.EventHandler(this.btn_search_Click);
            // 
            // Form_Search
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 18F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.ClientSize = new System.Drawing.Size(829, 451);
            this.Controls.Add(this.btn_search);
            this.Controls.Add(this.txt_searchtext);
            this.Controls.Add(this.cb_searchitem);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.dataGridView1);
            this.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.MaximizeBox = false;
            this.Name = "Form_Search";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
            this.Text = "查找";
            this.Load += new System.EventHandler(this.Form_Search_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox cb_searchitem;
        private System.Windows.Forms.TextBox txt_searchtext;
        private System.Windows.Forms.Button btn_search;

    }
}