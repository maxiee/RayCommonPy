SERVICE_NAME_RAYMQ = "RayMQ"

SERVICE_NAME = "name"
SERVICE_HOST = "host"
SERVICE_PORT = "port"

# 所有服务的注册表
services = [
    {
        SERVICE_NAME: SERVICE_NAME_RAYMQ,
        SERVICE_HOST: "100.114.157.36",
        SERVICE_PORT: 50051,
    }
]


def find_service(service_name):
    for service in services:
        if service["name"] == service_name:
            return service
    return None
