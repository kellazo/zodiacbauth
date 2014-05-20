zodiacbauth
===========

Project Zodiac Authentication amb Buildout

Descarregar
fer
Local:

python bootstrap.py

bin/buildout

bin/pserve development.py

in a server (AMAZON WEB SERVICES):

python bootstrap.py

bin/buildout

bin/pserve production.py

afegir enllaç wsgi

in /etc/apache2/sites-availabe/default

<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	
	WSGIScriptAlias /zodiacbauth /var/www/zodiacAuth.buildout3/parts/mywsgiapp/wsgi

	DocumentRoot /var/www
	<Directory />
		Options FollowSymLinks
		AllowOverride None
	</Directory>
	<Directory /var/www/>
		Options Indexes FollowSymLinks MultiViews ExecCgi
		
		AddHandler cgi-script .cgi
		AddHandler wsgi-script .wsgi

		AllowOverride all
		Order allow,deny
		allow from all
	</Directory>
	
	
them change url's to function

to view in production:

http://guillem.tk/zodiacbauth

login:

user: lacet
pasw: lacet123
