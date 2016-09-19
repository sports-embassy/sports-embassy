all: style.css

style.css: sports_embassy/sass/style.scss sports_embassy/sass/*.scss bower_components
	./node_modules/.bin/node-sass  $< > common/static/common/style.css