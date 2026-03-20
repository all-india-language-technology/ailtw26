.PHONY: build force clean serve

build:
	python scripts/build.py

force:
	python scripts/build.py --force

clean:
	python scripts/build.py --clean-only

serve:
	python -m http.server 8000 --directory docs
