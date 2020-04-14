tag_project_name = "telegraf"

app_count = 4

app_image = "961225894672.dkr.ecr.us-west-2.amazonaws.com/telegraf:1.3"

fargate_cpu = 4096

fargate_memory = 8192

app_port = 8086

webhook_port = 1619

influxdb_url = "https://hilldale-b40313e5.influxcloud.net:8086"

influxdb_db = "relops_workers"

influxdb_user = "relops_wo"

interval = "300s"

medium_interval = "600s"

long_interval = "1200s"
