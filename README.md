

هذا المستودع يوفر **مثبت تلقائي لبيئة Ubuntu الوهمية (proot) داخل Termux** مع حزم أساسية مثبتة مسبقًا.  
المستودع يحتوي على:  
- `hatanbasic.py` → يقوم بتثبيت وإعداد الحزم الأساسية داخل Ubuntu.  
- `install-ubuntu-hatan.sh` → يقوم بتنزيل أو تحديث بيئة Ubuntu (Neo-Oli’s proot) وتشغيل HATAN BASIC.

---

## 📥 طريقة التثبيت

انسخ المستودع إلى جهازك داخل Termux:

```bash
git clone https://github.com/hatanhack/hatanbasic.git
cd hatanbasic


---

🚀 طريقة التشغيل

1. اجعل السكربت قابل للتنفيذ:



chmod +x install-ubuntu-hatan.sh

2. شغّل السكربت:



./install-ubuntu-hatan.sh

سيقوم السكربت بـ:

تنزيل أو تحديث بيئة Ubuntu الوهمية.

الدخول إلى بيئة Ubuntu.

تشغيل سكربت hatanbasic.py لتثبيت جميع الحزم المطلوبة.



---

📦 الحزم المثبتة

يقوم سكربت hatanbasic.py بتثبيت الحزم التالية:

التطوير: git, python, python2, php, ruby, perl, nano, bash

الشبكات: curl, wget, openssl, openssh, nmap, dnsutils, net-tools, w3m

أدوات النظام: clang, coreutils, openjdk-17, proot, termux-api



---

🔄 التحديثات

يتم جلب تحديثات بيئة Ubuntu من Neo-Oli/termux-ubuntu.

كل مرة تقوم بتشغيل install-ubuntu-hatan.sh، يقوم بالتحقق من أحدث نسخة وتحديثها تلقائيًا.



---

⚠️ المتطلبات

Termux (أحدث إصدار)

لا يحتاج روت (يتم استخدام بيئة proot)

اتصال إنترنت مستقر



---

👨‍💻 المؤلف

تم الإنشاء بواسطة HATAN
تلغرام: @n_co1

---
