
receiver-image:
	docker build -t receiver-bot:latest -f ./docker/receiver/Dockerfile .

bot-image:
	docker build -t bot:latest -f ./docker/bot/Dockerfile .

up-receiver-container:
	docker stop receiver-bot || true
	docker run --rm -d -p 5000:5000 --env-file ./env.sh --name receiver-bot receiver-bot:latest
flow: add commit push

add:
	git add .

commit:
	git commit -m "`git status -s`"

push:
	git push origin `git rev-parse --abbrev-ref HEAD`
