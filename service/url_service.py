from utils.base62 import encode
from repo.url_repo import URLRepo
from fastapi import HTTPException
from datetime import datetime

repo = URLRepo()

class URLService:

    def create_short_url(self, db, request_body, request):
        url = repo.create(db, request_body.full_url, request_body.expires_at)

        short_code = encode(url.id)
        repo.update_short_code(db, url, short_code)
        base_url = str(request.base_url).rstrip("/")
        return f"{base_url}/{short_code}"
        # return f"http://localhost:8000/{short_code}"

    def resolve_url(self, db, code):
        url = repo.get_by_code(db, code)

        if not url:
            raise HTTPException(status_code=404, detail="URL not found")

        if url.expires_at and url.expires_at < datetime.utcnow():
            raise HTTPException(status_code=410, detail="URL expired")

        url.click_count += 1
        db.commit()

        return url.full_url