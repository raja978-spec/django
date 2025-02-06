#                DJANGO DESIGN PATTERN
'''
 Django is based on MVT design pattern

   * Django first call the function on url it moves to Model to take data from
     Database and give it to templates.
      
                           URL
                            |
                            |
            Model <--<--<-VIEWS-->-->--> TEMPLATES 
              |             |
              |             |
              |-->---->--->-|
'''
#               START PROJECT WITH VIRTUAL EV
'''
 python -m venv Virtual_environment_name

 django-admin startproject project_name
 (or)
 python -m django startproject FileSharingApp
 
 django-app startapp app_name
 (or)
 >python -m django startapp FileSharing
 
'''
#               DJANGO_FILE STRUCTURE
'''
 * manage.py - A command-line utility that allows 
               you to interact with your Django
               project
 * __init__.py - An empty file that tells Python that 
                the current directory should be
                considered as a Python package 
 * settings.py - Comprises the configurations of the 
              current project like DB connections.
 * urls.py - All the URLs of the project are present 
          here
 * wsgi.py - This is an entry point for your application 
          which is used by the webservers to serve 
          the project you have created.
'''
#               ABOUT REQUIREMENT.txt file
'''
 * It helps to run your code for another person,
 * This txt will display the needed packages to 
   run your project on their machine.
 * To create Requirement file type this command 
   After activating and installing all the packages.
   
   pip freeze > requirements.txt

 * To install the requirement file run this following
  command.

  pip install -r requirements.txt
'''
#                   CSRF_TOKEN
'''
 * CSRF means cross site request forgery protection
 * It protects from 
    
    1. XSS Attack
    2. Sql inject (Hacker trys to delete record)
    3. Provides HTTPSprotection
    
 * Enable security using {%csrf_token%} this tag.
 * Disable crsf security by importing csrf_exempt in your views file.
'''
#                 BENEFITES OF DJANGO
'''
 * Easily switch database.
 * It has built in admin to authorizied work.
 * Easily scalable - A app that has 50 users only, if the app is used by 100
                     of people we can easily scale for that users also.
 * Secured 
'''
#        PASS ARGUMENTS IN URL AND RETURN JSON
#                    FORMAT
'''
  path('name/<int:d><str:i>',views.functionname)

  def arg(request,d,i):
    Dict={
        'Age':d,
        'Name':i
    }
    return JsonResponse(Dict)
''' 
#       JOINING TEMPLATE,STATICS WITH SETTINGS
'''
  If templates,static folders are created outside 
  of the app's folder

 TEMPLATES=[
   'DIRS':[os.path.join(BASE_DIR,'templates')]
 ]

 Under STATIC_URL type
 STATICSFILES = [
   os.path.join(BASE_DIR,'static')
 ]
'''
#      EXTENDS, BLOCK TITLE, CONTET 
'''

 EXTENDS:

 Helps to extend html content on file to another file
 SYNTAX: {% extends 'HTML_filename.html' %}

 BLOCK TITLE:
 
 Helps to bloack unwanted tags while extends, and also helps to
 Change the particular place.

 In Parents's file {%block title%} 'My first page' {%endblock%}
 In Child file {%block title%} 'My second page' {%endblock%}

 BLOCK CONTENT:

 Helps to change content of the code.
 It change only the content block's code, not all the 
 code
 
 In parent's file {% block content%}<h1>This is my first
 page</h1> {% endblock %}
 In child file {% block content %}<h1>This is my second
 page</h1> {% endblock %}
'''

#         ABOUT VIEWS
'''
 * Views is the responsable for http request and
   response.
 * There are two types of views
   1. Function Based Views
   2. Class Based Views 
'''

#        FOR AND IF IN JINJA SYNTAX
'''
 For helps to iterate dict and load it to hmtl page.

 SYNTAX:  {% for i in dict% }
            {{i.name}}
            {{i.age}}
          {% endfor %}

 If is same as the all programming language.

 SYNTAX: {% if dict %}
            {{do_something}}
          {% else %}
            {{do_Something}}
          {% endif %}
'''

#       ADD IMAGE IN HTML FILE WITH DJANGO
'''
 * You have to specify where the static files are placed in settings if
   the static file is created outside the app folder.
 * If not you can simply add image path in img tag.
 * In html specify {% load static %},img tag you have to specify scr as 
   {% static 'filename/imagename.png' %}
'''

