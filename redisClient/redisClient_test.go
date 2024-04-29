package redisclient_test

import (
	"context"
	redisclient "test/redisClient"
	"testing"
)

func TestNewClient(t *testing.T) {

	//Create our redis connection instance
	redisConn, err := redisclient.GetRedisClient()

	//Check if we have an error
	if err != nil {
		t.Errorf("Got an error creating the client: %d", err)
	}

	//Check the connection
	conn := redisConn.RedisClient.Ping(context.Background())

	//Check if the attribute Error is != than nil
	if conn.Err() != nil {
		t.Errorf("Could not establish the connection, Error: %d", err)
	}

}

func TestIfIsSingleton(t *testing.T) {

	//Create one instance
	conn1, _ := redisclient.GetRedisClient()
	//Create one instance
	conn2, _ := redisclient.GetRedisClient()
	//Check if the instances are the same
	if conn1 != conn2 {
		t.Error("conn1 and conn2 are not the same instance")
	}

}
