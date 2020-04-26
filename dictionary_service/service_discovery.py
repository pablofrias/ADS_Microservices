import consul
import random

c = consul.Consul(host='172.17.0.2', port=8500)
print(c.catalog.service('dictionary'))
print(c.catalog.service('dictionary')[1][0]['Address'])


def registerService(serviceName, serviceAddress, servicePort):
    pos = str(random.randrange(10))
    c.agent.service.register(serviceName, \
                                service_id=serviceName + pos, \
                                address=serviceAddress,\
                                port=servicePort)


def unregisterService(serviceName):
    c.agent.service.deregister(serviceName)

def getServiceIP(serviceName):
    print(c.agent.services())
