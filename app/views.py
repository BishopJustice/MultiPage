from flask import render_template, request, redirect, url_for, session
from app import db, app
from models import User, Project, Item, Link
from forms import SignupForm, SigninForm
import datetime
import webbrowser


@app.route('/')
def index():
    if 'email' not in session:
        try:
            signup_form = SignupForm()
            signin_form = SigninForm()
            return render_template('home.html', signup_form=signup_form, signin_form=signin_form)
        except:
            return("Email is not in session")

    user = db.session.query(User).filter_by(email = session['email']).first()
    if user is None:
        try:
            signup_form = SignupForm()
            signin_form = SigninForm()
            return render_template('home.html', signup_form=signup_form, signin_form=signin_form)
        except:
            return("User is None")

    projects = db.session.query(Project).filter_by(uid=user.uid).all()
    items = db.session.query(Item).filter_by(uid=user.uid, state="Open").all()
    return render_template('index.html', projects=projects, user=user, items=items, message="")
   

@app.route('/project/<int:pid>', methods=['GET'])
def project(pid):
    if 'email' not in session:
        return redirect(url_for('index'))
 
    user = db.session.query(User).filter_by(email = session['email']).first()
    if user is None:
        return redirect(url_for('index'))

    projects = db.session.query(Project).filter_by(uid=user.uid).all()
    links = db.session.query(Link).filter_by(pid=pid).all()
    project = db.session.query(Project).filter_by(pid=pid, uid=user.uid).one()
    open_items = db.session.query(Item).filter_by(pid=pid, state="Open").all()
    resolved_items = db.session.query(Item).filter_by(pid=pid, state="Resolved").all()
    return render_template("project.html", project=project, projects=projects, 
                            links=links, open_items=open_items, resolved_items=resolved_items, user=user)
@app.route('/account')
def account():
    if 'email' not in session:
        return redirect(url_for('signin'))
    user = db.session.query(User).filter_by(email = session['email']).first()
    if user is None:
        return redirect(url_for('signin'))
    projects = db.session.query(Project).filter_by(uid=user.uid).all()
    open_items = db.session.query(Item).filter_by(state="Open", uid=user.uid).all()
    resolved_items = db.session.query(Item).filter_by(state="Resolved", uid=user.uid).all()
    return render_template('account.html', user=user, projects=projects,
                           open_items=open_items, resolved_items=resolved_items)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate() == False:
          return render_template('signup.html', form=form)
        else:
          joined = unicode(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
          newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data, joined)
          db.session.add(newuser)
          db.session.commit()
          
          session['email'] = newuser.email

          return redirect(url_for('index'))
   
    elif request.method == 'GET':
        return render_template('signup.html', form=form)



@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
   
    if request.method == 'POST':
      if form.validate() == False:
        return render_template('signin.html', form=form)
      else:
        session['email'] = form.email.data
        return redirect(url_for('index'))
                 
    elif request.method == 'GET':
      return render_template('signin.html', form=form)

@app.route('/signout')
def signout():
    if 'email' not in session:
        return redirect(url_for('signin'))
    session.pop('email', None)
    return redirect(url_for('index'))

@app.route('/add_project', methods=['POST'])
def add_project():
    name = request.form['project_name']
    if len(name) >= 50:
        return redirect(request.referrer)
    else:
        user = db.session.query(User).filter_by(email = session['email']).first()
        project = Project(name=name, uid=user.uid)
        db.session.add(project)
        db.session.commit()
        return redirect(request.referrer)

@app.route('/delete_project/<int:pid>', methods=['POST'])
def delete_project(pid):
    project = db.session.query(Project).filter_by(pid=pid).first()
    db.session.delete(project)
    db.session.commit()
    project = db.session.query(Project).filter_by(pid=pid).first()
    if project:
        print project
        return redirect(request.referrer)
    else:
        print "What?"
        return redirect(url_for('index'))

@app.route('/add_item', methods=['POST'])
def add_item():
    user = db.session.query(User).filter_by(email = session['email']).first().uid
    project = request.form['projectid']
    description = request.form['item_description']
    opened_at = unicode(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    item = Item(uid=user, pid=project, description=description, state="Open", opened_at=opened_at)
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
    item.resolved_at = datetime.datetime.now()
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


@app.route('/open_links/<int:pid>', methods=['POST'])
def open_links(pid):
    links = db.session.query(Link).filter_by(pid=pid).all()
    for each in links:
        webbrowser.open(each.url)
    return redirect(request.referrer)

@app.route('/delete_link/<int:id>', methods=['POST'])
def delete_link(id):
    link = db.session.query(Link).filter_by(id=id).one()
    db.session.delete(link)
    db.session.commit()
    return redirect(request.referrer)






