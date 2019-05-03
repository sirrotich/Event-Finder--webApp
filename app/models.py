
class Services(db.Model):
    __tablename__= 'services'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    topic = db.Column(db.String(255))
    content = db.Column(db.Text)
    date = db.Column(db.DateTime(250), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    reviews = db.relationship('Reviews', backref='title', lazy='dynamic')

    def save_service(self,post):
        db.session.add(post)
        db.session.commit()

    @classmethod
    def get_posts(id):
    service = Services.query.filter_by(title=title).all()
        return post

    def __repr__(self):
        return f"Services {self.id}','{self.date}')"

class Reviews(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    review = db.Review(db.String(255))
    date_posted = db.Column(db.DateTime(250), default=datetime.utcnow)
    services_id = db.Column(db.Integer, db.ForeignKey("services.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_review(cls,id):
        reviews = Reviews.query.filter_by(services_id=id).all()
        return reviews

    def __repr__(self):
        return f"Reviews('{self.review}', '{self.date_posted}')"


class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    user = db.relationship('User', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)