from dataclasses import dataclass
from typing import Optional

from didcomm.did_doc.did_resolver import DIDResolver
from didcomm.errors import DIDResolverNotProvidedError, SecretsResolverNotProvidedError
from didcomm.secrets.secrets_resolver import SecretsResolver


# TODO: Decide if we want to provide a possiblity to register default resolvers,
# or it's better to always pass ResolversConfig explicitly to every pack/sign/unpack/etc. methods.

default_did_resolver: Optional[DIDResolver] = None

default_secrets_resolver: Optional[SecretsResolver] = None


def register_default_did_resolver(did_resolver: DIDResolver):
    """
    Registers a DID Resolver that can be used in all pack/unpack operations by default.

    :param did_resolver: a default DID resolver to be registered.
    """
    global default_did_resolver
    default_did_resolver = did_resolver


def register_default_secrets_resolver(secrets_resolver: SecretsResolver):
    """
    Registers a Secrets Resolver that can be used in all pack/unpack operations by default.

    :param secrets_resolver: a default _secrets resolver to be registered.
    """
    global default_secrets_resolver
    default_secrets_resolver = secrets_resolver


@dataclass(frozen=True)
class ResolversConfig:
    """
    Resolvers configuration.

    Attributes:
        secrets_resolver (SecretsResolver): an optional _secrets resolver that can override a default _secrets resolver
        registered by 'register_default_secrets_resolver'

        did_resolver (DIDResolver): an optional DID Doc resolver that can override a default DID Doc resolver
        registered by 'register_default_did_resolver'
    """

    secrets_resolver: Optional[SecretsResolver] = None
    did_resolver: Optional[DIDResolver] = None


def get_effective_resolvers(resolvers_config: ResolversConfig) -> ResolversConfig:
    if resolvers_config and resolvers_config.secrets_resolver:
        secrets_resolver = resolvers_config.secrets_resolver
    else:
        secrets_resolver = default_secrets_resolver

    if secrets_resolver is None:
        raise SecretsResolverNotProvidedError()

    if resolvers_config and resolvers_config.did_resolver:
        did_resolver = resolvers_config.did_resolver
    else:
        did_resolver = default_did_resolver

    if did_resolver is None:
        raise DIDResolverNotProvidedError()

    return ResolversConfig(secrets_resolver, did_resolver)