#           MODEL AND ORM
'''
 * Modle is an class helps to create table(class name)
   column(class member) in database.

   EX: class Person(models.Model): #table name
           name=models.CharField() # column

 * Object relational mapper helps to access database
   in more pythonic way.
 * We can delete,save,retrive data from database 
   without writing any SQL query.
 * A model is an way of abstracting(hidding) the
   actually database structure using python

              OR QUERY IN DJANGO MODELS

def Output(request):

    #         USING OR 

    #data=Person.objects.filter(name__startswith="raja") | Person.objects.filter(name__startswith="rani")

    #    USING OR WITH Q OBJECT
    
    from django.db.models import Q # helps to do or function in simple way like 
                                # below
    #data=Person.objects.filter(Q(name__startswith="r") | Q(name__startswith="n") )
    # we can alos perform ~(not) function in this Q
    data=Person.objects.filter(~Q(name__startswith="r") | ~Q(name__startswith="n") )
    
    result={
        'data':data,
        'query':data.query
    }
    
    return render(request,'form.html',context=result)

        
        # USING AND QUERY WITH Q

  from django.db.models import Q
  Data=Users.objects.filter(Q(name__startswith='t') & Q(name__startswith='l'))

  Some of the usefull builtin keywords to handle
  db strings, You can type this all instead of
  __startswith
  
  1. exact
  2. iexact
  3. contains
  4. icontains
  5. in
  6. istartswith
  7. endswith
  
  Keyword to handle date

  1. year
  2. month
  3. day
  4. week_day
  5. isnull
  6. search
  7. regex
  8. iregex 

       # UNION OPERATIONS

 * We know that union helps to combine two more
   more table's data.
   
 * Specify the column name inside value_list

 * Union doesn't return duplicate values in row
   if one first table column's value is also in 
   second tables column then union print only
   onces the values.

 Data=Post.objects.all().values_list('Class').union(Users.objects.all().values_list('name'))
 
 OUTPUT: <QuerySet [('Class1',), ('Class2',), ('Class3',), ('Class4',), ('elango',), ('latha',), ('tina',)]>

 * We can also returning data with their id.

 Data=Users.objects.all().values_list('id','name').union(Post.objects.all().values_list('id','Class')) 

 OUTPUT: <QuerySet [(1, 'Class1'), (1, 'elango'), (2, 'Class2'), (2, 'latha'), (3, 'Class3'), (3, 'tina')]>

 * We can manipulate in returning data by various
   functions. Instead of value_list we can also use
   value that will return dict type data. other than
   this there are alot of fucntions are there to 
   handle return type data.

 Data=Users.objects.all().values('id','name').union(Post.objects.all().values_list('id','Class'))

 OUTPUT: <QuerySet [{'id': 1, 'name': 'Class1'}, {'id': 1, 'name': 'elango'}, {'id': 2, 'name': 'Class2'}, {'id': 2, 'name': 'latha'}, {'id': 3, 'name': 'Class3'}, {'id': 3, 'name': 'tina'}, {'id': 4, 'name': 'Class1'}, {'id': 4, 'name': 'Class4'}, 
          {'id': 5, 'name': 'Class2'}]>


      EXCLUDE FUNCTION IN MODLE

  Data=Users.objects.exclude(name='tina')
  
 * This will return all data except tina, We can also
   perform exclude with conditional opeartors like
   !=,<,>,<=,>=, this all will be only for integer type
 
 * Django modle has built in keyword for those
   conditional opeartion.

 EX: Data=Users.objects.find(age__gt=20)

 This will return al the ages that is greater than
 20.

 Some of the build in keywords to handle int type are:

 1.lt
 2.lte
 3.gt
 4.gte

  
    SELECT PARTICULAR ROW'S VALUE BY COLUMN

  data=Users.objects.filter(name='ragu').values('content')
 
  This will execute SELECT "SignupApp_users"."content" FROM 
  "SignupApp_users" WHERE "SignupApp_users"."name" = ragu
  this statement

  You can also use only() function that will run this
  same query.

 VIEWS.py

  def output(request):
    data=Users.objects.filter(name='ragu').only('content')
    context={
    'query':data.query,
    'Data':data
    }
    return render(request,'Output.html',context=context)

 HTML FILE
 
 You have to use for jinja tag to extract the 
 content
 
 <center>
   {% for i in Data%}
     {{i.content}}
   {% endfor %}
   <br>
   {{query}}
 </center>  

       
         EXECETING RAW QUERY IN VIEWS

  raw() is the method helps to specify query we
  want to perform

 VIEWS.py

 data=Users.objects.raw('SELECT * FROM AppName_ModelName')

  HTML FILE

  Without the for loop it will return raw query on
  HTML

  <center>
   {% for i in Data%}
     {{i.name}}<br>
     {{i.content}}<br>
   {% endfor %}
   <br>
   {{query}}
  </center>
   
      EXECUTE RAW QUERY BY DIRECTLY ON DB

  There are 4 methods involve on this execution.
  
  * connection is the method helps to connect db
    from our project
  * connection.cursour it is actually pointing
    to the specified location in db to execute
    query.
  * cursor.fetchone() or fetchall() is another
    type of method helps to take data from sql 
    statement it depends upon the sql statement.
  * fetchone returns tuple and fetchall returns
    list of tuple.

  VIEWS.py

  def output(request):
    cursor=connection.cursor()
    cursor.execute('select content from SignupApp_Users where name="tina" ')
    data=cursor.fetchone()
    context={
    'query':connection.queries,
    'Data':data
    }
    return render(request,'Output.html',context=context)

  HTML FILE

  <center>
   {{Data}}
   {{query}}
  </center>

  OUTPUT: ("this is tina's content",) 
 
           FORMATTED FETCHING OUTPUT

  VIEWS.py

  # this function return's an formated output
  # without this function output will be
  # [{'id': 6, 'name': 'tina', 'content': "this is tina's content"}, 
  # {'id': 7, 'name': 'ragu', 'content': "this is ragu's content"}]
  # with this function output will be 6 tina this
  # is tina's content 7 ragu this is ragu's content

  def dictfetchall(cursor):
    desc=cursor.description
    return[
        dict(zip([col[0] for col in desc],row))
        for row in cursor.fetchall()
    ]
  def output(request):
    cursor=connection.cursor()
    cursor.execute('select * from SignupApp_Users ')
    data=dictfetchall(cursor)
    context={
    'query':connection.queries,
    'Data':data
    }
    return render(request,'Output.html',context=context)

  HTML file

  <center>
   {{Data}}<hr>
   {% for i in Data%}
   {{i.id}}<br
    {{i.name}}<br>
    {{i.content}}<br>
   {% endfor %}
   {{query}}
  </center>

          MODLE INHERITANCE

     ABSTRACT BASE CLASS MODELS INHERITANCE

  * Abstract base class is the main class to create all of
    the models in models.py

  * It is used when an common information is used
    to other tables.

  class Users(models.Model):
    name=models.CharField(max_length=10)
    content=models.CharField(max_length=100)

    class Meta:
      # we define this users class as abstract class
      # by abstract = True, So this tables content
      # will be used to other inherited classes.
        abstract=1
      # All this users fileds can be used n number
      # of classes(tables)
        
  class Post(Users):
    # name and content fileds also added
    # to this class(table)
    post=models.CharField(max_length=100)

 * You can also access Abstract Meta class by 
   inheriting that class.

   class Users(models.Model):
    name=models.CharField(max_length=10)
    content=models.CharField(max_length=100)

    class Meta:
        abstract=1
        ordering=['name']

   class Post(Users):
     post=models.CharField(max_length=100)

    class Meta(Users.Meta):
        ordering=['post']

   
 IMPLEMENT ONE TO ONE RELATIONSHIP BY INHERITANCE

 class Users(models.Model):
    name=models.CharField(max_length=10)
    content=models.CharField(max_length=100)

    class Meta:
        abstract=1
        ordering=['name']

 class Post(Users):
    post=models.CharField(max_length=100)

    class Meta(Users.Meta):
        ordering=['post']

 class Posted_images(Post): #one-one link
  image=models.FileField()

  * behind the scene django implements one to
    one relationship 

  * See you operation on migrations folder.

  * Primary key is automatically created as
    post_ptr

     operations = [
        migrations.CreateModel(
            name='Posted_images',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SignupApp.post')),
                ('image', models.FileField(upload_to='')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=('SignupApp.post',),
        ),
  

                PROXY MODELS

  * Changes the behaviour of the model.
  * Proxy model operate on orginal model.
  
  from django.db import models
  from django.utils import timezone 
  # Create your models here.
  class Users(models.Model):
    name=models.CharField(max_length=10)
    created=models.DateField()

  # this class implements the logic for the model useres
  # django doesn't create this modles it just implement
  # the logic here we define logic for created attribute
  # in useres.
  class Proxy(Users):
    class Meta:
        proxy=True 
        ordering=['created']

    def created_on(self):
        return timezone.now()-self.created

   
       CREATING MULTIPLE DATABSES IN DJANGO

   * When we create multiple database for one app
     then django confused which database to save
     and retrive information, in this case we
     use routers for those databases.   

      Author.objects.using('other').all()

      Here other is the name of the database
      we want to use from list of database.

  SETTINGS.py

  DATABASES = {
    'default': {},
    'users_db':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'users.db.sqlite3',
    }
  }

  
  # Django looks default database as default os
  # this rout helps to tell django you have to
  # use this data base.
  DATABSE_ROUTERS=['routers.db_routers.AuthRouter',]

  Create an folder called routers with db_router py
  file and that will have the AuthRouter class.

  ROUTER.py

  class AuthRouter:
    route_app_labels={'auth','contenttypes','sessions','admin'}

    # the above 4 apps will read users_db using this
    # function
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None
    
    """
    Attempts to write auth and contenttypes models go to 
    users_db.
    """    
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None
    
    """
    Allow relations if a model in the auth or contenttypes apps is
    involved.
    """
    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels):
            return True
        return None
    
    
    """
    Make sure the auth and contenttypes apps only appear 
    in the 'users_db' database. It just allows to
    migrate inside users_db
    """
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'users_db'
        return None

  * After this Run migrate command with db_name here
    we defined users_db so run the below code.

    python manage.py migrate --database=users_db

  * Now all the apps are migrated in new database
    called users_db, And now we can create superuser
    for this db.

    python manage.py createsuperuser --database=users_db


             TRANSCATION IN MODELS

  * Django db has transaction method that helps to
    analysis the changes made in database after POST
    method, If all of the changes made in for an 
    particular row then only transaction allows to 
    save entered db information in db.

  * Lets assume user-a and user-b are the two users 
    in an bank both of their balance is 100  when user-a
    tries to send some money to user-b then transaction
    checks each and every queries to be executed and then
    save both user's balance changes made by queiries in db.
    if user-a enters an unknow bank cutomer let's
    assume user-c he is not present in db so transcation
    will raise error. And no balance changes were
    made.

    EX: 

    from django.db import transaction
    def output(request):
    
    if request.method=="POST":
        user1=request.POST.get('user1')
        user2=request.POST.get('user2')
        amount=request.POST.get('amount')

        with transaction.atomic():
            u1_update_balance=Users.objects.get(name=user1)
            u1_update_balance.balance -= int(amount)
            u1_update_balance.save() # this will be made after u1 and u2_update_balance 
                                     # executed sucessfully

            u2_update_balance=Users.objects.get(name=user2)
            u2_update_balance.balance +=int(amount)  
            u2_update_balance.save()  # this will be made after u1 and u2_update_balance 
                                     # executed sucessfully

             
            return render(request,'Output.html',{'message':'<h1>updated</h1>'})

    return render(request,'Output.html')
 
  * We can use also transaction as decorator in above the name of
    the function as @transaction.atomic

         
      DJANGO MODEL AGGREGATION FUNCTIONS

  Django has built in aggregation methods before
  going to use that we have to import that.

 from .models import Books
 from django.db.models import Sum
 def output(request):
    # In aggregate Sum method we have to put the
    # column name which is going to be sumed
    obj=Books.objects.all().aggregate(Sum('BooksNo'))
    return render(request,'Output.html',{'data':obj})

  * this method basically returns the sum as
    dict data type,keys are automatically created
    by django, 
    {'BooksNo__sum': 15}
    we can modify the keys by the below step

 from .models import Books
 from django.db.models import Sum
 def output(request):
    obj=Books.objects.aggregate(count_of_books_nums=Sum('BooksNo'))
    return render(request,'Output.html',{'data':obj})
 
 OUTPUT:

 {'count_of_books_nums': 15}

 from .models import Books
 from django.db.models import Sum,Max,Min,Avg
 def output(request):
    obj=Books.objects.aggregate(count_of_books_nums=Sum('BooksNo'))
    obj1=Books.objects.aggregate(max_of_books_nums=Max('BooksNo'))
    obj2=Books.objects.aggregate(min_of_books_nums=Min('BooksNo'))
    obj3=Books.objects.aggregate(avearge_of_books_nums=Avg('BooksNo'))
    con={
        'sum':obj,
        'max':obj1,
        'min':obj2,
        'avg':obj3
    }
    return render(request,'Output.html',{'data':con})

 OUTPUT:{
  'sum': {'count_of_books_nums': 15}, 
 'max': {'max_of_books_nums': 5}, 
 'min': {'min_of_books_nums': 1}, 
 'avg': {'avearge_of_books_nums': 3.0}
 }

 You can also give four statement in one aggregate

 def output(request):
    obj=Books.objects.aggregate(count_of_books_nums=Sum('BooksNo'),Max_bookno=Max('BooksNo'),min_books_nums=Min('BooksNo'),average_books_nums=Avg('BooksNo'))
    con={
        'sum':obj,
      }
    return render(request,'Output.html',{'data':con})

'''


