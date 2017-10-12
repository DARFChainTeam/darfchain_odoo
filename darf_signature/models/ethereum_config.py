from openerp import models, fields, api
from openerp.tools.translate import _
import logging
#from fingerprint import Fingerprint
from dateutil import relativedelta
from datetime import datetime as dt
import base64
import hashlib
from openerp.exceptions import UserError
from web3 import Web3, HTTPProvider, IPCProvider


class EthereumConfig(models.Model):
    
    _name = 'ethereum.config'
    
    ethereum_address = fields.Char(string="Ethereum smart-contract address")
    ethereum_interface = fields.Char(string="Ethereum smart contract interface")
    ethereum_node = fields.Char(string="Ethereum node")
    
    
    