from models.url_model import URLMapping

class URLRepo:

    def create(self, db, full_url, expires_at):
        url = URLMapping(full_url= str(full_url), expires_at=expires_at)
        db.add(url)
        db.commit()
        db.refresh(url)
        return url

    def update_short_code(self, db, url, short_code):
        url.short_code = short_code
        db.commit()
        return url

    def get_by_code(self, db, code):
        return db.query(URLMapping).filter(URLMapping.short_code == code).first()