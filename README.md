---

# 📚 Student Courses Search System

A simple, fast, and practical web-based system to search for students and display their registered courses with a clean dashboard interface.

---

## 🚀 Features

* 🔍 Search by **student name** (Arabic supported with normalization)
* 🔢 Search by **academic number**
* ⚡ Fast search with limited results (Top 20)
* 🧠 Smart Arabic text normalization:

  * (أ / إ / آ → ا)
  * (ة → ه)
  * (ى → ي)
* 📊 Simple **Dashboard** for viewing data
* 🌐 دعم **تغيير اللغة (عربي / English)**
* 📉 إزالة العناصر الثقيلة (charts) لسرعة الأداء
* 📊 Visitor counter (stored securely on server)
* 🔒 Backend logic hidden باستخدام PHP

---

## 🛠️ Technologies Used

* **Frontend:**

  * HTML
  * CSS (Responsive + Dark UI)
  * JavaScript

* **Backend:**

  * PHP

* **Data Processing:**

  * Python

---

## 📁 Project Structure

```
project/
│
├── index.html          # صفحة البحث الرئيسية
├── dashboard.html      # لوحة التحكم (عرض البيانات بشكل منظم)
│
├── search.php          # منطق البحث (Hidden logic)
├── counter.php         # عداد الزوار
│
├── students.json       # قاعدة البيانات النهائية
├── counter.txt         # تخزين عدد الزوار
│
├── py&txt/             # مجلد معالجة البيانات
│   │
│   ├── generate_data.py   # تحويل TXT → JSON
│   ├── CS.txt
│   ├── IT.txt
│   ├── IS.txt
│   ├── gen.txt
│
├── favicon.ico
├── README.md
```

---

## ⚙️ How It Works

### 1. Data Preparation (Python)

* يتم قراءة ملفات المواد من مجلد:

```
py&txt/
```

* استخراج:

  * اسم الطالب
  * الرقم الأكاديمي
  * المواد

* تحويل البيانات إلى:

```
students.json
```

---

### 2. Search Process

#### في الواجهة (index.html):

* المستخدم يكتب:

  * اسم أو رقم أكاديمي

* يتم إرسال request إلى:

```
search.php
```

---

#### داخل السيرفر (PHP):

* إذا كان الإدخال رقم:

  * يتم البحث مباشرة في الأرقام

* إذا كان نص:

  * يتم تطبيع النص العربي
  * ثم البحث داخل الأسماء

---

### 3. Dashboard

* صفحة:

```
dashboard.html
```

تعرض:

* البيانات بشكل منظم
* واجهة نظيفة بدون عناصر ثقيلة
* مناسبة للموبايل

✔ تم حل مشكلة:

* القائمة الجانبية (Sidebar) أصبحت ثابتة (Fixed)

---

### 4. Visitor Counter

* عند أول استخدام:

```
counter.php?action=increment
```

* يتم تحديث:

```
counter.txt
```

---

## ▶️ How to Run

### 1. تشغيل السيرفر (PHP)

```bash
php -S localhost:8000
```

ثم افتح:

```
http://localhost:8000
```

---

### 2. توليد البيانات

```bash
cd py&txt
python generate_data.py
```

---

## 🔒 Security Notes

* ❌ لا يوجد أي logic مهم في الـ frontend
* ✅ كل العمليات تتم داخل PHP
* 🔐 حماية من:

  * سرقة البيانات
  * التلاعب بالعداد
  * تحميل JSON مباشرة

---

## 💡 Future Improvements

* 🗄️ استخدام Database بدل JSON (MySQL)
* 🔎 بحث متقدم (اسم + رقم + مادة)
* ⚡ تحسين الأداء باستخدام indexing
* 📡 إنشاء REST API
* 👤 نظام تسجيل دخول (Admin Dashboard)

---

## 👨‍💻 Author

Developed by **Ali Ashraf**

---

## ⭐ License

This project is open-source and free to use.

---
