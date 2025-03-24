# 👁️ GitHub Profile View Counter (FastAPI)

This is a minimal FastAPI-based service that counts how many times your GitHub profile has been visited (or at least viewed via the badge).  
Each time your GitHub README loads the badge image, a view is counted.

---

## 🚀 Live Badge

Replace `zkben` with your own GitHub username:

```md
![View Counter](https://your-railway-url.up.railway.app/badge?page_id=zkben)
```

Example badge:

![View Counter](https://githubprofilecounter-production.up.railway.app/badge?page_id=zkben)

---

## 🛠️ Tech Stack

- **FastAPI** – Lightweight API framework  
- **Uvicorn** – ASGI server  
- **JSON File Storage** – Simple file-based view tracking  
- *(PostgreSQL or Redis planned for future scalability)*

---

## 📦 Local Development

### 1. Clone the repository

```bash
git clone https://github.com/z-kahraman/github_profile_counter.git
cd profile-counter
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
uvicorn main:app --reload
```

Then open your browser:

```
http://127.0.0.1:8000/badge?page_id=zkben
```

---

## 📈 Future Improvements

- PostgreSQL or Redis backend
- Per-day unique view tracking
- Geo/agent analytics
- Dashboard UI
- Rate limiting and abuse protection

---

## 🧑‍💻 Author

Developed by [@z-kahraman](https://github.com/z-kahraman)  
Project inspired by curiosity and the desire to learn full-stack deployment.

