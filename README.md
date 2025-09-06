# HATANBASIC

> أداة تثبيت الحزم الأساسية على Termux

---

## الوصف

`hatanbasic.py` هو سكربت بايثون يساعدك على تثبيت مجموعة من الحزم الأساسية في بيئة Termux على أجهزة أندرويد بسهولة وسرعة.

---

## الحزم التي يتم تثبيتها

- python
- python2
- python-dev
- python3
- php
- java
- git
- perl
- bash
- nano
- curl
- openssl
- openssh
- wget
- clang
- nmap
- w3m
- hydra
- ruby
- macchanger
- host
- dnsutils
- coreutils

---

## المتطلبات

- تطبيق Termux مثبت على جهازك الأندرويد
- اتصال إنترنت نشط

---

## كيفية الاستخدام

1. افتح تطبيق Termux.
2. حدّث الحزم وقم بترقيتها:
    ```bash
    pkg update && pkg upgrade -y
    ```
3. ثبت git:
    ```bash
    apt install git
    ```
4. استنسخ المستودع:
    ```bash
    git clone https://github.com/hatanhack/hatanbasic.git
    cd hatanbasic
    ```
5. شغّل السكربت:
    ```bash
    python3 hatanbasic.py
    ```

---

### شكرًا لاستخدامك HATANBASIC!