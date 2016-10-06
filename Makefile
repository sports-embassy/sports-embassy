all: common/static/common/style.css

common/static/common/style.css: sports_embassy/sass/style.scss sports_embassy/sass/*.scss bower_components bin/node-sass
	bin/node-sass  $< > $@

bower_components: bin/bower
	bin/bower install

bin/node-sass:
	npm install node-sass
	ln -s ../node_modules/.bin/node-sass $@

bin/bower:
	npm install bower
	ln -s ../node_modules/.bin/bower $@
