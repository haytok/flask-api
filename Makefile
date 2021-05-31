# 開発環境
.PHONY: dev-build
dev-build:
	docker-compose build

.PHONY: dev-up
dev-up:
	docker-compose up

.PHONY: dev-down
dev-down:
	docker-compose down
