# Removes erroneous wordpress file extensions, phpp instead of php

exec { 'fix wordpress site running on apache':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
