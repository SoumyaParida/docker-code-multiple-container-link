docker-test
=================

Run a simple python web service in a docker container linking to database running in another container.

###Demo

1. Run the mongo container, using the official mongoDB docker image.  This will take a moment to pull the necessary layers from the repository.

		$ docker run --name mongo -d mongo
		
	The Docker `run` command starts a container.  In this instance we are starting a container named mongo (`--name mongo`).  You can name a container whatever you want.  The `-d` indicates to start the container in daemonized mode, or as a background process.  And finally, the second `mongo` is the name of the image to run.  If the image is not located locally it will attempt to pull an image named `mongo` from the Docker repository.
	
	To make sure it's working correctly, view the running docker containers by executing the `docker ps` command.

		$ docker ps

		CONTAINER ID    IMAGE        COMMAND                  CREATED         STATUS         PORTS       NAMES
		c1fc1ef13e1d    mongo:latest "/entrypoint.sh mongod   5 seconds ago   Up 5 seconds   27017/tcp   mongo


2. Build the python web service container. Make sure to include the trailing '.'

		$ docker build -t webservice .
	
	This command creates a docker container named `webservice` based on the `Dockerfile` in the current directory.

3. Run our web service container and link it to the running mongo container.  Expose port 8000 and make it available to our host.
  
	*Notice that we also want to mount our local source code, so we can make code
changes on the fly.  Use the full path of your **myapp** directory.*

		$ docker run --name webservice -p 8000:8000 -v /docker-code-test/myapp:/usr/src/app --link mongo:mongo -d webservice

4. Browse to *<http://localhost:8000/>* to initialize our data.
5. Browse to *<http:/localhost:8000/index>* or *use the link on the web app home page* to see the data pulled from our mongo database container.

That's all there is to linking containers and using the environment variables
that are exposed to connect the containers together in an application.  

**But what if you want to actually get on the mongo console and see what is in your database?**

We are now on the mongo shell of our mongo database.  You can now view the data we are creating when visiting <http://localhost:8000/> easily.  
Our string data is in the database named '**slsdb**' in the '**strings**' collection.

	> use slsdb
	switched to db slsdb
	> show collections
	strings
	system.indexes
	> db.strings.find()
	{'_id': ObjectId('58bd4e8d7fe0f2000a247945'), 'string': ['hi', 'hihello']} 
	{'_id': ObjectId('58bd4f097ae372000a4e1f2c'), 'string': ['bye', 'byehello']} 