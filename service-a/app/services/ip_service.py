from pydantic import BaseModel, IPvAnyAddress

class Ip(BaseModel):
    ip: IPvAnyAddress