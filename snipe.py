from web3 import EthereumTesterProvider, Web3
import json

rpcUrl = ""
web3 = Web3(EthereumTesterProvider())

uniswapFactory = web3.to_checksum_address("0x1F98431c8aD98523631AE4a59f267346ea31F984")
uniswapRouter = web3.to_checksum_address("0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45")
weth = web3.to_checksum_address("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")


factoryAbi = json.load(open("./abi/factory.json"))
routerAbi = json.load(open("./abi/router.json"))
erc20Abi = json.load(open("./abi/erc20.json"))
