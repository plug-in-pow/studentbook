from flask import Flask, g, render_template, request
from .forms import RegisterFormSt , RegisterFormte , RegisterFormco , LoginForm
import os
import os.path
from . import db
from . import auth
def create_app(test_config=None):
	#create factory for app object with test config	
	app = Flask(__name__,instance_relative_config=True)


	app.config.from_mapping(
		SECRET_KEY='a92cede7a46f3d768a4895932bb47633',
		DATABASE=os.path.join(app.instance_path,'studentbook.sqlite'),
	)

	if test_config is None:
		#load the instance config
		app.config.from_pyfile('config.py',silent=True)
	else:
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instace_path)
	except:
		pass			
	
	#print(os.path.abspath(g.__file__))
	@app.route("/")
	def home():
	    return render_template("home.html")

	@app.route("/")
	def index():
	    return render_template("home.html")



	#about page
	@app.route("/about")
	def about():
		return render_template("about.html")

	#contact us page
	@app.route("/contact")
	def contact():
		return render_template("contact.html")

	#for student
	@app.route("/register_s",methods=['GET','POST'])
	def register_s():
		form = RegisterFormSt()
		return render_template("register_student.html",title="Register-Student",form=form)
		#return render_template('login.html',title='register-student',form=form)	

	#for teacher
	@app.route("/register_t",methods=['GET','POST'])
	def register_t():
		form = RegisterFormte()
		return render_template("register_teacher.html",title="Register-Teacher",form=form)

	#for committee
	@app.route("/register_c",methods=['GET','POST'])
	def register_c():
		form = RegisterFormco()
		return render_template("register_committee.html",title="Register-Committee",form=form)

	#login for all
	@app.route("/login",methods=['GET','POST'])
	def login():
		form = LoginForm()
		return render_template("login.html",title="Login",form=form)

	db.init_app(app)
	
	app.register_blueprint(auth.bp)	
	
	return app	