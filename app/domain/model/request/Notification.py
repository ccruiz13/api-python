from dataclasses import dataclass

@dataclass
class Notification:
    email: str
    phone: str
    message: str
