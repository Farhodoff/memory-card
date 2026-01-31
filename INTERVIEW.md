# 🎙 Interview: Memory Card Game Project

**Intervyu oluvchi (Q):** Salom! O‘zingiz yaratgan "Memory Card Game" loyihasi haqida qisqacha gapirib bera olasizmi? Bu qanday loyiha?

**Dasturchi (A):** Salom! Albatta. Bu Django frameworki asosida yaratilgan veb-ilova bo‘lib, foydalanuvchilarning xotirasini charxlashga mo‘ljallangan o‘yin. Foydalanuvchi yopilgan kartalar orasidan bir xil juftliklarni topishi kerak. Asosiy maqsad – eng qisqa vaqt ichida barcha juftliklarni topib, maksimal ball to‘plash.

---

**Q:** Loyihada qaysi texnologiyalardan foydalandingiz va nima uchun?

**A:** 
1. **Backend uchun Django (Python):** Django xavfsizlik (ayniqsa Auth tizimi), tezkor ishlab chiqish va ma'lumotlar bazasi bilan ishlashda juda qulayligi uchun tanlandi.
2. **Frontend uchun HTML, CSS va JavaScript:** Dizayn uchun hech qanday CSS framework (Bootstrap yoki Tailwind) ishlatmadim, aksincha **Vanilla CSS** yordamida zamonaviy **Glassmorphism** (oyna effekti) uslubini yaratdim. O‘yin logikasi (kartalarni aylantirish, vaqtni hisoblash) esa to‘liq JavaScriptda yozildi.
3. **Ma'lumotlar Bazasi (SQLite):** Hozircha kichik loyiha bo‘lgani uchun yengil va sozlash oson bo‘lgan SQLite ishlatildi.

---

**Q:** O‘yin logikasi qanday ishlaydi? Backend va Frontend o‘rtasidagi bog‘liqlik qanday?

**A:** Bu qiziq qismi. 
- **Backend (API):** Django'da maxsus API yozdim. Bu API bazadan kartalar (Card modeli) rasmlarini oladi, ularni tasodifiy (random) tartibda aralashtiradi va Frontendga JSON formatida yuboradi.
- **Frontend (JS):** Foydalanuvchi "O‘yinni boshlash" tugmasini bosganda, JS orqali API ga soro‘v yuboriladi. Kartalar kelgach, ular ekranga chiziladi. O‘yin davomida kartalarni solishtirish (match qilish) va vaqtni hisoblash brauzerda (mijoz tomonida) bajariladi.
- **Natijani saqlash:** O‘yin tugagach, yakuniy ball va vaqt yana API orqali Backendga yuboriladi va `UserScore` modeliga saqlanadi.

---

**Q:** Dizayn borasida qanday yechimlar qildingiz? "Glassmorphism" dedingiz, bu nimani anglatadi?

**A:** Men oddiy dizayndan qochib, foydalanuvchiga "premium" his berishni xohladim. Glassmorphism – bu interfeys elementlariga xira oyna (muzlagan shisha) effektini berish. 
- Orqa fonga gradientli ranglar qo'ydim.
- Panellar (`.glass-panel`) yarim shaffof (translucent) va xira (blur effekti bilan) qilindi.
- Ranglar palitrasi sifatida to‘q ko‘k (`bg-dark`) va yorqin aksent ranglar (binafsha va pushti) tanlandi. Bu o‘yinga zamonaviy "Cyberpunk" yoki "Futuristic" kayfiyat bag‘ishlaydi.

---

**Q:** Loyiha davomida qanday qiyinchiliklarga duch keldingiz va ularni qanday hal qildingiz?

**A:** 
1. **Statik fayllar muammosi:** Boshida rasmlar va CSS yuklanmay qoldi. `settings.py` da `STATIC_ROOT`, `MEDIA_ROOT` va URL konfiguratsiyalarini to‘g‘ri sozlash orqali buni hal qildim.
2. **O‘yin logikasi:** Kartalar tez bosilganda xatoliklar bo‘lmasligi uchun JavaScriptda "lock" (qulflab turish) mexanizmini qo‘shdim. Ya'ni, ikkita karta ochilganda, ular tekshirilib bo‘lmaguncha uchinchi kartani ochib bo‘lmaydi.
3. **Login Redirect:** Foydalanuvchi kirganda to‘g‘ri sahifaga o‘tishi uchun `LOGIN_REDIRECT_URL` sozlamasini qo‘shdim.

---

**Q:** Kelajakda bu loyihani rivojlantirish uchun nimalar qo‘shgan bo‘lar edingiz?

**A:** 
- **Multiplayer rejimi:** Ikki foydalanuvchi real vaqtda bir-biri bilan bellashishi (WebSockets orqali).
- **Darajalar (Levels):** Oson (4x4), O‘rta (6x6) va Qiyin (8x8) maydonlar.
- **Mavzular:** Foydalanuvchi o‘zi xohlagan mavzuni (masalan, Hayvonlar, Bayroqlar, Texnologiya) tanlay olish imkoniyati.
- **Global Reyting:** Faqat o‘zimni emas, balki butun tizim bo‘yicha eng kuchli o‘yinchilarni ko‘rish imkoniyati (Hozir bu qisman bor).

**Q:** Ajoyib! Javoblaringiz uchun rahmat.

**A:** Sizga ham rahmat!
