all:
	make common_layer

common_layer:
	mkdir python
	cp -a ./common python
	pip install aws_lambda_powertools --target "python" >/dev/null
	pip install mysql-connector-python --target "python" >/dev/null
	pip install pydantic --target "python" >/dev/null
	pip install py-linq --target "python" >/dev/null
	zip -r common.zip python >/dev/null
	rm -r python
