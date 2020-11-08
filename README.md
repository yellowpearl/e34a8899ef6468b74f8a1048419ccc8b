<h1>
	Dashboard 
</h1>
<p>Test task for Alitics</p>
<h3>
	Install and run
</h3>
<ul>
	<li>git clone https://github.com/yellowpearl/e34a8899ef6468b74f8a1048419ccc8b.git</li>
	<li>sudo apt install redis-server</li>
	<li>sudo apt-get install rabbitmq-server</li>
	<li>pip3 install virtualenv</li>
	<li>python3 -m venv env</li>
	<li>source venv/bin/activate</li>
	<li>cd ./dashboard</li>
	<li>pip3 install -r requirements.txt</li>
	<li>change db settings in settings.py</li>
	<li>python manage.py makemigrations</li>
	<li>python manage.py migrate</li>
	<li>python manage.py createsuperuser</li>
	<li>python manage.py runserver</li>
	<li>(in new terminal) celery -A dashboard worker -l info</li>
	<li>login in 127.0.0.1/admin</li>
	<li>go to 127.0.0.1/main</li>
</ul>
<img href="https://lh3.googleusercontent.com/pw/ACtC-3dd9uWxRhicsXaZhpmqkH3tx9R0Vc0EJpQ6Y_it3gK-jU2vNaElIDPWTdqf3wsRjT8fslAr5zvxyBYuEYIrhzmvysjGb8AUOhtfNqNxGc1WfDVi3cKNOjU9is3KlrEDLRTe9dGXA_7i13JuFWMWoNAm=w1080-h675-no?authuser=0">
