all:
	make common_layer

common_layer:
	mkdir python
	cp -a ./lambda_functions/common python
	pip install aws_lambda_powertools --target "python"
	zip -r common.zip python
	rm -r python
