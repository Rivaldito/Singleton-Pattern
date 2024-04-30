import settings
import redis_client

if __name__ == "__main__":
    
    r1 = redis_client.RedisClient(
        redis_host= settings.publicEndPoint,
        redis_port= settings.port,
        redis_password= settings.password,
        redis_username=settings.username
    )

    r1.connect()
    r1.ping()

     
    print(r1)

