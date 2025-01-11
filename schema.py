from pydantic import BaseModel, Field

class FashionItem(BaseModel):
    name: str = Field(...,min_length=1 ,title="Name of the fashion item", example= "T-shirt")
    price: float = Field(..., gt = 0, title="Price of the item")
    description: str = Field(None, title= "Item Information")
    

class CreateFashionItem(FashionItem):
    pass

class DeleteFashionItem(FashionItem):
    id: int = Field(..., title="ID of the item to delete")

    class Config:
        orm_mode = True

class UpdateFashionItem(FashionItem):
    pass
  
class FashionItemResponse(FashionItem):
    id: int


    class Config:
        orm_mode = True
    

class UserCreate(BaseModel):
    username: str = Field(..., min_length=1)
    email: str = Field(..., email=True)
    password: str = Field(..., min_length=8)


class UserResponse(BaseModel):
    username: str
    email: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
