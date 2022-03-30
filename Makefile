up:
	@docker compose build
	@docker compose up -d

stop:
	@docker compose stop

logs:
	@docker container logs -f identity.loqui.dev

create_db:
	@docker container exec -i identity_db.loqui.dev sh -c 'exec mysql -Didentity' < $(SCRIPT)
