from ctypes import get_last_error

#arquivo onde está os inputs de classificação da transação
import classification

#decide pra onde vai depois de classificada a transação
if classification.tp_lancamento == 'm':
    import manual

if classification.tp_lancamento == 'n':
    if classification.estado_lancamento == '1':
        import nfe
    else:
        import nfe_sc
##Fechando programa
print('\n######## OBRIGADO E VOLTE SEMPRE ########\n')