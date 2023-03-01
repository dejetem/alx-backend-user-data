#!/usr/bin/env python3
"""
module user passwords validation
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    encodes a str argument and returing a
    hashed password which is a byte string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    checks if the provided password matches the
    hashed password
    Returns:
        True if valid(matches) or False if invalid
    """
    is_valid = False
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        is_valid = True
    return is_valid
