install:
	# install the package
	pip install --upgrade pip && \
		pip install -r requirements.txt && \
		python -m textblob.download_corpora
format:
	# format the code
	black *.py src/*.py
lint:
	# run the linter
	pylint --disable=R,C *.py src/*.py
test:
	# run the tests
	python -m pytest -vv --cov=src --cov=main test_*.py
build:
	# build the package		
	docker build -t deploy-fastapi .
run:
	# run the package
	# docker run -p 127.0.0.1:8080:8080 a3780aa02164
deploy:
	# deploy the package
	aws ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin 224400985101.dkr.ecr.ap-southeast-2.amazonaws.com
	docker build -t wiki .
	docker tag wiki:latest 224400985101.dkr.ecr.ap-southeast-2.amazonaws.com/wiki:latest
	docker push 224400985101.dkr.ecr.ap-southeast-2.amazonaws.com/wiki:latest
all: install format lint test build deploy