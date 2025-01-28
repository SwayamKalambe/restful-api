from fastapi import APIRouter, HTTPException, Depends, status
from database import get_db
from models import FashionItems, Users
from schema import CreateFashionItem, UpdateFashionItem, FashionItemResponse
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schema import UserCreate, UserResponse
from auth import (get_current_user, 
                  create_access_token, 
                  authenticate_user, 
                  get_user_by_email, 
                  get_user, 
                  hash_password)

router = APIRouter()


# OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Register a new user
@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    if get_user(db, username=user.username):
        raise HTTPException(status_code=400, detail="Username already taken")
    
    hashed_pass = hash_password(user.password)

    new_user = Users(username=user.username, email=user.email, password=hashed_pass)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# Login and get access token
@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Retrieve all items (protected)
@router.get("/items", response_model=list[FashionItemResponse])
async def get_items(
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
):
    return db.query(FashionItems).all()

# Add a new item (protected)
@router.post("/items", response_model=FashionItemResponse)
async def create_items(
    item: CreateFashionItem,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
):
    new_item = FashionItems(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# Retrieve an item by ID (protected)
@router.get("/items/{item_id}", response_model=FashionItemResponse)
async def get_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
):
    item = db.query(FashionItems).filter(FashionItems.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not Found")
    return item

# Update an item (protected)
@router.put("/items/{item_id}", response_model=FashionItemResponse)
async def update_item(
    item_id: int,
    updated_item: UpdateFashionItem,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
):
    item = db.query(FashionItems).filter(FashionItems.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not Found")
    
    for key, value in updated_item.model_dump().items():
        setattr(item, key, value)
    db.commit()
    return item

# Partially update an item (protected)
@router.patch("/items/{item_id}", response_model=FashionItemResponse)
async def update_item_partial(
    item_id: int,
    updated_item: UpdateFashionItem,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
):
    item = db.query(FashionItems).filter(FashionItems.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not Found")
    
    for key, value in updated_item.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

# Delete an item (protected)
@router.delete("/items/{item_id}")
async def delete(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
):
    item = db.query(FashionItems).filter(FashionItems.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not Found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}