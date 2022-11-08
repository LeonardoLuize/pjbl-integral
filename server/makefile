setup:
	python3 -m venv venv
	./venv/Scripts/pip install --upgrade pip
	make install

install:
	./venv/Scripts/pip install -r requirements.txt

run:
	python -m uvicorn app.main:app --host=0.0.0.0 --port=80 --reload

run-dev:
	./venv/Scripts/python -m uvicorn app.main:app --reload