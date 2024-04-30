import redis

class RedisClient:

    # Dictionary of instance to connect a differents redis database
    __instances = {}

    def __new__(cls, redis_host, redis_port, redis_username, redis_password):
        #Create a tuple with the config of the connection to the database
        config_key = (redis_host,redis_port,redis_username,redis_password)

        if config_key not in cls.__instances:
            #Create a new object
            instance = super(RedisClient, cls).__new__(cls)
            #Save our objectec in __instances dic
            cls.__instances[config_key] = instance
            #Call the constructor
            instance.__init__(redis_host, redis_port, redis_username, redis_password)

            return cls.__instances[config_key]
    
    #Constructor of the class
    def __init__(self, redis_host, redis_port, redis_username, redis_password) -> None:
        #Atributes of our class
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_username = redis_username
        self.redis_pasword = redis_password
        self.client = None
    
    def connect(self):
        """
        Create a connection to the redis DB

        Return: A redis client
        """
        #Check if the instance of the object has been created before
        if self.client:
            return self.client
        try:
            self.client = redis.Redis(
                host=self.redis_host,
                port=self.redis_port,
                username= self.redis_username,
                password=self.redis_pasword,
                decode_responses=True
            )
            print("Connection to Redis DB successful")
        except:
            print("Connection to Redis DB failed")
    
    def ping(self):
        if self.client.ping():
            print("Ping: Pong") 

    def close(self)-> None:
        self.client.close()