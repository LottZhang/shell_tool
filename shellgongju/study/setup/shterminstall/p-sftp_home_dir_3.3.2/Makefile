install:
	[ -f client.pyc.bak ] || cp /usr/lib/python2.6/site-packages/shterm/sftp3/client.pyc client.pyc.bak 
	[ -f file_client.php.bak ] || cp /var/www/shterm/client/file_client.php file_client.php.bak
	cp client.pyc /usr/lib/python2.6/site-packages/shterm/sftp3/
	cp file_client.php /var/www/shterm/client/
	cp get_sftp_workdir /usr/libexec/shterm/
	@echo "install done"

uninstall:
	[ -f client.pyc.bak ] && mv client.pyc.bak /usr/lib/python2.6/site-packages/shterm/sftp3/client.pyc
	[ -f file_client.php.bak ] && mv file_client.php.bak /var/www/shterm/client/file_client.php
	rm -rf /usr/libexec/shterm/get_sftp_workdir
	@echo "remove done"
