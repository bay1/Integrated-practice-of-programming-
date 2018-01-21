using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace phonebook
{
    class function
    {
        private static string _bp = AppDomain.CurrentDomain.SetupInformation.ApplicationBase;
        public static string _basePath = AppDomain.CurrentDomain.SetupInformation.ApplicationBase + @"student.xml";

        public static void CreateStudentXml()
        {
            XDocument studentDoc = new XDocument();
            XDeclaration XDeclaration = new XDeclaration("1.0", "utf-8", "yes");
            studentDoc.Declaration = XDeclaration;
            XElement xElement = new XElement("studentcontract");
            studentDoc.Add(xElement);
            studentDoc.Save(_basePath);
        }

        public static bool AddStudentInfo(StudentInfo param)
        {
            XElement xml = XElement.Load(_basePath);
            XElement studentXml = new XElement("student");
            studentXml.Add(new XAttribute("studentid", param.StudentID));
            studentXml.Add(new XElement("name", param.Name));
            studentXml.Add(new XElement("sex", param.Sex));
            studentXml.Add(new XElement("age", param.Age.ToString()));
            studentXml.Add(new XElement("birthdate", param.BirthDate.ToString("yyyy-MM-dd")));
            studentXml.Add(new XElement("phone", param.Phone));
            studentXml.Add(new XElement("homeaddress", param.HomeAddress));
            studentXml.Add(new XElement("email", param.Email));
            studentXml.Add(new XElement("profession", param.Profession));
            xml.Add(studentXml); 
            xml.Save(_basePath);
            return true;
        }
        public static bool UpdateStudentInfo(StudentInfo param)
        {
            bool result = false;
            if (param.StudentID > 0)
            {
                XElement xml = XElement.Load(_basePath);
                XElement studentXml = (from db in xml.Descendants("student")
                                       where db.Attribute("studentid").Value == param.StudentID.ToString()
                                       select db).Single();
                studentXml.SetElementValue("name", param.Name);
                studentXml.SetElementValue("sex", param.Sex);
                studentXml.SetElementValue("age", param.Age.ToString());
                studentXml.SetElementValue("birthdate", param.BirthDate.ToString("yyyy-MM-dd"));
                studentXml.SetElementValue("phone", param.Phone);
                studentXml.SetElementValue("homeaddress", param.HomeAddress);
                studentXml.SetElementValue("email", param.Email);
                studentXml.SetElementValue("profession", param.Profession);
                xml.Save(_basePath);
                result = true;
            }
            return result;
        }
        public static bool DeleteStudentInfo(int studentid)
        {
            bool result = false;
            if(studentid>0)
            {
                XElement xml = XElement.Load(_basePath);
                XElement studentXml=(from db in xml.Descendants("student")
                    where db.Attribute("studentid").Value==studentid.ToString()select db).Single();
                studentXml.Remove();
                xml.Save(_basePath);
                result = true;
            }
            return result;
        }
        public static List<StudentInfo>GetAllStudentInfo()
        {
            List<StudentInfo> studentList = new List<StudentInfo>();
            XElement xml = XElement.Load(_basePath);
            var studentVar = xml.Descendants("student");
            studentList = (from student in studentVar
                           select new StudentInfo
                           {
                               StudentID = Int32.Parse(student.Attribute("studentid").Value),
                               Name = student.Element("name").Value,
                               Age = Int32.Parse(student.Element("age").Value),
                               Sex = student.Element("sex").Value,
                               BirthDate = DateTime.Parse(student.Element("birthdate").Value),
                               Phone = student.Element("phone").Value,
                               HomeAddress = student.Element("homeaddress").Value,
                               Email = student.Element("email").Value,
                               Profession = student.Element("profession").Value
                           }).ToList();
            return studentList;     
        }
        public static StudentInfo GetStudentInfo(int studentid)
        {
            StudentInfo studentinfo = new StudentInfo();
            XElement xml = XElement.Load(_basePath);
            studentinfo = (from student in xml.Descendants("student")
                           where student.Attribute("studentid").Value == studentid.ToString()
                           select new StudentInfo
                           {
                               StudentID = Int32.Parse(student.Attribute("studentid").Value),
                               Name = student.Element("name").Value,
                               Age = Int32.Parse(student.Element("age").Value),
                               Sex = student.Element("sex").Value,
                               BirthDate = DateTime.Parse(student.Element("birthdate").Value),
                               Phone = student.Element("phone").Value,
                               HomeAddress = student.Element("homeaddress").Value,
                               Email = student.Element("email").Value,
                               Profession = student.Element("profession").Value
                           }).Single();
            return studentinfo;
        }
        public static List<StudentInfo>GetStudentInfoList(StudentInfo param)
        {
            List<StudentInfo> studentList = new List<StudentInfo>();
            XElement xml = XElement.Load(_basePath);
            var studentVar = xml.Descendants("student");
            if(param.StudentID!=0)
            {
                studentVar = xml.Descendants("student").Where(a => a.Attribute("studentid").Value == param.StudentID.ToString());
            }
            else if(!String.IsNullOrEmpty(param.Name))
            {
                studentVar = xml.Descendants("student").Where(a => a.Element("name").Value == param.Name);
            }
            studentList = (from student in studentVar
                           select new StudentInfo
                           {
                               StudentID = Int32.Parse(student.Attribute("studentid").Value),
                               Name = student.Element("name").Value,
                               Age = Int32.Parse(student.Element("age").Value),
                               Sex = student.Element("sex").Value,
                               BirthDate = DateTime.Parse(student.Element("birthdate").Value),
                               Phone = student.Element("phone").Value,
                               HomeAddress = student.Element("homeaddress").Value,
                               Email = student.Element("email").Value,
                               Profession = student.Element("profession").Value
                           }).ToList();
            return studentList; 
        }

        public static List<StudentInfo> GetStudentInfo2(string stuprofession)  //根据专业查找学生
        {
            List<StudentInfo> allstudentinfo = GetAllStudentInfo();  //查找的不是一个学生 新建临时列表
            List<StudentInfo> somestudent = new List<StudentInfo>();
            foreach(StudentInfo student in allstudentinfo)
            {
                if (student.Profession == stuprofession)
                    somestudent.Add(student);
            }
            return somestudent;
        }

        public static bool ExistId(int studentid)
        {

            List<StudentInfo> studentList = GetAllStudentInfo();
            foreach (StudentInfo student in studentList)
                if (student.StudentID == studentid)
                    return true;
            return false;
        }
    }
}
