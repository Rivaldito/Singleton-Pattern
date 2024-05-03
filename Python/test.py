import unittest
import redis_client
import settings

class TestRedisClinet(unittest.TestCase):
    
    def test_constructor(self):

        client = redis_client.RedisClient(
        redis_host= settings.publicEndPoint,
        redis_port= settings.port,
        redis_password= settings.password,
        redis_username=settings.username
        )
        client.connect()
        self.assertIsNotNone(client.client,"Could not create the Redis client")
    
    def test_single_instance(self):

        r1 = redis_client.RedisClient(
        redis_host= settings.publicEndPoint,
        redis_port= settings.port,
        redis_password= settings.password,
        redis_username=settings.username
        )

        r1.connect()
        r2 = redis_client.RedisClient(
        redis_host= settings.publicEndPoint,
        redis_port= settings.port,
        redis_password= settings.password,
        redis_username=settings.username
        )
        r2.connect()

        self.assertNotEqual(r1,r2,"Not singleton instance")




if __name__ == "__main__":
    unittest.main()