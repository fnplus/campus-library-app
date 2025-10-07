## CampusLibrary Web UI

Next.js (App Router) frontend that renders the CampusLibrary catalogue.

### Prerequisites

- Node.js 20+
- Backend API running locally (`uvicorn app.main:app --reload --port 8080`)

Copy the example environment file and adjust the API URL if required:

```bash
cp .env.local.example .env.local
```

### Development

```bash
npm install
npm run dev
```

Visit [http://localhost:3000](http://localhost:3000) to load the catalogue. The page fetches resources from `NEXT_PUBLIC_API_BASE_URL` and uses query parameters for search (`?q=`) and category filtering (`?category=`).

### Production build

```bash
npm run build
npm start
```

### Project layout

- `src/app/page.tsx` – main catalogue page with search and filters.
- `src/lib/api.ts` – API helper that talks to the FastAPI backend.
- `src/components/` – UI components (resource list, cards, etc.).

### Next steps

- Add pagination and peer availability indicators once the crawler feeds richer metadata.
- Layer in authentication / moderation banners when backend support is ready.
