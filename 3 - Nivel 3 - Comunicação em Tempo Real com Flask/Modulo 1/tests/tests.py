import sys
sys.path.append('../')

import os
import pytest
from payment.pix import Pix

def test_create_pix():

    payment_pix = Pix()

    payment_pix_info = payment_pix.create_pix(base="../")

    assert 'bank_payment_id' in payment_pix_info
    assert 'qr_code' in payment_pix_info

    assert os.path.isfile(f"../static/img/{payment_pix_info.get('qr_code')}.png")
    
    