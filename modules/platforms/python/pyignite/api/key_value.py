#
# Copyright 2019 GridGain Systems, Inc. and Contributors.
# 
# Licensed under the GridGain Community Edition License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.gridgain.com/products/software/community-edition/gridgain-community-edition-license
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import Iterable, Union

from pyignite.queries.op_codes import *
from pyignite.datatypes import (
    Map, Bool, Byte, Int, Long, AnyDataArray, AnyDataObject,
)
from pyignite.datatypes.key_value import PeekModes
from pyignite.queries import Query, Response
from pyignite.utils import cache_id


def cache_put(
    connection: 'Connection', cache: Union[str, int], key, value,
    key_hint=None, value_hint=None, binary=False, query_id=None,
) -> 'APIResult':
    """
    Puts a value with a given key to cache (overwriting existing value if any).

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param key: key for the cache entry. Can be of any supported type,
    :param value: value for the key,
    :param key_hint: (optional) Ignite data type, for which the given key
     should be converted,
    :param value_hint: (optional) Ignite data type, for which the given value
     should be converted.
    :param binary: (optional) pass True to keep the value in binary form.
     False by default,
    :param query_id: (optional) a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status if a value
     is written, non-zero status and an error description otherwise.
    """

    query_struct = Query(
        OP_CACHE_PUT,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('key', key_hint or AnyDataObject),
            ('value', value_hint or AnyDataObject),
        ],
        query_id=query_id,
    )
    return query_struct.perform(connection, {
        'hash_code': cache_id(cache),
        'flag': 1 if binary else 0,
        'key': key,
        'value': value,
    })


def cache_get(
    connection: 'Connection', cache: Union[str, int], key,
    key_hint=None, binary=False, query_id=None,
) -> 'APIResult':
    """
    Retrieves a value from cache by key.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param key: key for the cache entry. Can be of any supported type,
    :param key_hint: (optional) Ignite data type, for which the given key
     should be converted,
    :param binary: (optional) pass True to keep the value in binary form.
     False by default,
    :param query_id: (optional) a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status and a value
     retrieved on success, non-zero status and an error description on failure.
    """

    query_struct = Query(
        OP_CACHE_GET,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('key', key_hint or AnyDataObject),
        ],
        query_id=query_id,
    )
    result = query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'key': key,
        },
        response_config=[
           ('value', AnyDataObject),
        ],
    )
    if result.status != 0:
        return result
    result.value = result.value['value']
    return result


def cache_get_all(
    connection: 'Connection', cache: Union[str, int], keys: Iterable,
    binary=False, query_id=None,
) -> 'APIResult':
    """
    Retrieves multiple key-value pairs from cache.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param keys: list of keys or tuples of (key, key_hint),
    :param binary: (optional) pass True to keep the value in binary form.
     False by default,
    :param query_id: (optional) a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status and a dict, made of
     retrieved key-value pairs, non-zero status and an error description
     on failure.
    """

    query_struct = Query(
        OP_CACHE_GET_ALL,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('keys', AnyDataArray()),
        ],
        query_id=query_id,
    )
    result = query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'keys': keys,
        },
        response_config=[
            ('data', Map),
        ],
    )
    if result.status == 0:
        result.value = dict(result.value)['data']
    return result


def cache_put_all(
    connection: 'Connection', cache: Union[str, int], pairs: dict,
    binary=False, query_id=None,
) -> 'APIResult':
    """
    Puts multiple key-value pairs to cache (overwriting existing associations
    if any).

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param pairs: dictionary type parameters, contains key-value pairs to save.
     Each key or value can be an item of representable Python type or a tuple
     of (item, hint),
    :param binary: (optional) pass True to keep the value in binary form.
     False by default,
    :param query_id: (optional) a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status if key-value pairs
     are written, non-zero status and an error description otherwise.
    """

    query_struct = Query(
        OP_CACHE_PUT_ALL,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('data', Map),
        ],
        query_id=query_id,
    )
    return query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'data': pairs,
        },
    )


