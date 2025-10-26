.PHONY: clean run

IMAGE="uncmath25/django_bitcoin_assets_dev"
CONTAINER="mariadb"
PORT=8501
REMOTE_DIR="/app"

default: run

clean:
	@echo "*** Cleaning... ***"

run: clean
	@echo "*** Running Streamlit Docker server on http://localhost:8501 ... ***"
	docker build -t $(IMAGE) -f Dockerfile .
	docker run --rm \
		-p $(PORT):$(PORT) \
		-v $$(pwd)/src:$(REMOTE_DIR) \
		--name $(CONTAINER) \
		$(IMAGE)