#         DJANGO DEBUGGER TOOLBAR
'''
 * Provides panels to show debug informations like
 * System information 
 * Timing - Shows how long a page to load
 * Settings configration
 * Header - Shows what contents are send receive 
            from server 
 * Work on SQL queries
 * Templates,include

 INSTALLING TOOLBAR WITH : pip install django-debug-toolbar

 Add it on INSTALLED APP on settings and url 

 URLS.py
 
 import debug_toolbar
 path('__debug__/',include(debug_toolbar.urls))

 And also we want to add middleware after CSRFtoken
 middleware

 'debug_toolbar.middleware.DebugToolbarMiddleware'

  Set Interla Ips on settings

  INTERNAL_IPS=[
    #...
    '127.0.0.1',
    #...
  ]

  Include wanted debug toolbar panels in Settings.py

  DEBUG_TOOLBAR_PANLES=[
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.header.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatedPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profilling.ProfillingPanel',
  ]
'''

#        IMPORTANT NOTES FOR MODEL
'''
 * For each makemigrations command django create 
   and stores the migration files in migration
   folder.

   EX: 0015_users.py

 * When you use migrate command then django executes
   this whole py file.

 * When you see an anonymous error while makemigration
   and migrate then see the migrations folder to 
   find the error. And also you can modify those
   unwanted code(that will raise error) in 
'''

