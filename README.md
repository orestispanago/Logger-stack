### Docker-MySQL-NodeRED-Grafana

Docker stack with persistent data volumes for IoT data logging projects.

Some volumes contain an ```init``` folder with first run configurations,
MySQL users, schema, Grafana datasource etc.


#### Use as template

The ```docker-compose.yml``` file may be used as a template for other projects.
In this case make sure to:

* Clean up the init volumes definitions in ```docker-compose.yml```.
* Create volumes before first ```docker-compose up``` to avoid permission issues

Once the containers are successfully built and running:

* Create schema and table in MySQL workbench

* Set MySQL datasource IP ```172.17.0.1``` in Grafana.

* Secure NodeRED


#### Setting NodeRED admin password:

Create and copy hashed password

```bash
docker exec -it nodered npx node-red admin hash-pw
```
```bash
docker-compose stop node-red
```
Uncomment the adminAuth section in ```settings.js``` and paste the hashed password.

Start NodeRED

```bash
docker-compose start node-red

```

#### MySQL node tips

Install ```node-red-contrib-stackhero-mysql``` to avoid ```ER_NOT_SUPPORTED_AUTH_MODE``` error.

Import ```.json``` flow containing example ```INSERT``` function.
