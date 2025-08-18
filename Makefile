install:
	# install the package
	pip install --upgrade pip && \
	pip install -r requirements.txt
format:
	# format the code
lint:
	# run the linter
test:
	# run the tests
build:
	# build the package
deploy:
	# deploy the package