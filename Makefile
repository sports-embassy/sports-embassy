all: common/static/common/style.css

common/static/common/style.css: sports_embassy/sass/style.scss sports_embassy/sass/*.scss bower_components bin/node-sass
	bin/node-sass  $< > $@

bower_components: bin/bower
	bin/bower install

bin/node-sass:
ifneq "$$(which node-sass)" ""
	ln -s "$$(which node-sass)" $@
else
	npm install node-sass
	ln -s ../node_modules/.bin/node-sass $@
endif

bin/bower:
ifneq "$$(which bower)" ""
	ln -s "$$(which bower)" $@
else
	npm install bower
	ln -s ../node_modules/.bin/bower $@
endif

clean:
	rm -rf node_modules
	rm -rf bower_components
	rm -f bin/node-sass
	rm -f bin/bower
	rm -f common/static/common/style.css
