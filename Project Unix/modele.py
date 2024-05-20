from dataclasses import dataclass, field

@dataclass
class Account :
    email:str
    password:str

@dataclass
class SecureLogs:
    source_name: str
    day: str
    nombre: int
    time: str
    localisation: str
    ssh_protocole: str
    log_info: str
    address: str

@dataclass
class ApacheLogs:
    source_name: str
    ip_address: str
    date: str
    day: int
    month: int
    year: int
    time: str
    method: str
    http: str
    status: int
    size: int
    urls: str
    software: str
    operating_system: str
    browser: str
    http_request: str