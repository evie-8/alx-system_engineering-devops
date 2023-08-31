# adding nginx
exec { 'nginx installing':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin/:/usr/local/bin/:usr/sbin:/usr/bin:/sbin:/bin',
}

# ensuring to update packages
exec { 'update packages':
  command => 'apt-get -y update'
  path    => '/usr/local/sbin/:/usr/local/bin/:usr/sbin:/usr/bin:/sbin:/bin',
}

# checking if nginx is installed
package { 'nginx':
  ensure => 'installed',
}

# accepting http requests
exec { 'http requests':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin/:/usr/local/bin/:usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

# changing to var/www directory
exec { 'changing permissions':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin/:/usr/local/bin/:usr/sbin:/usr/bin:/sbin:/bin',
}

# creating landing page
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# creating 404 page
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

# redirection
file { 'redirection':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
        listen 80 default_server;
	listen [::]:80 default_server;
	       root /var/www/html/;
        index index.html index.htm index.nginx-debian.html;
	server_name_;
	location / {
		try_files \$uri \$uri/ =404;
	}
	error_page 404 /404.html;
	location /404.html {
		internal;
	}
	if  (\$request_filename ~ redirect_me){
		rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
	}
}
",
}

# start nginx
service { 'nginx':
  ensure  => 'running';
  require => Package['nginx'],
}

# restart nginx
exec { 'restart nginx':
  command => 'service nginx restart',
  path    => '/usr/local/sbin/:/usr/local/bin/:usr/sbin:/usr/bin:/sbin:/bin',
}
