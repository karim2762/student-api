# 🎓 Student API

<div align="center">

![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Vercel-black?style=for-the-badge)
![API](https://img.shields.io/badge/API-REST-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-orange?style=for-the-badge)

### Fast • Secure • Simple

A lightweight student records API built for educational purposes.  
Search and retrieve student information instantly using roll numbers.

</div>

---

## ✨ Features

- 🚀 Fast API responses
- 🔒 API Key Authentication
- 🎓 Student Record Lookup
- ☁️ Vercel Ready Deployment
- 📦 JSON Based Database
- 📱 Mobile Friendly Integration
- ⚡ Lightweight & Easy to Use

---

## 📂 Project Structure

```bash
student-api/
│
├── api/
│   └── index.py
│
├── students.json
├── requirements.txt
├── vercel.json
├── index.html
└── README.md
```

---

## 🔑 Authentication

All requests require a valid API Key.

```http
x-api-key: YOUR_API_KEY
```

---

## 🌐 API Endpoint

```http
GET /api?roll=ROLL_NUMBER
```

### Example Request

```http
https://your-domain.vercel.app/api?roll=Y24CS3201
```

---

## 📥 Example Response

```json
{
  "success": true,
  "student": {
    "roll": "Y24CS3201",
    "name": "Student Name"
  }
}
```

---

## ⚙️ Deployment

### Deploy on Vercel

1. Fork this repository
2. Connect GitHub to Vercel
3. Import project
4. Add Environment Variables

```env
API_KEY=your_secret_key
```

5. Deploy 🚀

---

## 🛡️ Security Notice

This project contains educational student lookup functionality.

Please ensure:

- API Keys remain private
- Sensitive data is protected
- Public deployments follow applicable privacy regulations
- Unauthorized access is prohibited

---

## 📈 Future Improvements

- Database Integration
- Admin Dashboard
- Rate Limiting
- Analytics
- JWT Authentication
- Search Filters

---

## 👨‍💻 Developer

### KEXER

Creator & Maintainer

- GitHub: https://github.com/karim2762
- Instagram: @kexer.vx
- Telegram: @Kexer_hub

---

## 📜 Copyright

© 2026 KEXER. All Rights Reserved.

This project is provided for educational and learning purposes only. Unauthorized redistribution, resale, or misuse of the source code is prohibited.

---

<div align="center">

### Built with ❤️ by KEXER

"Creating tools that are simple, powerful, and accessible."

</div>
