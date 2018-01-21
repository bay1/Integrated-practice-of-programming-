namespace phonebook
{
    partial class Form_Edit
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form_Edit));
            this.btn_close = new System.Windows.Forms.Button();
            this.btn_update = new System.Windows.Forms.Button();
            this.dt_birthdate = new System.Windows.Forms.DateTimePicker();
            this.rd_woman = new System.Windows.Forms.RadioButton();
            this.rd_man = new System.Windows.Forms.RadioButton();
            this.txt_homeaddress = new System.Windows.Forms.TextBox();
            this.txt_profession = new System.Windows.Forms.TextBox();
            this.txt_email = new System.Windows.Forms.TextBox();
            this.txt_phone = new System.Windows.Forms.TextBox();
            this.txt_age = new System.Windows.Forms.TextBox();
            this.txt_name = new System.Windows.Forms.TextBox();
            this.txt_studengid = new System.Windows.Forms.TextBox();
            this.label9 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btn_close
            // 
            this.btn_close.Location = new System.Drawing.Point(209, 516);
            this.btn_close.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.btn_close.Name = "btn_close";
            this.btn_close.Size = new System.Drawing.Size(112, 35);
            this.btn_close.TabIndex = 26;
            this.btn_close.Text = "取消";
            this.btn_close.UseVisualStyleBackColor = true;
            this.btn_close.Click += new System.EventHandler(this.btn_close_Click);
            // 
            // btn_update
            // 
            this.btn_update.Location = new System.Drawing.Point(46, 516);
            this.btn_update.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.btn_update.Name = "btn_update";
            this.btn_update.Size = new System.Drawing.Size(112, 35);
            this.btn_update.TabIndex = 27;
            this.btn_update.Text = "确认";
            this.btn_update.UseVisualStyleBackColor = true;
            this.btn_update.Click += new System.EventHandler(this.btn_update_Click);
            // 
            // dt_birthdate
            // 
            this.dt_birthdate.Location = new System.Drawing.Point(141, 258);
            this.dt_birthdate.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.dt_birthdate.Name = "dt_birthdate";
            this.dt_birthdate.Size = new System.Drawing.Size(180, 28);
            this.dt_birthdate.TabIndex = 25;
            // 
            // rd_woman
            // 
            this.rd_woman.AutoSize = true;
            this.rd_woman.Location = new System.Drawing.Point(271, 150);
            this.rd_woman.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.rd_woman.Name = "rd_woman";
            this.rd_woman.Size = new System.Drawing.Size(50, 23);
            this.rd_woman.TabIndex = 23;
            this.rd_woman.TabStop = true;
            this.rd_woman.Text = "女";
            this.rd_woman.UseVisualStyleBackColor = true;
            // 
            // rd_man
            // 
            this.rd_man.AutoSize = true;
            this.rd_man.Location = new System.Drawing.Point(140, 150);
            this.rd_man.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.rd_man.Name = "rd_man";
            this.rd_man.Size = new System.Drawing.Size(50, 23);
            this.rd_man.TabIndex = 24;
            this.rd_man.TabStop = true;
            this.rd_man.Text = "男";
            this.rd_man.UseVisualStyleBackColor = true;
            // 
            // txt_homeaddress
            // 
            this.txt_homeaddress.Location = new System.Drawing.Point(141, 398);
            this.txt_homeaddress.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.txt_homeaddress.Name = "txt_homeaddress";
            this.txt_homeaddress.Size = new System.Drawing.Size(181, 28);
            this.txt_homeaddress.TabIndex = 19;
            // 
            // txt_profession
            // 
            this.txt_profession.Location = new System.Drawing.Point(141, 448);
            this.txt_profession.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.txt_profession.Name = "txt_profession";
            this.txt_profession.Size = new System.Drawing.Size(181, 28);
            this.txt_profession.TabIndex = 18;
            // 
            // txt_email
            // 
            this.txt_email.Location = new System.Drawing.Point(141, 346);
            this.txt_email.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.txt_email.Name = "txt_email";
            this.txt_email.Size = new System.Drawing.Size(181, 28);
            this.txt_email.TabIndex = 17;
            // 
            // txt_phone
            // 
            this.txt_phone.Location = new System.Drawing.Point(141, 308);
            this.txt_phone.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.txt_phone.Name = "txt_phone";
            this.txt_phone.Size = new System.Drawing.Size(181, 28);
            this.txt_phone.TabIndex = 22;
            // 
            // txt_age
            // 
            this.txt_age.Location = new System.Drawing.Point(140, 207);
            this.txt_age.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.txt_age.Name = "txt_age";
            this.txt_age.Size = new System.Drawing.Size(181, 28);
            this.txt_age.TabIndex = 21;
            // 
            // txt_name
            // 
            this.txt_name.Location = new System.Drawing.Point(140, 86);
            this.txt_name.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.txt_name.Name = "txt_name";
            this.txt_name.Size = new System.Drawing.Size(181, 28);
            this.txt_name.TabIndex = 20;
            // 
            // txt_studengid
            // 
            this.txt_studengid.Location = new System.Drawing.Point(140, 23);
            this.txt_studengid.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.txt_studengid.Name = "txt_studengid";
            this.txt_studengid.Size = new System.Drawing.Size(181, 28);
            this.txt_studengid.TabIndex = 16;
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(42, 355);
            this.label9.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(89, 19);
            this.label9.TabIndex = 9;
            this.label9.Text = "电子邮箱";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(62, 457);
            this.label10.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(49, 19);
            this.label10.TabIndex = 10;
            this.label10.Text = "专业";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(44, 407);
            this.label8.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(89, 19);
            this.label8.TabIndex = 7;
            this.label8.Text = "家庭住址";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(42, 311);
            this.label7.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(89, 19);
            this.label7.TabIndex = 8;
            this.label7.Text = "手机号码";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(42, 258);
            this.label6.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(89, 19);
            this.label6.TabIndex = 11;
            this.label6.Text = "出生日期";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(62, 210);
            this.label5.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(49, 19);
            this.label5.TabIndex = 14;
            this.label5.Text = "年龄";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(62, 150);
            this.label4.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(49, 19);
            this.label4.TabIndex = 15;
            this.label4.Text = "性别";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(62, 86);
            this.label3.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(49, 19);
            this.label3.TabIndex = 12;
            this.label3.Text = "姓名";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(62, 26);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(49, 19);
            this.label2.TabIndex = 13;
            this.label2.Text = "学号";
            // 
            // Form_Edit
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 18F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(356, 575);
            this.Controls.Add(this.btn_close);
            this.Controls.Add(this.btn_update);
            this.Controls.Add(this.dt_birthdate);
            this.Controls.Add(this.rd_woman);
            this.Controls.Add(this.rd_man);
            this.Controls.Add(this.txt_homeaddress);
            this.Controls.Add(this.txt_profession);
            this.Controls.Add(this.txt_email);
            this.Controls.Add(this.txt_phone);
            this.Controls.Add(this.txt_age);
            this.Controls.Add(this.txt_name);
            this.Controls.Add(this.txt_studengid);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Name = "Form_Edit";
            this.Text = "编辑";
            this.Load += new System.EventHandler(this.Form_Edit_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btn_close;
        private System.Windows.Forms.Button btn_update;
        private System.Windows.Forms.DateTimePicker dt_birthdate;
        private System.Windows.Forms.RadioButton rd_woman;
        private System.Windows.Forms.RadioButton rd_man;
        private System.Windows.Forms.TextBox txt_homeaddress;
        private System.Windows.Forms.TextBox txt_profession;
        private System.Windows.Forms.TextBox txt_email;
        private System.Windows.Forms.TextBox txt_phone;
        private System.Windows.Forms.TextBox txt_age;
        private System.Windows.Forms.TextBox txt_name;
        private System.Windows.Forms.TextBox txt_studengid;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;

    }
}