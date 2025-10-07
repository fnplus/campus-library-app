# CampusLibrary

> A local shared resource library for students  
> Browse and download notes, ebooks, videos, music, software, and more — all from peers on your LAN.

---

## 💡 What is CampusLibrary

CampusLibrary is a peer-to-peer network application built for closed networks (hostels, dorms, campus residences).  
Students can share study materials, ebooks, media, software, and any other digital resources they legally possess. The system catalogs these resources, enriches them with metadata (e.g. cover art, description), and presents a clean web interface for discovery, search, and download.

Everything stays local — no external hosting required.

---

## ✨ Key Features

- 🔎 **Peer discovery & indexing** via D‑LAN, DC++ or similar  
- 🗂️ **Support for all file types** — notes, ebooks, videos, music, code, software, etc.  
- 🏷️ **Categories & tags** (Books, Notes, Media, Software, Others)  
- 🖼️ **Metadata enrichment** (cover art, descriptions for books/media)  
- ⚡ **Web UI**: responsive interface for browsing, searching, filtering  
- 📥 **Direct download / streaming** from peers (HTTP / SMB / D‑LAN)  
- 🔁 **Optional caching / seeding** by the server for popular resources  
- 🛠️ **Moderation tools**: hide or remove unsuitable content  

---

## 🏗️ Architecture Overview

```
Students’ Devices (peers)
 └── share folders: Books, Notes, Videos, etc.
      │
      │ (Peer discovery + file listings)
      ▼
[CampusLibrary Server]
 ├── crawler / indexer — scans peer listings  
 ├── metadata module — fetches cover art / book info  
 ├── database (SQLite or Postgres) — stores catalog  
 ├── API (FastAPI) — serves metadata & peer info  
 └── Web UI (React) — user interface
      │
      ▼
End users → browser on LAN → browse → download / stream
```

---

## 🛠 Quick Start (for prototype/hack)

### Prerequisites

- A server on the same LAN (Raspberry Pi, PC, mini server)  
- Docker & Docker Compose (or Python + Node.js environment)  
- API keys (optional) for book metadata sources (Open Library, Google Books, etc.)  
- On peer devices: D‑LAN or DC++ installed

### 1️⃣ Server setup (Docker mode)

```bash
git clone https://github.com/yourusername/CampusLibrary.git
cd CampusLibrary
cp .env.example .env
# Insert API keys in `.env` if needed
docker compose up --build
```

- Backend API: `http://<server-ip>:8080`  
- Frontend UI: `http://<server-ip>:5173`  
- If mDNS / Avahi is enabled: `http://campuslibrary.local`

### 2️⃣ Peer setup (student machines)

1. Install D‑LAN / DC++  
2. Add shared folders (e.g. “Books”, “Notes”, “Media”)  
3. (Optional) For easier download, run a simple HTTP server in each shared folder:

```bash
cd ~/Books && python3 -m http.server 9000
cd ~/Media && python3 -m http.server 9001
```

The server will detect these shares and index them automatically.

---

## 🧰 Developer Commands

### Backend API

```bash
cd server
pip install -r requirements.txt
uvicorn api:app --reload --host 0.0.0.0 --port 8080
```

### Crawler / Indexer

```bash
python3 crawl.py
```

### Frontend UI

```bash
cd web
npm install
npm run dev
```

---

## 📈 Roadmap & Future Enhancements

- Cover art / thumbnail support for ebooks and media  
- In-browser preview: PDF viewer, audio player, video stream  
- Duplicate detection across peers  
- Caching hot resources on server  
- Peer reliability / availability metrics  
- Admin dashboard for moderation (hide/remove)  
- Optional authentication / access control  

---

## ⚠️ Usage & Legal Disclaimer

CampusLibrary is intended for **educational, local network use only**.  
Users must ensure all shared content is legal and abide by copyright and institutional policies.  
This project does **not condone** sharing of infringing material.

---

## 🤝 Contributing & License

Contributions, pull requests, and issue suggestions are welcome!  
Licensed under the **MIT License** © 2025 CampusLibrary contributors.

---

**Let’s put all useful resources in reach — powered by students, for students.**
