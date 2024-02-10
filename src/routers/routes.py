#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'luigelo@ldvloper.com'

from src.module.infrastructure.api_responses.success_response import SuccessResponse
from src.module.infrastructure.api_responses.models.success_response_model import SuccessResponseModel

"""
    Global Modules
"""
from fastapi import APIRouter

"""
    Routes modules
"""
from src.routers import isalive

router = APIRouter()

"""
    General Purpose Routes
"""


@router.get("/", response_model=SuccessResponseModel)
async def root():
    return SuccessResponse(message="API is alive", data={})
