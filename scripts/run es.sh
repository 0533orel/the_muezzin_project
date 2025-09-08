docker run -d --name es \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  -p 9200:9200 -p 9400:9400 \
  docker.elastic.co/elasticsearch/elasticsearch:8.15.0