def cache_contains_key(
    connection: 'Connection', cache: Union[str, int], key,
    key_hint=None, binary=False, query_id=None,
) -> 'APIResult':
    """
    Returns a value indicating whether given key is present in cache.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param key: key for the cache entry. Can be of any supported type,
    :param key_hint: (optional) Ignite data type, for which the given key
     should be converted,
    :param binary: pass True to keep the value in binary form. False
     by default,
    :param query_id: a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status and a bool value
     retrieved on success: `True` when key is present, `False` otherwise,
     non-zero status and an error description on failure.
    """

    query_struct = Query(
        OP_CACHE_CONTAINS_KEY,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('key', key_hint or AnyDataObject),
        ],
        query_id=query_id,
    )
    result = query_struct.perform(
        connection,
            query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'key': key,
        },
        response_config=[
            ('value', Bool),
        ],
    )
    if result.status == 0:
        result.value = result.value['value']
    return result


def cache_contains_keys(
    connection: 'Connection', cache: Union[str, int], keys: Iterable,
    binary=False, query_id=None,
) -> 'APIResult':
    """
    Returns a value indicating whether all given keys are present in cache.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param keys: a list of keys or (key, type hint) tuples,
    :param binary: pass True to keep the value in binary form. False
     by default,
    :param query_id: a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status and a bool value
     retrieved on success: `True` when all keys are present, `False` otherwise,
     non-zero status and an error description on failure.
    """

    query_struct = Query(
        OP_CACHE_CONTAINS_KEYS,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('keys', AnyDataArray()),
        ],
        query_id=query_id,
    )
    result = query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'keys': keys,
        },
        response_config=[
            ('value', Bool),
        ],
    )
    if result.status == 0:
        result.value = result.value['value']
    return result


def cache_get_and_put(
    connection: 'Connection', cache: Union[str, int], key, value,
    key_hint=None, value_hint=None, binary=False, query_id=None,
) -> 'APIResult':
    """
    Puts a value with a given key to cache, and returns the previous value
    for that key, or null value if there was not such key.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param key: key for the cache entry. Can be of any supported type,
    :param value: value for the key,
    :param key_hint: (optional) Ignite data type, for which the given key
     should be converted,
    :param value_hint: (optional) Ignite data type, for which the given value
     should be converted.
    :param binary: pass True to keep the value in binary form. False
     by default,
    :param query_id: a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status and an old value
     or None if a value is written, non-zero status and an error description
     in case of error.
    """

    query_struct = Query(
        OP_CACHE_GET_AND_PUT,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('key', key_hint or AnyDataObject),
            ('value', value_hint or AnyDataObject),
        ],
        query_id=query_id,
    )
    result = query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'key': key,
            'value': value,
        },
        response_config=[
            ('value', AnyDataObject),
        ],
    )
    if result.status == 0:
        result.value = result.value['value']
    return result


def cache_get_and_replace(
    connection: 'Connection', cache: Union[str, int], key, value,
    key_hint=None, value_hint=None, binary=False, query_id=None,
) -> 'APIResult':
    """
    Puts a value with a given key to cache, returning previous value
    for that key, if and only if there is a value currently mapped
    for that key.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param key: key for the cache entry. Can be of any supported type,
    :param value: value for the key,
    :param key_hint: (optional) Ignite data type, for which the given key
     should be converted,
    :param value_hint: (optional) Ignite data type, for which the given value
     should be converted.
    :param binary: pass True to keep the value in binary form. False
     by default,
    :param query_id: a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status and an old value
     or None on success, non-zero status and an error description otherwise.
    """

    query_struct = Query(
        OP_CACHE_GET_AND_REPLACE, [
            ('hash_code', Int),
            ('flag', Byte),
            ('key', key_hint or AnyDataObject),
            ('value', value_hint or AnyDataObject),
        ],
        query_id=query_id,
    )
    result = query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'key': key,
            'value': value,
        },
        response_config=[
            ('value', AnyDataObject),
        ],
    )
    if result.status == 0:
        result.value = result.value['value']
    return result


