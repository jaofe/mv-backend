from fastapi import HTTPException, status, UploadFile
from sqlalchemy.orm import Session
from app.products.schema import ProductCreate, ProductResponse
from app.products.repository import create_product
from app.species.repository import get_species_by_id
from app.images.service import CloudinaryService
import tempfile
import os


def create_new_product(
    db: Session,
    product_data: ProductCreate,
    user_id: int,
    images: list[UploadFile] | None = None
) -> ProductResponse:
    # Verify species exists
    species = get_species_by_id(db, product_data.species_id)
    if not species:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Species not found"
        )
    
    # Handle image uploads if provided
    image_urls = []
    if images:
        cloudinary_service = CloudinaryService()
        
        for image in images:
            try:
                # Save uploaded file temporarily
                with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(image.filename)[1]) as temp_file:
                    content = image.file.read()
                    temp_file.write(content)
                    temp_file_path = temp_file.name
                
                # Upload to Cloudinary
                result = cloudinary_service.upload_image(temp_file_path, folder="products")
                image_urls.append(result['secure_url'])
                
                # Clean up temporary file
                os.unlink(temp_file_path)
                
            except Exception as e:
                # Clean up any uploaded images if one fails
                for url in image_urls:
                    try:
                        public_id = url.split('/')[-1].split('.')[0]
                        cloudinary_service.delete_image(f"products/{public_id}")
                    except:
                        pass
                
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Failed to upload image: {str(e)}"
                )
    
    # Create product
    new_product = create_product(
        db=db,
        name=product_data.name,
        weight=product_data.weight,
        price=product_data.price,
        fishing_date=product_data.fishing_date,
        description=product_data.description,
        species_id=product_data.species_id,
        user_id=user_id,
        image_urls=image_urls if image_urls else None,
        status="available"
    )
    
    return ProductResponse.model_validate(new_product)
