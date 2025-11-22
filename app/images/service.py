from app.config import settings
import cloudinary 
import cloudinary.uploader  

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
    secure=True
)

class CloudinaryService:
    @staticmethod
    def upload_image(file_path: str, folder: str = "mv") -> dict:
        response = cloudinary.uploader.upload(file_path, folder=folder)
        return response

    @staticmethod
    def delete_image(public_id: str) -> dict:
        response = cloudinary.uploader.destroy(public_id, resource_type = "image")
        return response