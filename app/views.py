from flask import render_template, request, redirect, url_for, session
from app import db, app
from util import security
from models import User, Project, Item, Link
from forms import SignupForm, SigninForm, ContactForm, EmailForm, PasswordForm
import datetime

@app.route('/')
def index():
    if 'email' not in session:
        signup_form = SignupForm()
        signin_form = SigninForm()
        return render_template('home.html', signup_form=signup_form, signin_form=signin_form)


    user = db.session.query(User).filter_by(email = session['email']).first()
    if user is None:
        signup_form = SignupForm()
        signin_form = SigninForm()
        return render_template('home.html', signup_form=signup_form, signin_form=signin_form)

    projects = db.session.query(Project).filter_by(uid=user.uid).all()
    items = db.session.query(Item).filter_by(uid=user.uid, state="Open").order_by(Item.opened_at).all()
    return render_template('index.html', projects=projects, user=user, items=items, message="")

@app.route('/test')
def test():
    security.send_email("This is an email", "Luke", "test@test.com", "This is a test")
    return "message sent"

@app.route('/project/<int:pid>', methods=['GET'])
def project(pid):
    if 'email' not in session:
        return redirect(url_for('index'))
 
    try:
        user = db.session.query(User).filter_by(email = session['email']).first()
    except:
        return redirect(url_for('index'))
    if user is None:
        return redirect(url_for('index'))

    try:
        project = db.session.query(Project).filter_by(pid=pid, uid=user.uid).one()
        projects = db.session.query(Project).filter_by(uid=user.uid).all()
        links = db.session.query(Link).filter_by(pid=pid).all()
        open_items = db.session.query(Item).filter_by(pid=pid, state="Open").all()
        resolved_items = db.session.query(Item).filter_by(pid=pid, state="Resolved").all()

    except:
        return redirect(url_for('index'))
    return render_template("project.html", project=project, projects=projects, 
                            links=links, open_items=open_items, resolved_items=resolved_items, user=user)
@app.route('/account')
def account():
    if 'email' not in session:
        return redirect(url_for('signin'))
    try:
        user = db.session.query(User).filter_by(email = session['email']).first()
    except:
        return redirect(url_for('index'))
    if user is None:
        return redirect(url_for('index'))
    try:
        projects = db.session.query(Project).filter_by(uid=user.uid).all()
        open_items = db.session.query(Item).filter_by(state="Open", uid=user.uid).all()
        resolved_items = db.session.query(Item).filter_by(state="Resolved", uid=user.uid).all()
        return render_template('account.html', user=user, projects=projects,
                               open_items=open_items, resolved_items=resolved_items)
    except:
        return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    
    if request.method == 'POST':
        signup_form = SignupForm()
        signin_form = SigninForm()
        if signup_form.validate() == False:
            return render_template('home.html', signin_form=signin_form, signup_form=signup_form)
        else:
            joined = unicode(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
            newuser = User(signup_form.firstname.data, signup_form.lastname.data, signup_form.email.data, signup_form.password.data, joined)
            db.session.add(newuser)
            db.session.commit()
            subject = "Confirm your email"
            token = security.ts.dumps(newuser.email, salt='email-confirm-key')
            confirm_url = url_for(
                'confirm_email',
                token=token,
                _external=True)

            html = "Your account was successfully created. Please click the link below to confirm\
                    your email address and activate your account:{confirm_url}".format(confirm_url=confirm_url)
            security.send_email(subject, newuser.firstname, newuser.email, html)
            session['email'] = newuser.email
            return redirect(url_for('index'))
   
    elif request.method == 'GET':
        return redirect(url_for('index'))

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = security.ts.loads(token, salt="email-confirm-key", max_age=86400)
    except:
        abort(404)

    user = User.query.filter_by(email=email).first_or_404()
    user.email_confirmed = True

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('signin'))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    signin_form = SigninForm()
    if request.method == 'POST':
        if signin_form.validate() == False:
            return render_template('signin.html', form=signin_form)
        else:
            session['email'] = signin_form.email.data
        return redirect(url_for('index'))
                 
    elif request.method == 'GET':
        return render_template('signin.html', form=signin_form)