def cache_get_and_remove(
    connection: 'Connection', cache: Union[str, int], key,
    key_hint=None, binary=False, query_id=None,
) -> 'APIResult':
    """
    Removes the cache entry with specified key, returning the value.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param key: key for the cache entry. Can be of any supported type,
    :param key_hint: (optional) Ignite data type, for which the given key
     should be converted,
    :param binary: pass True to keep the value in binary form. False
     by default,
    :param query_id: a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status and an old value
     or None, non-zero status and an error description otherwise.
    """

    query_struct = Query(
        OP_CACHE_GET_AND_REMOVE, [
            ('hash_code', Int),
            ('flag', Byte),
            ('key', key_hint or AnyDataObject),
        ],
        query_id=query_id,
    )
    result = query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'key': key,
        },
        response_config=[
            ('value', AnyDataObject),
        ],
    )
    if result.status == 0:
        result.value = result.value['value']
    return result


def cache_put_if_absent(
    connection: 'Connection', cache: Union[str, int], key, value,
    key_hint=None, value_hint=None, binary=False, query_id=None,
) -> 'APIResult':
    """
    Puts a value with a given key to cache only if the key
    does not already exist.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param key: key for the cache entry. Can be of any supported type,
    :param value: value for the key,
    :param key_hint: (optional) Ignite data type, for which the given key
     should be converted,
    :param value_hint: (optional) Ignite data type, for which the given value
     should be converted.
    :param binary: (optional) pass True to keep the value in binary form. False
     by default,
    :param query_id: (optional) a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status on success,
     non-zero status and an error description otherwise.
    """

    query_struct = Query(
        OP_CACHE_PUT_IF_ABSENT,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('key', key_hint or AnyDataObject),
            ('value', value_hint or AnyDataObject),
        ],
        query_id=query_id,
    )
    result = query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'key': key,
            'value': value,
        },
        response_config=[
            ('success', Bool),
        ],
    )
    if result.status == 0:
        result.value = result.value['success']
    return result


def cache_get_and_put_if_absent(
    connection: 'Connection', cache: Union[str, int], key, value,
    key_hint=None, value_hint=None, binary=False, query_id=None,
) -> 'APIResult':
    """
    Puts a value with a given key to cache only if the key does not
    already exist.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param key: key for the cache entry. Can be of any supported type,
    :param value: value for the key,
    :param key_hint: (optional) Ignite data type, for which the given key
     should be converted,
    :param value_hint: (optional) Ignite data type, for which the given value
     should be converted.
    :param binary: (optional) pass True to keep the value in binary form. False
     by default,
    :param query_id: (optional) a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status and an old value
     or None on success, non-zero status and an error description otherwise.
    """

    query_struct = Query(
        OP_CACHE_GET_AND_PUT_IF_ABSENT,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('key', key_hint or AnyDataObject),
            ('value', value_hint or AnyDataObject),
        ],
        query_id=query_id,
    )
    result = query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'key': key,
            'value': value,
        },
        response_config=[
            ('value', AnyDataObject),
        ],
    )
    if result.status == 0:
        result.value = result.value['value']
    return result


def cache_replace(
    connection: 'Connection', cache: Union[str, int], key, value,
    key_hint=None, value_hint=None, binary=False, query_id=None,
) -> 'APIResult':
    """
    Puts a value with a given key to cache only if the key already exist.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param key: key for the cache entry. Can be of any supported type,
    :param value: value for the key,
    :param key_hint: (optional) Ignite data type, for which the given key
     should be converted,
    :param value_hint: (optional) Ignite data type, for which the given value
     should be converted.
    :param binary: pass True to keep the value in binary form. False
     by default,
    :param query_id: a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status and a boolean
     success code, or non-zero status and an error description if something
     has gone wrong.
    """

    query_struct = Query(
        OP_CACHE_REPLACE,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('key', key_hint or AnyDataObject),
            ('value', value_hint or AnyDataObject),
        ],
        query_id=query_id,
    )
    result = query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'key': key,
            'value': value,
        },
        response_config=[
            ('success', Bool),
        ],
    )
    if result.status == 0:
        result.value = result.value['success']
    return result


