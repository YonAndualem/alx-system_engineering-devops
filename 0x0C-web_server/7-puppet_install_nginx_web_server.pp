# Installs and Configures an nginx web server
package { 'nginx' :
  ensure     => installed,
}

file { 'Configure index.html':
  path       => '/var/www/html/index.html',
  ensure     => present,
  content    => 'Hello World!',
}

file { 'Configure 404.html':
  path       => '/var/www/html/404.html',
  ensure     => present,
  content    => 'Ceci n\'est pas une page',
}

file_line { 'redirect':
  path       => '/etc/nginx/sites-available/default',
  ensure     => present,
  after      => 'server_name _;',
  line       => 'rewrite ^/redirect_me/?.*$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file_line { '404 error page':
  path       => '/etc/nginx/sites-available/default',
  ensure     => present,
  after      => 'server_name _;',
  line       => 'error_page 404 /404.html;',
}

service { 'nginx' :
  ensure     => running,
  require    => Package['nginx'],
}
