# Memory Card Game (Django)

Ushbu loyiha Django framework yordamida yaratilgan "Xotira o'yini" (Memory Card Game).
Foydalanuvchilar ro'yxatdan o'tib, kartalarni juftlash orqali o'z xotiralarini sinab ko'rishlari va natijalarini saqlashlari mumkin.

## Xususiyatlar
- 🔐 **Auth Tizimi**: Ro'yxatdan o'tish va kirish (Login/Register).
- 🃏 **Karta Modeli**: Ma'lumotlar bazasidan olinadigan rasmli kartalar.
- 🧩 **O'yin Jarayoni**: Vaqt va ball hisoblash tizimi.
- 📊 **Dashboard**: Foydalanuvchi statistikasi va yetakchilar ro'yxati (Leaderboard).
- 🎨 **Dizayn**: Zamonaviy "Glassmorphism" uslubidagi UI (Vanilla CSS).

## O'rnatish va Ishga Tushirish

1. **Talablar**: Python o'rnatilgan bo'lishi kerak.
2. **Kutubxonalarni o'rnatish**:
   ```bash
   pip install django pillow
   ```
3. **Migration (Ma'lumotlar bazasini yaratish)**:
   ```bash
   python3 manage.py migrate
   ```
4. **Boshlang'ich ma'lumotlarni yuklash** (Admin va Kartalar):
   ```bash
   python3 init_game_data.py
   ```
5. **Loyihani ishga tushirish**:
   ```bash
   python3 manage.py runserver
   ```

## Foydalanish

- Brauzerda `http://127.0.0.1:8000/` manziliga kiring.
- **Login**: 
  - Username: `admin`
  - Password: `1`
  - Yoki yangi akkaunt oching ("Ro'yxatdan o'tish").
- **Admin Panel**: `http://127.0.0.1:8000/admin/` (Yangi kartalar qo'shish uchun).

## Texnologiyalar
- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite
