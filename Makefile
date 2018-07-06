
.PHONY: all clean crete-venv install install-user

all:
	./setup.py build

clean:
	rm -rf build/

install:
	pip3 install -r requirements.txt .

install-user:
	pip3 install -r requirements.txt --user .

create-venv: venv

venv:
	virtualenv-3 venv
