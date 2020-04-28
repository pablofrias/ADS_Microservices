import consul

c = consul.Consul(host='172.17.0.2', port=8500)
print(c.health.service('dictionary', passing=True))
print(c.health.service('dictionary', passing=True)[1][0]['Node']['Address'])
