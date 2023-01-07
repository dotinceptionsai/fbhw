# week3

# the post can be single or an array
```
curl http://192.168.1.241:8080/ -d'{"message": "hello"}'
{"result":[{"translation_text":"Hallo"}]}
curl http://192.168.1.241:8080/ -d'{"message": ["goodbye","hello"]}'
{"result":[{"translation_text":"Abschied"},{"translation_text":"Hallo"}]}$ 
```
# you can see the models saved
```
ls /data/models/
models--t5-base  t5-base  version.txt
```

