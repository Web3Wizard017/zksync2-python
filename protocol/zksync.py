from protocol.zksync_module import ZkSync
from protocol.zksync_provider import ZkSyncProvider
from protocol.middleware import build_zksync_middleware

from typing import Union, Optional
from web3._utils.module import attach_modules
from eth_typing import URI
from web3 import Web3


class ZkSyncBuilder:
    @classmethod
    def build(cls, url: Optional[Union[URI, str]]) -> Web3:
        web3_module = Web3()
        zksync_provider = ZkSyncProvider(url)
        zksync_middleware = build_zksync_middleware(zksync_provider)
        web3_module.middleware_onion.add(zksync_middleware)
        attach_modules(web3_module, {"zksync": (ZkSync,)})
        return web3_module
