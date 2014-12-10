all: start

.PHONY: all start
	
start:
	vagrant up
	python huntnet/manage.py runserver

