### Build

Run ```make_dirs.sh``` to created volume directories with correct ownership
```bash
bash make_dirs.sh
```
Then run docker-compose
```bash
docker-compose up
```
If everything is ok, stop (Ctrl+C) and run in detached mode
```bash
docker-compose up -d
```
Create schema and table in MySQL workbench

Set MySQL datasource IP ```172.17.0.1``` in Grafana.

#### Secure NodeRED

Create and copy hashed password

```bash
docker exec -it nodered npx node-red admin hash-pw
```
```bash
docker-compose stop nodered
```
Uncomment the adminAuth section in ```settings.js``` and paste the hashed password. Then start NodeRED

```bash
docker-compose start node-red
```
Install ```node-red-contrib-stackhero-mysql``` to avoid ```ER_NOT_SUPPORTED_AUTH_MODE``` error.

Import ```.json``` flow containing example ```INSERT``` function.
