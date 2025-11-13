from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    desc: str
    price: float
    qty: int

    # def __init__(self,id:int,name:str,desc:str,price:int,qty:int):
    #     self.id=id
    #     self.name=name
    #     self.desc=desc
    #     self.price=price
    #     self.qty=qty
