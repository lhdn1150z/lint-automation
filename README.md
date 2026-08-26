# 🤖 Auto Code Quality Checker (Linter Bot)

ระบบตรวจสอบคุณภาพโค้ดอัตโนมัติ ทุกครั้งที่ push หรือเปิด Pull Request จะรัน **flake8** (style/error checker) และ **black** (formatter) อัตโนมัติ พร้อม comment ผลลัพธ์กลับเข้า PR ให้ทันที

## 🎯 จุดประสงค์

จำลองงานจริงของ DevOps/Platform engineer: automated code review gate ที่ป้องกันโค้ดคุณภาพต่ำเข้า main branch โดยไม่ต้องรอคนมาตรวจด้วยมือ

## ⚙️ Features

- **flake8**: เช็ค syntax error, unused imports, style ผิดกฎ PEP8
- **black**: เช็ค code formatting อัตโนมัติ พร้อมโชว์ diff ที่ควรแก้
- **Auto PR Comment**: บอทคอมเมนต์สรุปผลเข้า PR ทันที ไม่ต้องเปิด log เอง
- **CI Gate**: ถ้าพบปัญหา job จะ fail กันไม่ให้ merge code ที่มีปัญหาแบบไม่รู้ตัว
- มี unit tests คู่ตัวอย่างโค้ดที่ format ถูกต้อง

## 📁 โครงสร้างโปรเจกต์

```
lint-automation/
├── src/
│   ├── sample.py       # โค้ดตัวอย่างที่ "ตั้งใจ" ให้มีปัญหา style (ใช้เดโม)
│   └── clean.py        # โค้ดที่ format ถูกต้องแล้ว
├── tests/
│   └── test_clean.py
├── .github/workflows/
│   └── lint.yml         # workflow หลัก
├── .flake8              # config กฎ flake8
└── requirements.txt
```

## 🚀 วิธีทดสอบ

### รัน local
```bash
pip install -r requirements.txt
flake8 src/
black --check --diff src/
pytest tests/ -v
```

### วิธีเดโมให้เห็นผลจริง
1. เปิด Pull Request ใหม่ (แก้ไฟล์อะไรก็ได้ เช่นแก้ `src/sample.py`)
2. ระบบจะรัน workflow อัตโนมัติ แล้ว **comment กลับเข้า PR** บอกว่าไฟล์ไหนมีปัญหา format/style อะไรบ้าง
3. รัน `black src/` แก้ไฟล์ให้ถูก format แล้ว push ใหม่ → comment รอบใหม่จะขึ้น ✅ ผ่านหมด

## 🛠️ Tech Stack

Python, flake8, black, pytest, GitHub Actions (github-script for PR comments)

## 📈 แนวทางต่อยอด

- เพิ่ม `mypy` เช็ค type hints
- เพิ่ม `bandit` เช็คช่องโหว่ความปลอดภัยในโค้ด
- Block merge อัตโนมัติถ้า lint ไม่ผ่าน (branch protection rules)
