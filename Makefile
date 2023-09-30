install:
		pip install --upgrade pip &&\
		pip install -r requirements.txt
		python -m textblob.download_corpora
format:
		#format code
		black *.py mylib/*.py
lint:
	#flake8 or #pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	#build container
	docker build -t deploy-fastapi .
run:
	#run docker
	#docker run -p 127.0.0.1:8080:8080 e2eab69ff828
deploy:
	#deploy
	aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/i2j5t6x8
	docker build -t fastapi-wiki .
	docker tag fastapi-wiki:latest public.ecr.aws/i2j5t6x8/fastapi-wiki:latest
	docker push public.ecr.aws/i2j5t6x8/fastapi-wiki:latestgit

all: install format lint test build deploy