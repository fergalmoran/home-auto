from app import db


class Light(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False)
    def __repr__(self):
        return '<Light %r>' % self.name


class Scene:
    pass
