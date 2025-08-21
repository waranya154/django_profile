

# 🌸 VASINEE Django Profile Webapp

โปรไฟล์เว็บแอปพลิเคชันส่วนตัว สร้างด้วย Django + Bootstrap 5

## 🚀 Features

- 👩‍🎓 หน้าโปรไฟล์ส่วนตัว (About)
- 🧮 ตารางสูตรคูณ (Multiplication Table)
- 🔁 ฟอร์มวนซ้ำ (For Loop)
- 🖼️ แกลเลอรี่ภาพชีวิตการเรียน (Index)
- 📬 ช่องทางติดต่อ (Contact)
- 🎨 UI สวยงาม รองรับภาษาไทย

## ⚡ Quick Start

```bash
git clone <repo-url>
cd My_profile
python -m venv env
env\Scripts\activate  # (Windows)
pip install -r requirements.txt
python manage.py runserver
# เปิด http://127.0.0.1:8000/
```

## 🗂️ Main Structure

- `webpage/views.py` : ฟังก์ชัน view สำหรับแต่ละหน้า
- `webpage/urls.py` : เส้นทาง URL
- `templates/` : HTML (base, index, about, contact, for, table)
- `static/` : CSS, JS, assets

## 📝 Production
- เพิ่มโดเมนใน `ALLOWED_HOSTS` (`settings.py`)
- ตั้ง `DEBUG = False`

---
© 2025 VASINEE | For learning & portfolio use only