#          DJANGO STATIC PROVIDER
'''
 Django provides django.contrib.staticfiles to manage
 static files.
 And also django loads delete static files with the help 
 of cache.
'''

#           DRF
'''
 It is an open source framework helps you to create 
 RESTful APIs
'''

#   CREARE RESPONSIVE IMAGE LAYOUT WITH BOOTSTRAP
'''
 HTML file

 * Here we create 2 rows with 3 columns
 * Width of this container is depends upon 
   number of column you have.
 * sm - means small size column
 * 8 - means width 
 * You can also define numbers without sm


  <div class="container">
  <div class="row">
    <div class="col-sm-8"><img scr= ...></div>
    <div class="col-sm-4"><img scr= ...></div>
  </div>
  <div class="row">
    <div class="col-sm"><img scr= ...></div>
    <div class="col-sm"><img scr= ...></div>
    <div class="col-sm"><img scr= ...></div>
  </div>
 </div>
'''

#          DJANGO-ADMIN COMMANDS
'''
 It is an commandline interface helps to do 
 administrative tasks.

 1. django-admin help
 2. ..... version
 3. ..... check - used to inspect entier project
 4. ..... loaddata - loads data into db
 5. ..... shell - starts python interactive 
                  interpreter
'''

#          JINJA TEMPLATING
'''
 It is an very popular templating engine for python
 the latest version of template is jinja 2

 FERTURES OF JINJA TEMPLATE

 * Protectes from XSS attach.
 * Generate HTML template faster.
 * Easier to debug
'''

#              URLS
'''
 * Collection of path to the python functions
   is called urls
 * We can create our own url by importing views
   into url section.

'''

# DIFFERENCE BETWEEN PROJECT AND APPLICATION

'''
 * An application is an entier django project
 * An app is an module that deals with particular
   part of the project.
'''

#             FORMS WITH HTML
'''
 * Specify method and action in form tag
 * Specify action with {% url 'urlname' %} and also
   specify urlname in urls path
 * Get an json response 
 
 GET METHOD - It visibles all your data in urlpath

 POST METHOD - * In django you need to create csrs_
                 token to specify method as post
               * It will hide all data in urlpath

  * You can specify name id for(lables) at input 
    tags.
''' 

#           DJANGO FORMS
'''
 * Create and import django forms and it's fields
   with label, widgets.
 * Create logical functions in views
 * In HTML you can specify form.as_many(p,table,etc)
'''

#       ADDING BOOSTRAP STYLE TO DJANGO FORM
'''
 * attrs is the argument helps to do this
 * form-control is the common class to create 
   resposive form
 class Userform(forms.Form):
    Name=forms.CharField(label="Name",max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    Feebback=forms.CharField( max_length=50,label_suffix="Feedback",widget=forms.Textarea(attrs={'class':'form-control'}))
''' 

#           FORM ALERTS IN DJANGO
'''
  There are two type of alert
    1. Error
    2. Success
  
  * We validate form with the help of this alerts
  * We do this alert with the help of bootstrap. All
    the alerts are differ from different colours.
'''

#          ONDELETE_CASECADE
'''
 * Helps to delete child table row when parent's 
   row is deleted.
 * Rows are deleted automatically  when parent and
   child are inherited with forigen key
 * In django it is used as follows

  class Position(models.Model):
    title=CharField(max_length=50)
 class Employee(models.Model):
    fullname=CharField(max_length=100)
    emp_code=CharField(max_length=3)
    mobile=CharField(max_length=15)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
'''

#        RENAMING MODELLABLES WITH DJANGO FORM
'''
 Type this below label on Meta class
 labels={
            'fullname':'Full Name',
            'emp_code':'Emp Code',
            }
''' 

#      REPLACING  OBJECT NAME WITH ROW DATA
'''
 * Use string function to view saved data into 
   database in models.py

 * Whenever you create a table inside model you have
   to add this

 def __str__(self):
   return self.title
'''

#       IMAGE UPLOADFIELD IN DJANGO
'''
 Add this on models, This will create a folder
 called image and saves your uploaded images on
 that folder automatically

 image=models.ImageField(upload_to='images/')
'''

