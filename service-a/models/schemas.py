from pydantic import BaseModel
from ipaddress import IPv4Address

class Ip(BaseModel):
    ip: IPv4Address