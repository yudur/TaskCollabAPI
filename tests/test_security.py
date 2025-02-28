import jwt

from taskcollabapi.core.env import env
from taskcollabapi.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    get_password_hash,
    verify_password,
)


def test_create_access_token():
    email = 'user@test.com'
    token = create_access_token(email)

    assert isinstance(token, str)

    payload = jwt.decode(token, env.secret_key, algorithms=env.jwt_algorithm)

    assert payload['sub'] == email
    assert 'exp' in payload
    assert 'jti' in payload


def test_create_refresh_token():
    email = 'user@test.com'
    token = create_refresh_token(email)

    assert isinstance(token, str)

    payload = jwt.decode(token, env.secret_key, algorithms=env.jwt_algorithm)

    assert payload['sub'] == email
    assert 'exp' in payload
    assert 'jti' in payload


def test_decode_token():
    email = 'user@test.com'
    token = create_access_token(email)
    decoded = decode_token(token)

    assert decoded is not None
    assert decoded.sub == email
    assert decoded.exp is not None
    assert decoded.jti is not None


def test_decode_invalid_token():
    invalid_token = 'invalid.token.string'
    decoded = decode_token(invalid_token)

    assert decoded is None


def test_password_hashing():
    password = 'secure.password'
    hashed_password = get_password_hash(password)

    assert isinstance(hashed_password, str)
    assert hashed_password != password


def test_verify_password():
    password = 'securepassword'
    hashed_password = get_password_hash(password)

    assert verify_password(password, hashed_password) is True
    assert verify_password('wrong.password', hashed_password) is False
