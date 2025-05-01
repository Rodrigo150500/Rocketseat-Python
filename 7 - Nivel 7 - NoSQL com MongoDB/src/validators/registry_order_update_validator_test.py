import pytest
from .registry_order_update_validator import registry_order_update_validator

def test_registry_order_update():

    body = {
            "data":{      
                "name": "Ronaldo",
                "address": "Rua adalberto",
                "cupom": False}            
            }
    
    registry_order_update_validator(body)

def test_registry_order_update_with_error():
    
    
    body = {
            "data":{      
                "name": "Ronaldo",
                "address": "Rua adalberto",
                "cupom": "ERRO"}            
            }
    
    with pytest.raises(Exception):
        registry_order_update_validator(body)