#          CRUD OPERATIONS
'''
 def create(request):
    if request.method=='GET':
       Form=EmployeeForm()
    else:
        Form=EmployeeForm(request.POST)
        if Form.is_valid():
            Form.save()
            return redirect('/show')
    return render(request,'CloneApp/create.html',{'form':Form})
 def show(request):
    Form=Employee.objects.all()
    return render(request,'CloneApp/show.html',{'form':Form})
 def edit(request,id):
    Form=Employee.objects.get(id=id)
    return render(request,'CloneApp/edit.html',{'form':Form})
 def update(request,id):
        Form=Employee.objects.get(id=id)
        form=EmployeeForm(request.POST,instance=Form)
        if form.is_valid():
            form.save()
            return redirect('/show')
        return render(request,'CloneApp/edit.html',{'form':Form})
 def delete(request,id):
    Form=Employee.objects.get(id=id)
    Form.delete()
    return redirect('/show')
'''

#       404 ERROR HANDLING
'''
 * If a specified path is not in your urlpattern
   then this error will raise.
 * We can handling this error with the help of 
   this error handling

  IN HTML:

  Create an html file called 404error

  <h1>404 error</h1>
    <p>Sorry the url doen't exist</p>
    <a href="{% url 'index' %}"></a>

  IN VIEWS:

  def Error404(request,exception):
    return render(request,'404error.html')

  exception argument takes the error which will
  raised in browser and render the page.

  IN URLS:

   handler400='todoapp.views.Error404'

   handler404 is the inbuilt function to handle error

   If browser tryies to search unspecified url then
   this will takes from the browser and render the
   404htmlerror page

  IN SETTINGS:

   * Before going to run you have to off debug and add 
     host * in
   * (*) will allows you to route all url.

  
   DEBUG = False
   ALLOWED_HOSTS = ['*']
'''

#       USERCREATION CLASS

'''
 * Helps to specify signupform(registration).
 * You have to inherit and import Usercreation
   form
 * It automatically add name,password,confirm_password 
   in HTML page

'''

#             SECURING ADMIN PANEL
'''

 * Honey pot is the module helps to do this
 * You have install with pip
 * After this you have to migrate, Honey pot 
   creates various fields to save attacker's
   information
 * And include that urls on app level or
   Project level url

   IN URLS:

   path('admin',include(admin_honeypot.urls)) dupliacte
   path('secure',admin.site.urls) orginial

 * So when ever attacker entries into admin 
   it doesn't allow him to redirect admin panel
   instead it save's his information

'''

#             LOGIN, LOGOUT IN DJANGO
'''
 2 COMMON RULES

  * Login,Logout,registration html file should
    be create inside registration folder otherwise
    it raise error

  * url path must me mentioned in project urls

 SETTINGS

   LOGIN_REDIRECT_URL='Home'
   LOGOUT_REDIRECT_URL='login'
   LOGIN_URL='login'

 * This will tells to the browser where you should
   go after login and log out

 * Home, login is the name of the ulr path
  
 * When user trying to access website without
  login then LOGIN_URL helps to redirect 
  
  to login page

 * If you use login_required decorator in views then you
   should specify this URL

 IN PROJECT URLS:

 from django.contrib.auth.views import *
  path('admin/', admin.site.urls),
  path('home',include('LibraryManagementApp.urls')),
  path('',LoginView.as_view(),name='login'),
  path('register',views.register,name='register'),
  path('logout',LogoutView.as_view(),name='logout')

 * Loginview is the class based view that provides
   login form for user
 * We use as_view() function to for class based view

 IN APP URL:

 urlpatterns = [
    path('',views.Home,name='Home'),
 ]

 IN HOME HTML

 * Create Login with form jinja tag ,register with
   UsercreationForm HTML page.
 * You should not create an logout HTML file
 * Specify url name on Home HTML file link as {% url 'login' %}
 * This url moves to login path and execute
   django login form

  LOGIN.HTML

   {{form}}


 IN VIEWS
 
 * Loginrequired is the decorator helps to protect
   annonymous user.
  
 * You have to create login function django takes 
   login form from LoginView class and render it
   to the login.html form

 * UsercreationForm is the class to create register form
   
 from django.shortcuts import redirect, render
 from django.contrib.auth.forms import UserCreationForm
 from django.contrib.auth.decorators import login_required
 
 def register(request):
    Form=UserCreationForm
    if request.method=="POST":
        Form=UserCreationForm(request.POST)
        if Form.is_valid():
            Form.save()
            return redirect('Home')
    else:
        return render(request,'registration/register.html',{'form':Form})
 
 def Login(request):
     return render(request,'registration/Login.html')

 @login_required
 def Home(request):
    return render(request,'Home.html')
'''

#      ANOTHER WAY TO CREATE AUTHENTICATION
'''
 * Django provides authication for all apps that we 
   can see on INSTALLED APP.
 * In that it has 'django.contrib.auth'

 IN PROJECT URLS.py

 path('login',include(django.contrib.auth.urls)),
 path('',include('my_app.urls'))

 This has all the urls from login-password_rest

 IN HTML

 login html file should be created inside the registration
 folder

  <center>
 <h2>Login</h2>
 <form method="POST">
    {% csrf_token %}
    {{form.as_p}}
    <button type="submit">Login</button>
 </form>
 </center> 

 HOME.html

 {% 'if user.is_authenticated %}
 {{user}} shows's user name
 {% else %}
 create in to login href="{% url 'login' %}">Log in</a>
 {% endif %}

 * Is authenticated check wherethere the user logined or not
 * login url takes project urlpath

 SETTINGS.py
 
 set login,logout redirect

 SUPERUSER

 You can create superuser and login with that details

 IN APP URLS.py

 from . import views
 urlpatterns = [
    path('',views.home,name='home'),
    ]
 
 IN VIEWS.py

 def home(request):
    return render(request,'home.html')


'''

