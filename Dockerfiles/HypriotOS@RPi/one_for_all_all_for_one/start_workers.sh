PROJECT='stock'  	# project 名稱
CONCURRENCY=1  		# 每個 worker 可以有幾個 subprocesses

cd /celery_projects
celery -A ${PROJECT} worker -n worker.%h --concurrency=${CONCURRENCY} --loglevel=INFO



