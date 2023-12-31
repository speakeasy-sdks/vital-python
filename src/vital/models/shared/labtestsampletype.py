"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class LabTestSampleType(str, Enum):
    r"""The type of sample used to perform a lab test."""
    DRIED_BLOOD_SPOT = 'dried_blood_spot'
    SERUM = 'serum'
    SALIVA = 'saliva'
    URINE = 'urine'
