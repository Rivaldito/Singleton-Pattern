package redisclient

import (
	"sync"
	"time"

	"github.com/redis/go-redis/v9"
)

// The only instance of the class
var redisSinletonInstance *redisConnection

// For thread-safe
var once sync.Once

// The struct of the redis client
type redisConnection struct {
	RedisClient *redis.Client
}

// The constructor of the class
func GetRedisClient() (*redisConnection, error) {

	var (
		err error
		opt *redis.Options
	)

	once.Do(func() {
		//URL of our connection redis database
		redisURL := "redis://" + username + ":" + password + "@" + publicEndPoint

		//SET the options of the client connection
		opt, err = redis.ParseURL(redisURL)
		if err != nil {
			return
		}

		opt.DialTimeout = 5 * time.Second

		//Create the connections
		connection := redis.NewClient(opt)

		//save the connection in our "global-package" variable
		redisSinletonInstance = &redisConnection{
			RedisClient: connection,
		}

	})

	if err != nil {
		return nil, err
	}
	return redisSinletonInstance, nil

}