@app.route('/reset', methods=["GET", "POST"])
def reset():
    form = EmailForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('reset.html', form=form)
        else:
            user = User.query.filter_by(email=form.email.data).first_or_404()
            if user:
                subject = "Password reset requested"
                token = security.ts.dumps(user.email, salt='recover-key')

                recover_url = url_for(
                    'reset_with_token',
                    token=token,
                    _external=True)

                html = "Click the following link to reset your password: {}".format(recover_url)

                security.send_email(subject, user.firstname, user.email, html)

                return redirect(url_for('index'))
            else:
                render_template('reset.html', form=form, )
    elif request.method == 'GET':
        return render_template('reset.html', form=form)

@app.route('/reset/<token>', methods=["GET", "POST"])
def reset_with_token(token):
    try:
        email = security.ts.loads(token, salt="recover-key", max_age=86400)
    except:
        abort(404)

    form = PasswordForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first_or_404()
        user.pwdhash = form.password.data
        user.set_password(user.pwdhash)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('signin'))

    return render_template('reset_with_token.html', form=form, token=token)

@app.route('/signout')
def signout():
    session.pop('email', None)
    return redirect(url_for('index'))

@app.route('/add_project', methods=['POST'])
def add_project():
    name = request.form['project_name']
    if len(name) >= 50:
        return redirect(url_for('index'))
    else:
        user = db.session.query(User).filter_by(email = session['email']).first()
        project = Project(name=name, uid=user.uid)
        db.session.add(project)
        db.session.commit()
        return redirect(request.referrer)

@app.route('/delete_project/<int:pid>', methods=['POST'])
def delete_project(pid):
    project = db.session.query(Project).filter_by(pid=pid).first()
    items = db.session.query(Item).filter_by(pid=pid).all()
    db.session.delete(project)
    for each in items:
        each.state = "Project Deleted"
    db.session.commit()
    project = db.session.query(Project).filter_by(pid=pid).first()
    if project:
        return redirect(request.referrer)
    else:
        return redirect(url_for('index'))

@app.route('/add_item', methods=['POST'])
def add_item():
    user = db.session.query(User).filter_by(email = session['email']).first().uid
    project = request.form['projectid']
    description = request.form['item_description']
    opened_at = unicode(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    if project:
        item = Item(uid=user, pid=project, description=description, state="Open", opened_at=opened_at)
    else:
        item = Item(uid=user, description=description, state="Open", opened_at=opened_at)
    db.session.add(item)
    db.session.commit()
    return redirect(request.referrer)

@app.route('/resolve_item/<int:item_id>', methods=['POST'])
def resolve_item(item_id):
    item = db.session.query(Item).filter_by(id = item_id).first()
    item.state = "Resolved"
    item.resolved_at = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    db.session.add(item)
    db.session.commit()
    return redirect(request.referrer)

@app.route('/delete_item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = db.session.query(Item).filter_by(id=item_id).first()
    item.state = "Deleted"
    db.session.add(item)
    db.session.commit()
    return redirect(request.referrer)

@app.route('/add_link', methods=['POST'])
def add_link():
    project = request.form['projectid']
    url = request.form['url']
    if url[0:7] != "http://" and url[0:8] != 'https://':
        url = "http://" + url
    link_name = request.form['link_name']
    link = Link(pid=project, url=url, link_name=link_name)
    db.session.add(link)
    db.session.commit()
    return redirect(request.referrer)

@app.route('/delete_link/<int:id>', methods=['POST'])
def delete_link(id):
    link = db.session.query(Link).filter_by(id=id).one()
    db.session.delete(link)
    db.session.commit()
    return redirect(request.referrer)

@app.route('/assign_project', methods=['POST'])
def assign_project():
    item_id = request.form['item_id']
    project_id = request.form['project_id']
    item = db.session.query(Item).filter_by(id=item_id).one()
    item.pid = project_id  
    db.session.add(item)
    db.session.commit()
    return redirect(request.referrer)

@app.route('/contact', methods=['GET','POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('contact.html', form=form)
        else:
            security.send_self_email(form.subject.data, form.name.data, form.email.data, form.message.data)
            return render_template('contact.html', success=True, form=form)

    elif request.method == 'GET':
        return render_template('contact.html', form=form)