#  WAY2 TO CREATE OWN ATHENTICATION SYSTEM
'''
VIEWS.py

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as Login
from django.contrib.auth import logout as Logout
from datetime import datetime
from .models import *
from .forms import *

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        pass1=request.POST["password"]
        user=authenticate(username=username,password=pass1)
        
        if user is not None:
            Login(request,user)
            return redirect('home')
        else:
            message='Please enter valid details'
            return render(request,'login.html',{'message':message})

    return render(request,'login.html')

def logout(request):
    Logout(request)
    return redirect('home')
    
def register(request):
    if request.method=="POST":
       
        username=request.POST.get("username")
        fname=request.POST.get("first_name")
        lname=request.POST.get("last_name")
        email=request.POST.get("email")
        pass1=request.POST.get("password")
        pass2=request.POST.get("password_repeat")
        
        if pass1==pass2:
            try:
              myusers=User.objects.create_user(username,email,pass1)
              myusers.last_name=lname
              myusers.first_name=fname
              myusers.save()
            except IntegrityError as e:
                message="
                Your have already registered...
                Please try to login 
              " 
                return render(request,'register.html',{'message':message})
            return redirect('login')
        else:
            message="Please check if you entered details is correct"
            return render(request,'register.html',{'message':message})
    return render(request,'register.html')
    

URLS.py

from django.contrib import admin
from django.urls import path
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('',views.post,name='post'),
    path('404',views.page404,name='404'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('forgot-password',views.forget_pasword,name='forgot-password'),
    path('createblog',views.create_blog,name='createblog')
]

LOGIN.hmtl

<form class="user" method="POST">
    {% if message %}
    <p>{{message}}</p>
    {% endif %} 
     <div class="form-group"><input class="form-control form-control-user" type="text" id="exampleInputEmail" aria-describedby="emailHelp" placeholder="Enter Username..." name="username"></div>
                                        <div class="form-group"><input class="form-control form-control-user" type="password" id="exampleInputPassword" placeholder="Password" name="password"></div>
                                        <div class="form-group">
                                            <div class="custom-control custom-checkbox small">
                                                <div class="form-check"><input class="form-check-input custom-control-input" type="checkbox" id="formCheck-1"><label class="form-check-label custom-control-label" for="formCheck-1">Remember Me</label></div>
                                                       
                                            </div>
                                        </div>
                                        {% csrf_token %}
                                        <button class="btn btn-primary btn-block text-white btn-user" type="submit">Login</button>
                                        <hr><a class="btn btn-primary btn-block text-white btn-google btn-user" role="button"><i class="fab fa-google"></i>&nbsp; Login with Google</a><a class="btn btn-primary btn-block text-white btn-facebook btn-user" role="button"><i class="fab fa-facebook-f"></i>&nbsp; Login with Facebook</a>
                                        <hr>
 </form>


REGITSER.html

   {% if message %}
      <p class="form-control form-control-user">{{message}}</p>
    {% endif %}
    <form class="user" method="POST">
       <div class="form-group row">
          <div class="col-sm-6"><input class="form-control form-control-user" type="text" id="username" placeholder="Username" name="username"></div>
          <div class="col-sm-6 mb-3 mb-sm-0"><input class="form-control form-control-user" type="text" id="exampleFirstName" placeholder="First Name" name="first_name"></div>
          <div class="col-sm-6"><input class="form-control form-control-user" type="text" id="exampleFirstName" placeholder="Last Name" name="last_name"></div>
        </div>
        <div class="form-group"><input class="form-control form-control-user" type="email" id="exampleInputEmail" aria-describedby="emailHelp" placeholder="Email Address" name="email"></div>
        <div class="form-group row">
        <div class="col-sm-6 mb-3 mb-sm-0"><input class="form-control form-control-user" type="password" id="examplePasswordInput" placeholder="Password" name="password"></div>
        <div class="col-sm-6"><input class="form-control form-control-user" type="password" id="exampleRepeatPasswordInput" placeholder="Repeat Password" name="password_repeat"></div>
        </div>
                                {% csrf_token %}
                                <button class="btn btn-primary btn-block text-white btn-user" type="submit">Register Account</button>
                                <hr><a class="btn btn-primary btn-block text-white btn-google btn-user" role="button"><i class="fab fa-google"></i>&nbsp; Register with Google</a><a class="btn btn-primary btn-block text-white btn-facebook btn-user" role="button"><i class="fab fa-facebook-f"></i>&nbsp; Register with Facebook</a>
                                <hr>
</form>
                         
'''
#         CREATING MODELS
'''
 MODELS.PY
 
 from django.db import models
 from django.forms import CharField, IntegerField

 # Create your models here.
 class Student_Details(models.Model):
    Name=CharField(max_length=10,label="Name")
    Roll_no=IntegerField(label="Roll no")
    Department=CharField(max_length=300,label="Department")
    
 ADMIN.PY

 from django.contrib import admin
 from .models import Student_Details
 # Register your models here.
 admin.site.register(Student_Details)
'''

#         CONNECTING MYSQL IN DJANGO
'''
 * We have to install two packages

 1. pip install mysql-connector
 2. pip install mysql

 * Create a table in localhost phpAdmin

 SETTINGS.PY

 * Change sqlite3 to mysql.
 * Add databasename in NAME, User, password, 
   Host, port.
 * password is optional but you have to give
   if you where in sensitive project.

  DATABASE={
    'default':{
        'ENGINE':'django.db.backend.mysql',
        'NAME':'dbname',
        'USER':'root ',
        'PASSWORD':'',
        'HOST':'127.0.0.1',
        'PORT':'3360', # leave blank if can't 
                        connect error
    }
 }

  After this you have to migrate
'''