def cache_replace_if_equals(
    connection: 'Connection', cache: Union[str, int], key, sample, value,
    key_hint=None, sample_hint=None, value_hint=None,
    binary=False, query_id=None,
) -> 'APIResult':
    """
    Puts a value with a given key to cache only if the key already exists
    and value equals provided sample.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param key:  key for the cache entry,
    :param sample: a sample to compare the stored value with,
    :param value: new value for the given key,
    :param key_hint: (optional) Ignite data type, for which the given key
     should be converted,
    :param sample_hint: (optional) Ignite data type, for whic
     the given sample should be converted
    :param value_hint: (optional) Ignite data type, for which the given value
     should be converted,
    :param binary: (optional) pass True to keep the value in binary form.
     False by default,
    :param query_id: (optional) a value generated by client and returned
     as-is in response.query_id. When the parameter is omitted, a random
     value is generated,
    :return: API result data object. Contains zero status and a boolean
     success code, or non-zero status and an error description if something
     has gone wrong.
    """

    query_struct = Query(
        OP_CACHE_REPLACE_IF_EQUALS,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('key', key_hint or AnyDataObject),
            ('sample', sample_hint or AnyDataObject),
            ('value', value_hint or AnyDataObject),
        ],
        query_id=query_id,
    )
    result = query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'key': key,
            'sample': sample,
            'value': value,
        },
        response_config=[
            ('success', Bool),
        ],
    )
    if result.status == 0:
        result.value = result.value['success']
    return result


def cache_clear(
    connection: 'Connection', cache: Union[str, int], binary=False,
    query_id=None,
) -> 'APIResult':
    """
    Clears the cache without notifying listeners or cache writers.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param binary: (optional) pass True to keep the value in binary form.
     False by default,
    :param query_id: (optional) a value generated by client and returned
     as-is in response.query_id. When the parameter is omitted, a random
     value is generated,
    :return: API result data object. Contains zero status on success,
     non-zero status and an error description otherwise.
    """

    query_struct = Query(
        OP_CACHE_CLEAR,
        [
            ('hash_code', Int),
            ('flag', Byte),
        ],
        query_id=query_id,
    )
    return query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
        },
    )


def cache_clear_key(
    connection: 'Connection', cache: Union[str, int], key,
    key_hint: object=None, binary=False, query_id=None,
) -> 'APIResult':
    """
    Clears the cache key without notifying listeners or cache writers.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param key:  key for the cache entry,
    :param key_hint: (optional) Ignite data type, for which the given key
     should be converted,
    :param binary: (optional) pass True to keep the value in binary form.
     False by default,
    :param query_id: (optional) a value generated by client and returned
     as-is in response.query_id. When the parameter is omitted, a random
     value is generated,
    :return: API result data object. Contains zero status on success,
     non-zero status and an error description otherwise.
    """

    query_struct = Query(
        OP_CACHE_CLEAR_KEY,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('key', key_hint or AnyDataObject),
        ],
        query_id=query_id,
    )
    return query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'key': key,
        },
    )


def cache_clear_keys(
    connection: 'Connection', cache: Union[str, int], keys: list,
    binary=False, query_id=None,
) -> 'APIResult':
    """
    Clears the cache keys without notifying listeners or cache writers.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param keys: list of keys or tuples of (key, key_hint),
    :param binary: (optional) pass True to keep the value in binary form.
     False by default,
    :param query_id: (optional) a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status on success,
     non-zero status and an error description otherwise.
    """

    query_struct = Query(
        OP_CACHE_CLEAR_KEYS,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('keys', AnyDataArray()),
        ],
        query_id=query_id,
    )
    return query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'keys': keys,
        },
    )


def cache_remove_key(
    connection: 'Connection', cache: Union[str, int], key,
    key_hint: object=None, binary=False, query_id=None,
) -> 'APIResult':
    """
    Clears the cache key without notifying listeners or cache writers.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param key:  key for the cache entry,
    :param key_hint: (optional) Ignite data type, for which the given key
     should be converted,
    :param binary: (optional) pass True to keep the value in binary form.
     False by default,
    :param query_id: (optional) a value generated by client and returned
     as-is in response.query_id. When the parameter is omitted, a random
     value is generated,
    :return: API result data object. Contains zero status and a boolean
     success code, or non-zero status and an error description if something
     has gone wrong.
    """

    query_struct = Query(
        OP_CACHE_REMOVE_KEY,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('key', key_hint or AnyDataObject),
        ],
        query_id=query_id,
    )
    result = query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'key': key,
        },
        response_config=[
            ('success', Bool),
        ],
    )
    if result.status == 0:
        result.value = result.value['success']
    return result


