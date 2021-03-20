MYSQL="./volumes/mysql"
GRAFANA="./volumes/grafana"
NODERED="./volumes/node-red"

mkdir -p $MYSQL/data
mkdir -p $MYSQL/init
mkdir -p $GRAFANA
mkdir -p $NODERED

cp init.sql $MYSQL/init
