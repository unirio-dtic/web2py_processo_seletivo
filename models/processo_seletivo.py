# coding=utf-8

db.define_table('processo_seletivo',
    Field('nome', 'string', length=255, notnull=True),
    Field('gru',  'boolean', default='F', label='Utilização de GRU'),
    Field('forma_ingresso',  'boolean', default='F', label='Utilização de Forma de Ingresso'),
    Field('Reserva',  'boolean', default='F', label='Utilização de Reserva de Vagas'),
    Field('pne',  'boolean', default='F', label='Utilização de PNE'),
    Field('enem',  'boolean', default='F', label='Utilização do Enem'))

db.processo_seletivo.nome.requires = [IS_NOT_EMPTY(error_message=T('required field')),
                                      IS_UPPER(),
                                      IS_LENGTH(maxsize=255, error_message='O campo aceita no máximo 255 caracter(es)')]

db.define_table('edicao',
    Field('id_processo_seletivo', db.processo_seletivo, label='Processo Seletivo'),
    Field('ano', 'integer', notnull=True),
    Field('edicao', 'string', length=100),
    Field('dt_hr_inicio_inscr', 'datetime', label="Data Hora Início*"),
    Field('dt_hr_termino_inscr', 'datetime', label="Data Hora Término*"),
    Field('ativo', 'boolean', default='F', label='Edição ativa*'))

db.edicao.id_processo_seletivo.requires = IS_IN_DB(db, db.processo_seletivo.id, '%(nome)s', error_message=T('required field'))
db.edicao.ano.requires = [IS_NOT_EMPTY(error_message=T('required field')),
                          IS_INT_IN_RANGE(1500,9999)]
db.edicao.edicao.requires = [IS_EMPTY_OR(IS_UPPER()),
                             IS_EMPTY_OR(IS_LENGTH(maxsize=100, error_message='O campo aceita no máximo 100 caracter(es)'))]
db.edicao.dt_hr_inicio_inscr.requires = [IS_NOT_EMPTY(error_message=T('required field')),
                                     IS_DATETIME(format='%d/%m/%Y %H:%M', error_message='precisa ser no formato DD/MM/AAAA HH:MM')]
db.edicao.dt_hr_termino_inscr.requires = [IS_NOT_EMPTY(error_message=T('required field')),
                                     IS_DATETIME(format='%d/%m/%Y %H:%M', error_message='precisa ser no formato DD/MM/AAAA HH:MM')]
db.edicao.id_referencia.writable = db.edicao.id_referencia.readable = False

db.define_table('vaga',
    Field('id_edicao', db.edicao, label='Edição do Processo*'),
    Field('id_caracteristica_vaga', db.caracteristica_vaga, label='Nome da Vaga*'),
    Field('id_forma_ingresso', db.forma_ingresso, label='Forma de Ingresso*', default=1),
    Field('quantidade_vagas', 'integer', label='Vagas 1º acesso'),
    Field('quantidade_vagas2', 'integer', label='Vagas 2º acesso'),
    Field('id_acao_afirmativa', db.acao_afirmativa, label='Ação Afirmativa*'),
    Field('reservada_pne', 'boolean', default='F', label='Reservada(s) para PNE'),
    Field('valor_gru', 'double', label='Valor GRU (R$)'),
    Field('data_vencimento_gru', 'date'))

db.vaga.id_edicao.requires = IS_IN_SET(listaEdicoes, error_message=T('required field'))
db.vaga.id_caracteristica_vaga.requires = IS_IN_DB(db, db.caracteristica_vaga.id, '%(nome)s', error_message=T('required field'))
db.vaga.id_forma_ingresso.requires = IS_IN_DB(db, db.forma_ingresso.id, '%(descricao)s', error_message=T('required field'))
db.vaga.id_acao_afirmativa.requires = IS_IN_DB(db, db.acao_afirmativa.id, '%(descricao)s', error_message=T('required field'))
db.vaga.valor_gru.requires = IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0, 180, dot="."))
db.vaga.data_vencimento_gru.requires = IS_EMPTY_OR(IS_DATE(format='%d/%m/%Y', error_message='precisa ser no formato DD/MM/AAAA'))
