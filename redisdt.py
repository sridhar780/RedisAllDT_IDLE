import redis

#connect
conn=redis.Redis(host='localhost',port=6379,db=0)


#string
conn.set('str1','siva sivani')
print(conn.get('str1'))



#Hashes

conn.hset('hash1','f1',100)
conn.hset('hash1','f2','raj')
conn.hset('hash1','f3','ds')
print(conn.hgetall('hash1'))



#list

conn.rpush('l1','bscds')
conn.rpush('l1','bscai&ml')
conn.lpush('l1','bsc-CSE')
print(conn.lrange('l1',0,-1))
conn.lpush('l1','bsc-MSCS')
print(conn.lrange('l1',0,-1))


#set

conn.sadd('set1',35000)
conn.sadd('set1',45000)
print(conn.smembers('set1'))


#Sorted Set

conn.zadd('score',{'rohith':150})
conn.zadd('score',{'Virat':157})
print(conn.zrange('score',0,-1,withscores=True))

#bitmaps
conn.setbit('bit1',0,1)
conn.setbit('bit1',1,0)
print(conn.getbit('bit',0))


