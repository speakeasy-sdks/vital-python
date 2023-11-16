"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class LabTestCollectionMethod(str, Enum):
    r"""The method used to perform a lab test."""
    TESTKIT = 'testkit'
    WALK_IN_TEST = 'walk_in_test'
    AT_HOME_PHLEBOTOMY = 'at_home_phlebotomy'
