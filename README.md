
# 🚀 Django REST API shablon

Ushbu loyiha Django REST API asosida yaratilgan.

## 📥 Loyihani yuklab olish

```bash
git clone <project-url>
cd <project-folder>
```

## 🐍 Virtual muhit (venv) yaratish

```bash
python -m venv venv
# yoki
py -m venv venv
# yoki
python3 -m venv venv
```

## ⚙️ Virtual muhitni faollashtirish

### Windows:

```bash
venv\Scripts\activate
```

### Linux / macOS:

```bash
source venv/bin/activate
```

## 📦 Kerakli paketlarni o‘rnatish

```bash
pip install -r requirements.txt
```

## 📁 Loyihaning asosiy papkasiga kirish

```bash
cd src/
```

## 🔐 `.env` fayl yaratish

```bash
cp .env.example .env
```

> `.env` fayl ichiga kerakli sozlamalarni kiriting

## 🗄️ Ma’lumotlar bazasini yaratish

```bash
python manage.py migrate
```

## 👤 Superuser yaratish

```bash
python manage.py createsuperuser
```

## ▶️ Serverni ishga tushirish

```bash
python manage.py runserver
```
