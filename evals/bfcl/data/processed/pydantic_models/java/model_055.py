# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:58:51+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class SearchablesnapshotdirectoryCreate(BaseModel):
    repositories: str = Field(
        ..., description='The service that provides access to the repositories.'
    )
    cache: str = Field(..., description='The cache service.')
    indexSettings: str = Field(
        ..., description='The settings for the index that the shard belongs to.'
    )
    shardPath: str = Field(..., description='The path to the shard data.')
    currentTimeNanosSupplier: str = Field(
        ..., description='A supplier that provides the current time in nanoseconds.'
    )
    threadPool: str = Field(..., description='The thread pool for executing tasks.')
    blobStoreCacheService: str = Field(
        ..., description='The service for caching blobs.'
    )
    sharedBlobCacheService: str = Field(
        ..., description='The service for caching blobs shared across multiple shards.'
    )