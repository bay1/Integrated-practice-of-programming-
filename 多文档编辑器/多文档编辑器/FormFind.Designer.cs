namespace 多文档编辑器
{
    partial class FormFind
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
            this.labelFind = new System.Windows.Forms.Label();
            this.labelReplace = new System.Windows.Forms.Label();
            this.textBoxFind = new System.Windows.Forms.TextBox();
            this.textBoxReplace = new System.Windows.Forms.TextBox();
            this.buttonFindNext = new System.Windows.Forms.Button();
            this.buttonReplace = new System.Windows.Forms.Button();
            this.buttonAllReplace = new System.Windows.Forms.Button();
            this.buttonCancle = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // labelFind
            // 
            this.labelFind.AutoSize = true;
            this.labelFind.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.labelFind.Location = new System.Drawing.Point(12, 27);
            this.labelFind.Name = "labelFind";
            this.labelFind.Size = new System.Drawing.Size(119, 20);
            this.labelFind.TabIndex = 0;
            this.labelFind.Text = "查找内容(N)";
            // 
            // labelReplace
            // 
            this.labelReplace.AutoSize = true;
            this.labelReplace.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.labelReplace.Location = new System.Drawing.Point(12, 74);
            this.labelReplace.Name = "labelReplace";
            this.labelReplace.Size = new System.Drawing.Size(99, 20);
            this.labelReplace.TabIndex = 1;
            this.labelReplace.Text = "替换为(P)";
            // 
            // textBoxFind
            // 
            this.textBoxFind.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.textBoxFind.Location = new System.Drawing.Point(137, 24);
            this.textBoxFind.Name = "textBoxFind";
            this.textBoxFind.Size = new System.Drawing.Size(250, 30);
            this.textBoxFind.TabIndex = 2;
            // 
            // textBoxReplace
            // 
            this.textBoxReplace.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.textBoxReplace.Location = new System.Drawing.Point(137, 74);
            this.textBoxReplace.Name = "textBoxReplace";
            this.textBoxReplace.Size = new System.Drawing.Size(250, 30);
            this.textBoxReplace.TabIndex = 3;
            // 
            // buttonFindNext
            // 
            this.buttonFindNext.Font = new System.Drawing.Font("楷体", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.buttonFindNext.Location = new System.Drawing.Point(411, 17);
            this.buttonFindNext.Name = "buttonFindNext";
            this.buttonFindNext.Size = new System.Drawing.Size(100, 30);
            this.buttonFindNext.TabIndex = 4;
            this.buttonFindNext.Text = "查找下一个";
            this.buttonFindNext.UseVisualStyleBackColor = true;
            this.buttonFindNext.Click += new System.EventHandler(this.buttonFindNext_Click);
            // 
            // buttonReplace
            // 
            this.buttonReplace.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.buttonReplace.Location = new System.Drawing.Point(411, 53);
            this.buttonReplace.Name = "buttonReplace";
            this.buttonReplace.Size = new System.Drawing.Size(100, 30);
            this.buttonReplace.TabIndex = 5;
            this.buttonReplace.Text = "替换";
            this.buttonReplace.UseVisualStyleBackColor = true;
            this.buttonReplace.Click += new System.EventHandler(this.buttonReplace_Click);
            // 
            // buttonAllReplace
            // 
            this.buttonAllReplace.Font = new System.Drawing.Font("楷体", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.buttonAllReplace.Location = new System.Drawing.Point(411, 89);
            this.buttonAllReplace.Name = "buttonAllReplace";
            this.buttonAllReplace.Size = new System.Drawing.Size(100, 30);
            this.buttonAllReplace.TabIndex = 6;
            this.buttonAllReplace.Text = "全部替换";
            this.buttonAllReplace.UseVisualStyleBackColor = true;
            this.buttonAllReplace.Click += new System.EventHandler(this.buttonAllReplace_Click);
            // 
            // buttonCancle
            // 
            this.buttonCancle.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.buttonCancle.Location = new System.Drawing.Point(411, 125);
            this.buttonCancle.Name = "buttonCancle";
            this.buttonCancle.Size = new System.Drawing.Size(100, 30);
            this.buttonCancle.TabIndex = 7;
            this.buttonCancle.Text = "取消";
            this.buttonCancle.UseVisualStyleBackColor = true;
            this.buttonCancle.Click += new System.EventHandler(this.buttonCancle_Click);
            // 
            // FormFind
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(532, 163);
            this.Controls.Add(this.buttonCancle);
            this.Controls.Add(this.buttonAllReplace);
            this.Controls.Add(this.buttonReplace);
            this.Controls.Add(this.buttonFindNext);
            this.Controls.Add(this.textBoxReplace);
            this.Controls.Add(this.textBoxFind);
            this.Controls.Add(this.labelReplace);
            this.Controls.Add(this.labelFind);
            this.Name = "FormFind";
            this.ShowIcon = false;
            this.Text = "查找";
            this.Load += new System.EventHandler(this.FormFind_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label labelFind;
        private System.Windows.Forms.Label labelReplace;
        private System.Windows.Forms.TextBox textBoxFind;
        private System.Windows.Forms.TextBox textBoxReplace;
        private System.Windows.Forms.Button buttonFindNext;
        private System.Windows.Forms.Button buttonReplace;
        private System.Windows.Forms.Button buttonAllReplace;
        private System.Windows.Forms.Button buttonCancle;
    }
}