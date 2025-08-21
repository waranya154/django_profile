

<div align="center">
	<h1>🌸 VASINEE Django Profile Webapp 🌸</h1>
	<p>
		<img src="https://img.shields.io/badge/Django-5.x-success?logo=django" alt="django"/>
		<img src="https://img.shields.io/badge/Bootstrap-5.x-blueviolet?logo=bootstrap" alt="bootstrap"/>
		<img src="https://img.shields.io/badge/License-Educational-lightgrey" alt="license"/>
	</p>
	<p>เว็บโปรไฟล์ส่วนตัว สร้างด้วย <b>Django</b> และ <b>Bootstrap 5</b> พร้อม UI สีชมพูสวยงาม รองรับภาษาไทย 🇹🇭</p>
</div>

---

## ✨ คุณสมบัติเด่น

• หน้าโปรไฟล์ส่วนตัว (About) <br>
• ตารางสูตรคูณ (Multiplication Table) <br>
• ฟอร์มวนซ้ำ (For Loop Demo) <br>
• แกลเลอรี่ภาพบรรยากาศชีวิตการเรียน (Index) <br>
• ช่องทางติดต่อ (Contact) พร้อมลิงก์ Facebook, IG, Line, Email, โทรศัพท์ <br>
• ใช้ Bootstrap 5, Bootstrap Icons, CSS ธีมชมพู <br>
• Responsive รองรับมือถือ <br>

---

## 🗂️ โครงสร้างโปรเจกต์

```text
My_profile/
├── manage.py
├── requirements.txt
├── My_profile/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── webpage/
│   ├── views.py
│   ├── urls.py
│   └── ...
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── for.html
│   └── table.html
├── static/
│   ├── css/
│   ├── js/
│   └── assets/
└── ...
```

---

## 🚀 วิธีติดตั้งและใช้งาน

1. **Clone repo และติดตั้ง dependencies**
	 ```bash
	 git clone <repo-url>
	 cd My_profile
	 python -m venv env
	 env\Scripts\activate  # (Windows)
	 pip install -r requirements.txt
	 ```

2. **รันเซิร์ฟเวอร์**
	 ```bash
	 python manage.py runserver
	 ```
	 เปิดเว็บที่ [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📝 อธิบายโค้ดและการทำงาน

| ไฟล์/โฟลเดอร์ | คำอธิบาย |
|---|---|
| `webpage/views.py` | ฟังก์ชัน view สำหรับแต่ละหน้า (index, about, contact, for_view, table_view) |
| `webpage/urls.py` | กำหนด path สำหรับแต่ละหน้า |
| `templates/base.html` | โครงสร้างหลักของเว็บ ใช้ Bootstrap และธีมสีชมพู |
| `templates/index.html` | หน้าแรก มี Hero Section, Carousel, และ Gallery |
| `templates/about.html` | ข้อมูลส่วนตัว, ความเชื่อ, เป้าหมาย, ตารางเป้าหมาย |
| `templates/contact.html` | ช่องทางติดต่อ พร้อมไอคอนและปุ่มลิงก์ |
| `templates/for.html` | ฟอร์มรับตัวเลข แสดงผลลัพธ์การวนซ้ำ |
| `templates/table.html` | ฟอร์มรับตัวเลข แสดงตารางสูตรคูณ |
| `static/` | เก็บไฟล์ CSS, JS, รูปภาพ, และ assets อื่นๆ |

---

## ⚙️ การตั้งค่า Production

- แก้ไข `ALLOWED_HOSTS` ใน `settings.py` ให้ตรงกับโดเมนที่ใช้งานจริง
- ตั้งค่า `DEBUG = False` สำหรับ production

---

## 📄 License

This project is for educational purposes only.