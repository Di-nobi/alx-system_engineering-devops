# changing phpp to php
exec { 'fix-wordpress':
  path     =>  '/usr/local/bin/:/bin/',
  command  =>  'sed -i s/phpp/php/g /var/www/html/wp-settings.php'
