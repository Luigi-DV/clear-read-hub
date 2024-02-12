from azure.storage.blob import BlobClient

from src.module.infrastructure.external_services.azure_storage.blob_sas import AzureStorageBlobSas

"""
    API Modules
"""
from src.core.settings import coresettings

"""
    Infrastructure Modules
"""
from src.module.infrastructure.external_services.azure_storage.container_client import AzureStorageContainerClient
from src.module.infrastructure.external_services.azure_storage.file_uploader import AzureStorageFileUploader

"""
    Domain Modules
"""
from src.module.domain.repositories.FileRepository import FileRepository
from src.module.domain.entities.File import File


class AzureStorageFileInterface(FileRepository):
    def __init__(self):
        pass

    async def save(self, file: File) -> BlobClient:
        uploader = AzureStorageFileUploader(coresettings.AZ_STORAGE_CONNECTION_STRING)
        container_client = AzureStorageContainerClient().client
        # Upload the file
        blob_client = uploader.upload_file(file.content.read(), container_client.container_name, file.filename)
        # Return the blob client
        return blob_client

    async def get_sas_token_url(self, blob_client: BlobClient) -> str:
        # Create a new instance of the AzureStorageBlobSas class
        azure_blob_sas = AzureStorageBlobSas(blob_client)

        # Return the blob URL with the SAS token
        return azure_blob_sas.generate_read_sas()
