.PHONY: clean build run

UI_IMAGE="uncmath25/ai_agent_prototype_ui"
UI_CONTAINER="ai_agent_prototype_ui"
UI_PORT=8501
UI_LOCAL_DIR="ui"
UI_REMOTE_DIR="/app"
# LLM_IMAGE="ollama/ollama:latest"
# LLM_CONTAINER="ai_agent_prototype_llm"
LLM_PORT=11434

default: run

clean:
	@echo "*** Cleaning... ***"

build: clean
	@echo "*** Building Streamlit Docker image ... ***"
	docker build -t $(UI_IMAGE) -f Dockerfile-ui .

run: build
	@echo "*** Running Streamlit UI on http://localhost:8501 ... ***"
# 	docker run --rm -d \
# 		-p $(LLM_PORT):$(LLM_PORT) \
# 		--name $(LLM_CONTAINER) \
# 		$(LLM_IMAGE)
# 	docker exec -it ai_agent_prototype_llm ollama run llama3
	docker run --rm \
		-p $(UI_PORT):$(UI_PORT) \
		-v $$(pwd)/$(UI_LOCAL_DIR):$(UI_REMOTE_DIR) \
		--name $(UI_CONTAINER) \
		$(UI_IMAGE)