#                BLOG_APP
'''
 MODELS.py

 from django.db import models
 from django.db.models.fields import *
 from django.db.models.fields.files import ImageField

 class Post(models.Model):
    title=CharField(max_length=100)
    published_date=DateTimeField()
    image=ImageField(upload_to='images/')
    summary=TextField()

    def Summary(self):
        return self.summary
    def Published_date(self):
        return self.published_date.strftime('%b,%e,%y') # formated date
    def __str__(self):
        return self.title

 ADMIN.py

  from django.contrib import admin
  from .models import Post
  admin.site.register(Post)

  Migrate

 SETTINGS.py

  * We have to specify media root and url
  * The uploaded images on stored in media root
  * We have access those posted images with media
    url

  MEDIA_ROOT=os.path.join(BASE_DIR,'media')
  MEDIA_URL='/media/'
 
 URLS.py

  You have to add static url to load uploaded image
 
  from django.conf import settings
  from django.conf.urls.static import static
  urlpatterns = [
    path('',views.Home,name='Home'),
    path('post',views.post,name='Home'),
    path('details',views.postlist,name='details')
 ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 
 POST.html

 {% for i in form %}
 <center>
    <h1>My blog</h1>
    <h3>Latest Post</h3>
    <a href="{url 'postlist' i.id}">{{i.title}}<br></a>
    
    <small>{{i.published_date}}</small><br>
    <div>
        <center>
            <img src="{{ i.image.url }}" alt="can't load" width="200" height="200"><br>
            <p>{{i.summary}}</p>
        </center>
    </div>
 </center>
 {% endfor %}

 DETAILS.HTML

 <center>
 <title>{{saved_post.title}}</title>
 <h1>{{saved_post.title}}</h1><br>
 <p>{{saved_post.published_date}}</p><br>
 <img src="{{ saved_post.image.url }}" alt="" width="300" height="400"><br>
 <p>{{saved_post.summary}}</p>   
 </center>

 VIEWS.py

 from .models import Post
 from django.shortcuts import render,get_object_or_404

 def post(request):
    Form=Post.objects.all()
    return render(request,'post.html',{'form':Form})

 def postlist(request,id):
    Saved_Post=get_object_or_404(Post,pk=id)
    return render(request,'details.html',{'saved_post':Saved_Post}) 
'''

#           ADDING ATTRIBUTES TO FORM
'''
 * Basically it is used with all Fileds, and widgest.
 * It all has the attr field to specify attributes.

  widgets={
            'published_date':TextInput(attrs={
                'value':Time
            })
        }
      
'''

#    ADDING RICH TEXT EDITOR TO DJANGO PROJECT
'''
HMTL file
mvxyk
<base href="/static/base2/assets/">
<textarea name="editor" cols="30" rows="10"></textarea>
<script type="text/javascript">
        CKEDITOR.replace('editor');
</script>
'''

#     LINK BOOTSTRAP ASSETS WITH BASE TAG
'''
   Don't run runserver command before sepecifying
   this tag, place the folders in correct position
     {% load static %}
    <base href="{% static 'base_1/' %}">
'''

#     ADDING ALERST WITH BOOTSTRAP
'''

 SYNTAX TO SEPCIFY ALERT

 <div class="alert alert-success" role="alert">
  form submitted
 </div>

 ALERT WITH DISMISS BUTTON

  <div class="alert alert-success alert-dismissible fade show" role="alert">
    {{message}} <!--Get the passed message form view-->
  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
  <span aria-hidden="true">&times;</span>
  </button>
 </div>

 TYPE OF ALERT WITH DIMISS BUTTON

 You can replace one of this word instead of 
 success 

 * primary
 * secondary
 * danger
 * warning
 * info
 * light
 * dark
'''

#          CUSTOME USER MODEL
'''
 AbstractUser is the class that will add more fields
 to django's default database model.

 self.normalize_email(email) #sets email to lowercase.
                            # and adds that in to database
 
 You can login to admin panel with email and password
 instead of username with the help of this class

 MODELS.py

 class AdminUser(Model):
    email=EmailField(verbose_name="Email",max_length=20)
    USERNAME_FIELD='email'# This will replace username with email field
    REQUIRED_FIELDS=['username']

 SETTINGS.py

  AUTH_USER_MODEL='App.AdminUser'

'''

#           MIDDLEWARE
'''
 * This is an inbuilt mini plugin in django helps to 
   do some specific stuff in every request and response.

 * In they have defualt middlewares that handels 
   various operations

   
    MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   ]

   Here it does authentication and CSRF protection
   stuffs. We can also create and custome middleware
 
 * To create an middle ware just create an py file
   with any name and create an middleware as an class
   with constructor and __call__ method.

 class ExampleMiddleWare():
    
    # it is called only ones 
    def __inti__(self,response):
      self.get_response=get_response
      
    # But this will called in each request made
    # in browser
    def __call__(self,request):

      print("Before reqeust")

      response=self.get_response(request)

      print("After response")

      return response
'''

