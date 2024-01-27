.PHONY: all build clean install_dependencies test me laugh help

all: build ## Main task for local dev
	python3 -m http.server

build: test ## Bunbles and minifies the project
	bun script/bundle.ts

clean: ## Cleans all artifacts
	rm -rf build/

install_dependencies: ## Install dependencies
	sudo apt install cowsay
	bun install -d bun-types
	bun add @types/web -D
	bun install peerjs

test: ## Execute tests
	bun test
	bun test --coverage

# https://stackoverflow.com/questions/2019989/how-to-assign-the-output-of-a-command-to-a-makefile-variable
GENERATE_JOKE = $(shell curl -s "https://v2.jokeapi.dev/joke/Any?format=txt&type=single")
SET_JOKE = $(eval GGJ24_JOKE=$(GENERATE_JOKE))
me: ## Easter egg
	$(SET_JOKE)
	@cowsay $(GGJ24_JOKE)
laugh: ## Easter egg
	@echo "Hihi"

help: ## Show this help
	@grep -Eh '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

