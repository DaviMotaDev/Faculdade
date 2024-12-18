from boleto import Boleto
from cartão_credit import CartaoCredito

pagametno_cartao =  CartaoCredito()
pagamento_boleto = Boleto()

pagametno_cartao.validar_pagamento(120)
pagamento_boleto.validar_pagamento(50)

pagametno_cartao.processar_pagamento(120)
pagamento_boleto.processar_pagamento(50)