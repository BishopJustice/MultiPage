from flask import render_template, request, redirect, url_for, session
from app import db, app
from models import User, Project, Item, Link
from forms import SignupForm, SigninForm
import datetime
import webbrowser


@app.route('/')
def index():
    if 'email' not in session:
        return render_template('index.html')
 
    user = db.session.query(User).filter_by(email = session['email']).first()
    if user is None:
        return render_template('index.html')
    projects = db.session.query(Project).filter_by(uid=user.uid).all()
    items = db.session.query(Item).filter_by(uid=user.uid).all()
    return render_template('index.html', projects=projects, user=user, items=items)

@app.route('/project/<int:pid>', methods=['GET'])
def project(pid):
    if 'email' not in session:
        return render_template('index.html')
 
    user = db.session.query(User).filter_by(email = session['email']).first()
    if user is None:
        return render_template('index.html')

    projects = db.session.query(Project).filter_by(uid=user.uid).all()
    links = db.session.query(Link).filter_by(pid=pid).all()
    project = db.session.query(Project).filter_by(pid=pid, uid=user.uid).one()
    items = db.session.query(Item).filter_by(pid=pid).all()
    return render_template("project.html", project=project, projects=projects, 
                            links=links, items=items, user=user)

@app.route('/add_project', methods=['POST'])
def add_project():
    user = db.session.query(User).filter_by(email = session['email']).first()
    project = Project(name=request.form['project_name'], uid=user.uid)
    db.session.add(project)
    db.session.commit()
    return redirect(request.referrer)

@app.route('/delete_project', methods=['POST'])
def delete_project():
    user = db.session.query(User).filter_by(email = session['email']).first()
    project = db.session.query(Project).filter_by(pid=request.form['project']).one()
    db.session.delete(project)
    db.session.commit()
    return redirect(request.referrer)

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



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate() == False:
          return render_template('signup.html', form=form)
        else:   
          newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
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
