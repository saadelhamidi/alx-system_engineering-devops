# Install and configure Nginx web server
exec { 'apt-update':
    command => '/usr/bin/apt-get update'
}

Exec['apt-update'] -> Package <| |>

package { 'nginx':
  ensure => installed,
}

# change folder rights
exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  path    => '/var/www/html/index.html',
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  content => 'server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    location /redirect_me {
        rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    }
    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}',
}

file { '/var/www/html/404.html':
  ensure  => present,
  path    => '/var/www/html/404.html',
  content => "Ceci n'est pas une page",
}

exec { 'ufw':
  command  => "ufw allow 'Nginx HTTP'",
  provider => 'shell',
}
exec { 'restart nginx service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
