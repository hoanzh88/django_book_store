# django Single App: book store
+ CRUD
+ Bootstrap

### Tạo Project
```
python -m django startproject myproject
python manage.py migrate
```

Chạy thử:
```python manage.py runserver```

### Creating a superuser
```python manage.py createsuperuser```

Chạy thử: http://localhost:8000/admin/

### Creating users and groups
Vào trang admin tạo 1 user và 1 group

### Setting up your authentication url
\django_book_store\book_store\urls.py
```
from django.urls import path, include
path('accounts/', include('django.contrib.auth.urls')),
```

\django_book_store\book_store\settings.py
```
import os
TEMPLATES = [
      {
       'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

### Login template
\django_book_store\templates\base_generic.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="icon" type="image/png" href="assets/img/favicon.png">	
    <title>{% block title %}CRUD{% endblock title %}</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">	
    <body>
        <div class="container">
            <div class="row">
              <div class="col col-md-03">
				  <ul class="sidebar-nav">
				   {% if user.is_authenticated %}
					 <li>User: {{ user.get_username }}</li>
					 <li><a href="{% url 'logout'%}?next={{request.path}}">Logout</a></li>
				   {% else %}
					 <li><a href="{% url 'login'%}?next={{request.path}}">Login</a></li>
				   {% endif %}
				  </ul>
			  </div>
              <div class="col col-md-09">                  
                  {% block content %}
                  {% endblock content %}  
              </div>      
            </div>
          </div>
		</body>
</html>
```

\django_book_store\templates\registration\login.html
```
{% extends "base_generic.html" %}
{% block title %}Login page{% endblock %}
{% block content %}
  {% if form.errors %}
    <p>Your username and password didn't match. Please try again.</p>
  {% endif %}
  {% if next %}
    {% if user.is_authenticated %}
      <p>Your account doesn't have access to this page. To proceed,
      please login with an account that has access.</p>
    {% else %}
      <p>Please login to see this page.</p>
    {% endif %}
  {% endif %}

  <form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    <table>
      <tr>
        <td>{{ form.username.label_tag }}</td>
        <td>{{ form.username }}</td>
      </tr>
      <tr>
        <td>{{ form.password.label_tag }}</td>
        <td>{{ form.password }}</td>
      </tr>
    </table>
    <input type="submit" value="login" />
    <input type="hidden" name="next" value="{{ next }}" />
  </form>

  {# Assumes you setup the password_reset view in your URLconf #}
  <p><a href="{% url 'password_reset' %}">Lost password?</a></p>
{% endblock %}
```

Chạy login thử ```http://localhost:8000/accounts/login/```



