install:
	# install the package
	pip install --upgrade pip && \
		pip install -r requirements.txt
format:
	# format the code
	black *.py src/*.py
lint:
	# run the linter
	pylint --disable=R,C *.py
test:
	# run the tests
build:
	# build the package
deploy:
	# deploy the package