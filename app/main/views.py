@main.route('/')
def index():
    '''
    my index page
    return
    '''
  
    # blogs = Blogs.query.order_by(Blogs.date.desc()).all()from .forms import ReviewForm
    services = Services.query.order_by(Services.date.desc()).all()
    
    title = 'Sir Titus blog'
    return render_template('index.html',title=title, service=service)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.author))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(author = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/cars')
def cars_list():
    # Function that renders all cars and its content

    cars = Cars.query.all()


    return render_template('cars.html', cars=cars)


