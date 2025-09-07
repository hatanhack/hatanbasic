# HATAN BASIC

🔧 أداة مميزة لتثبيت الأدوات الأساسية في Termux دفعة واحدة.  
تمت برمجتها بواسطة **hatanhack** لتسهيل إعداد بيئة عمل جاهزة للمبتدئين والمحترفين.  

---

## 📘 مقدمة عن Termux
Termux هو تطبيق يوفر بيئة لينكس متكاملة على أندرويد.  
قبل البدء باستخدام أي أداة أو سكربت، يجب معرفة **الأساسيات** مثل تحديث النظام وتثبيت الأدوات المهمة.  

---

## 🛠️ أساسيات Termux

### 1️⃣ تحديث النظام
أول خطوة بعد تثبيت Termux لازم تحدث الحزم:
```bash
apt update && apt upgrade -y


---

2️⃣ تثبيت الأدوات الأساسية

تثبيت git لإدارة المستودعات:


pkg install git -y

تثبيت python (يدعم السكربتات):


pkg install python -y

تثبيت python2 (مفيد لبعض السكربتات القديمة):


pkg install python2 -y

تثبيت nano (محرر نصوص بسيط):


pkg install nano -y


---

3️⃣ تحميل أي أداة من GitHub

مثال (تحميل أداة hatanbasic):

git clone https://github.com/hatanhack/hatanbasic.git
cd hatanbasic


---

4️⃣ إعطاء صلاحية تشغيل

قبل تشغيل أي سكربت، لازم تعطيه صلاحية التنفيذ:

chmod +x hatanbasic.py


---

5️⃣ تشغيل السكربت

بعدها تشغله باستخدام Python:

python hatanbasic.py

أو إذا كان Python3:

python3 hatanbasic.py


---

📦 ما الذي يثبته سكربت hatanbasic؟

السكربت يقوم تلقائيًا بتثبيت الحزم الأساسية التالية:

python

python2

python-dev

python3

php

java

git

perl

bash

nano

curl

openssl

openssh

wget

clang

nmap

w3m

hydra

ruby

macchanger

host

dnsutils

coreutils



---

👨‍💻 المطور

hatanhack

GitHub: hatanhack



---

⚠️ ملاحظة

هذه الأداة مخصصة لتسهيل تثبيت الأدوات الأساسية على Termux فقط.
لا تتحمل مسؤولية أي استخدام غير قانوني.

---