#     SESSION MANAGEMENT IN DJANGO
'''
 * In this server stores all users information
   who made an request first time on a website.

 * Server actually creates a unique indentifier
   to find correct user, All this are created 
   one time when a user visiting an website 
   first time.

   EX: In an hotel they have number for each table 
       with that unique number they address the customer
       who wants what dish.

 * In real world browser application it will be 
   happend with the help of HTTP requests we know 
   that HTTP is hypertext transfer protocol here 
   we are requesting for some hypertext to server
   with protocols(rules).

 * There are 2 type of protocol here one is stateless
   protocol and the another one is statefull protocol.

 * In Stateless protocol server didn't store unqiue
   id for each users.

 * But in Session management we have to store that type 
   of data to achive that we have number of implementations
   one of the implementation is Cookies.

 HOW COOKIES WORKS ?

 * When we made an request for particular website 
   obviously it is an stateless protocol but when 
   we get an response form that server it will send 
   you cookies with that response. 

 * An cookies is an small bit of information about
   your browser,pc,etc..

 * On first time visiting those website it will created 
   create cookies and send to you on that time and On the 
   second time server takes the stored information 
   from client machine that is user's cookies, According
   to that cookies values server sends response 

 * There are two type of cookies one can stores 
   that generated cookies in browser for temprorary(session cookies)
   when the tab or browser is closed the stored cookies
   also deleted, another one is stored permanantly
   untill we delete(presistent cookies).

 REAL SESSION MANAGEMENT EXAMPLE

 * It stores login information so that we didn't
   type each time username and password.

 * Cookies can also track all user behavior like
   social media.


 EXAMPLES TO SET COOKIES AND SENDS TO USER

 def cookies_count_view(request):
    count=request.COOKIES.get('count',0)# all of this are inbuilt functions
    totalCount=int(count)+1 # cookies are always stored as string
    response=render(request,'cookies.html',{'count':totalCount})
    response.set_cookies('count',totalCount) # this takes totalCount value and 
                                             # sets the cookies for user
    return response

 DISADVANTAGES OF COOKIES 

 * Still cookies are stored in client's machine
   they can access and modify the cookies and
   may be they modified as virues also so that 
   whenever server tries to access those cookies
   it will get affected. So less Secure.

 * Less information and stored as string only.

 DJANGO SESSION ID

 * To overcame less secure django provides Session id.
 
 * It is also create and sends those session id to 
   users with response and also it takes copy of the session id 
   in server side(django database), so whenever user 
   make a request to server it compares the session 
   id if it is matched only then server sends 
   response according to that id.

 * So if an user modify the session id server will not takes
   the unmatched cookies values.
 
 * In django it is already inbuilted in as MIDDLEWARE
  'django.contrib.sessions.middleware.SessionMiddleware',

 * And it has session app in installed_App

 * We can also delete those middleware and app
   if we need not.

  EXAMPLES TO SET COOKIES AND SENDS TO USER

 def cookies_count_view(request):
    count=request.session.get('count',0)# all of this are inbuilt functions
    totalCount=int(count)+1 # cookies are always stored as string
    request.session['count']=totalCount
    print(request.session.get_expiry_date()) # returns sessions expiry date and time
    return render(request,'cookiescount.html',{'count':totalCount})
'''

#             META CLASS
'''
  It is an class that describes how an class 
  was be created and it is played a rule for
  the class.
'''

#           HTTP METHODS
'''
 There are four methods GET,POST,PUT,DELETE
 But the commonly used methods are GET and POST
'''

#        ADDING LIST USING INPUT TAG IN HTML
'''
<form action="">
    <input list="l">
    <datalist id="l">
        <option value="Python">
        <option value="Perl">
            <option value="PHP">
                <option value="Java">
    </datalist>
    </form>
'''

#     CONNECTING MONGODB WITH DJANGO
'''
 Install djongo which is required to connect
 db with django.

 Install Mongodb Compass which is helps to create
 and connect db.

 Inside settings.py we need change swith monogodb
'''

#     SIGNUP WITH GOOGLE, FACEBOOK
#    SEE this folder for google authentication
#  G:\VS_CODE\Django\GoogleAuthentication-in-Django

'''
Install this module

pip install social-auth-app-django

Add this app to settings.py

SETTINGS.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #FACEBOOK
    'social_django',
    'SignUp',

 # Google authentication
   'django.contrib.sites', # must
    'allauth', # must
    'allauth.account', # must
    'allauth.socialaccount', # must
    'allauth.socialaccount.providers.google', # new
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    #FACEBOOK
    'social_django.middleware.SocialAuthExceptionMiddleware',
]


ROOT_URLCONF = 'GoogleSignUpSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                 
                #FACEBOOK
                 'social_django.context_processors.backends',  
                'social_django.context_processors.login_redirect', 
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
     # FACEBOOK
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',

     # GOOGLE
     # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

    'django.contrib.auth.backends.ModelBackend',
)

#GOOGLE
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# GOOGLE
SITE_ID = 2
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# FACEBOOK
SOCIAL_AUTH_FACEBOOK_KEY="987401429210606"
SOCIAL_AUTH_FACEBOOK_SECRET='f4cf6055393ae8098a58a5e9022f8d78'



               URLS.py

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/',include('social_django.urls',namespace='social')),
]



             VIEWS.py

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(LoginRequiredMixin,TemplateView):
    template_name='home.html'


           HOME.html
        
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <center>
        Welcome to home <br>
        My social login us {{user.username}} 
    </center>
</body>
</html>


For facebook login we have to create developer account
by visiting developers.facebook.com/ and register and 
login yourself in that site

Once you create your app on developers then go to
settings on that we have to add app domain, 

EX:localhost 

for local host

Next thing we have to add Site URL by clicking add 
platform-> Website at the end of the page

EX Site URL: http://localhost:8000/

Click save changes and copy paste the App Id
and App secret key in settings.py file

SOCIAL_AUTH_FACEBOOK_KEY="987401429210606"
SOCIAL_AUTH_FACEBOOK_SECRET='f4cf6055393ae8098a58a5e9022f8d78'

'''

#                 SERILIZER
'''

* It is a component used to convert complex data 
  types, such as Django model instances or other  
  Python data structures, into JSON or other 
  content types

* Serelizer converts object of model to json

* Deserialize the json into instance of model object.

* Used to validate incoming data

from rest_framework import serializers

this is the module used to inherit serialized 
model

'''

#    CREATING DJANGO WEBSITE FRONT END WITH REACT
# REFER HERE G:\VS_CODE\Django_React_project\leadmanager
'''

* Create an app with python manage.py command, inside
  that we have to create scr/components, template/frontend
  static/frontend

* React based operations are goes to scr/components
  folder template/frontend are handles the entry 
  point of our app, that is index.js

* And static/frontend has the complied version of
  js files that will generated when npm run build
  command are in run.

'''

#       LOAD TEMPLATES WITH LOADER FUNTION
'''
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('firstpage.html')
    return HttpResponse(template.render())

We have to specify the our app on installed app to load this
template
'''

#     SQL MIGRATE COMMAND
'''
python manage.py sqlmigrate firstmodels 001

will returns the sql command used to do migrate for that 
model (firstmodels)
'''





