def cache_remove_if_equals(
    connection: 'Connection', cache: Union[str, int], key, sample,
    key_hint=None, sample_hint=None,
    binary=False, query_id=None,
) -> 'APIResult':
    """
    Removes an entry with a given key if provided value is equal to
    actual value, notifying listeners and cache writers.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param key:  key for the cache entry,
    :param sample: a sample to compare the stored value with,
    :param key_hint: (optional) Ignite data type, for which the given key
     should be converted,
    :param sample_hint: (optional) Ignite data type, for whic
     the given sample should be converted
    :param binary: (optional) pass True to keep the value in binary form.
     False by default,
    :param query_id: (optional) a value generated by client and returned
     as-is in response.query_id. When the parameter is omitted, a random
     value is generated,
    :return: API result data object. Contains zero status and a boolean
     success code, or non-zero status and an error description if something
     has gone wrong.
    """

    query_struct = Query(
        OP_CACHE_REMOVE_IF_EQUALS,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('key', key_hint or AnyDataObject),
            ('sample', sample_hint or AnyDataObject),
        ],
        query_id=query_id,
    )
    result = query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'key': key,
            'sample': sample,
        },
        response_config=[
            ('success', Bool),
        ],
    )
    if result.status == 0:
        result.value = result.value['success']
    return result


def cache_remove_keys(
    connection: 'Connection', cache: Union[str, int], keys: Iterable,
    binary=False, query_id=None,
) -> 'APIResult':
    """
    Removes entries with given keys, notifying listeners and cache writers.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param keys: list of keys or tuples of (key, key_hint),
    :param binary: (optional) pass True to keep the value in binary form.
     False by default,
    :param query_id: (optional) a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status on success,
     non-zero status and an error description otherwise.
    """

    query_struct = Query(
        OP_CACHE_REMOVE_KEYS,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('keys', AnyDataArray()),
        ],
        query_id=query_id,
    )
    return query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'keys': keys,
        },
    )


def cache_remove_all(
    connection: 'Connection', cache: Union[str, int], binary=False,
    query_id=None,
) -> 'APIResult':
    """
    Removes all entries from cache, notifying listeners and cache writers.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param binary: (optional) pass True to keep the value in binary form.
     False by default,
    :param query_id: (optional) a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status on success,
     non-zero status and an error description otherwise.
    """

    query_struct = Query(
        OP_CACHE_REMOVE_ALL,
        [
            ('hash_code', Int),
            ('flag', Byte),
        ],
        query_id=query_id,
    )
    return query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
        },
    )


def cache_get_size(
    connection: 'Connection', cache: Union[str, int], peek_modes=0,
    binary=False, query_id=None,
) -> 'APIResult':
    """
    Gets the number of entries in cache.

    :param connection: connection to Ignite server,
    :param cache: name or ID of the cache,
    :param peek_modes: (optional) limit count to near cache partition
     (PeekModes.NEAR), primary cache (PeekModes.PRIMARY), or backup cache
     (PeekModes.BACKUP). Defaults to all cache partitions (PeekModes.ALL),
    :param binary: (optional) pass True to keep the value in binary form.
     False by default,
    :param query_id: (optional) a value generated by client and returned as-is
     in response.query_id. When the parameter is omitted, a random value
     is generated,
    :return: API result data object. Contains zero status and a number of
     cache entries on success, non-zero status and an error description
     otherwise.
    """
    if not isinstance(peek_modes, (list, tuple)):
        if peek_modes == 0:
            peek_modes = []
        else:
            peek_modes = [peek_modes]

    query_struct = Query(
        OP_CACHE_GET_SIZE,
        [
            ('hash_code', Int),
            ('flag', Byte),
            ('peek_modes', PeekModes),
        ],
        query_id=query_id,
    )
    result = query_struct.perform(
        connection,
        query_params={
            'hash_code': cache_id(cache),
            'flag': 1 if binary else 0,
            'peek_modes': peek_modes,
        },
        response_config=[
            ('count', Long),
        ],
    )
    if result.status == 0:
        result.value = result.value['count']
    return result
