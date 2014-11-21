# log_inscricao #

db.define_table('log_inscricao',
    Field('inscricao', 'string', length=10),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'))

#####

# log_verificar_status #

db.define_table('log_verificar_status',
    Field('cpf_usuario', 'string', length=15),
    Field('inscricao', 'string', length=10),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'),migrate=True)

#####

# log_alterar_email #

db.define_table('log_alterar_email',
    Field('cpf_usuario', 'string', length=15),
    Field('candidato_cpf', 'string', length=15),
    Field('antigo_email', 'string', length=90),
    Field('novo_email', 'string', length=90),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'),migrate=True)

#####

# log_alocacao_individual
db.define_table('log_alocacao_individual',
    Field('cpf_responsavel', 'string', length=15),
    Field('id_inscricao_pessoa', 'string'),
    Field('id_vaga_fase', 'string'),
    Field('id_sala', 'string'),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'),migrate=True)

# log_verificar_cpl #

db.define_table('log_verificar_cpl',
    Field('cpf_usuario', 'string', length=15),
    Field('inscricao', 'string', length=10),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'),migrate=True)

#####

# log_indicacao #

db.define_table('log_indicacao',
    Field('cpf_indicado', 'string', length=15),
    Field('cpf_responsavel', 'string', length=15),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'),migrate=True)

#####

# log_permissao_atividade #

db.define_table('log_permissao_atividade',
    Field('cpf_responsavel', 'string', length=17),
    Field('id_edicao_colaborador', 'string', length=17),
    Field('cpf_alterado', 'string', length=17),
    Field('id_atividade', 'string', length=30),
    Field('quantidade', 'integer'),
    Field('tipo', 'string', length=20),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'),migrate=True)

#####

# log_permissao_local #

db.define_table('log_permissao_local',
    Field('cpf_responsavel', 'string', length=17),
    Field('cpf_alterado', 'string', length=17),
    Field('id_local', 'string', length=30),
    Field('tipo', 'string', length=20),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'),migrate=True)

#####

# log_selecao #

db.define_table('log_selecao',
    Field('cpf_responsavel', 'string', length=15),
    Field('id_inscricao', 'string'),
    Field('status', 'boolean'),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'),migrate=True)

#####

# log_funcao #

db.define_table('log_funcao',
    Field('cpf_responsavel', 'string', length=15),
    Field('id_inscricao', 'string'),
    Field('id_atividade', 'string'),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'),migrate=True)

#####

# log_local #

db.define_table('log_local',
    Field('cpf_responsavel', 'string', length=15),
    Field('id_inscricao', 'string'),
    Field('id_local', 'string'),
    Field('tipo', 'string',length=1),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'),migrate=True)

#####

# log_status_inscricao #

db.define_table('log_status_inscricao',
    Field('inscricao', 'string', length=10),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'))

#####

# log_alteracao_inscricao #

db.define_table('log_alteracao_inscricao',
    Field('inscricao', 'string', length=10),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'))

#####

# log_consulta_clp #

db.define_table('log_consulta_clp',
    Field('inscricao', 'string', length=10),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'))

#####

# log_parecer #

db.define_table('log_parecer',
    Field('login', 'string', length=14),
    Field('id_inscricao', 'string', length=15),
    Field('deferida', 'boolean'),
    Field('cra', 'string', length=10),
    Field('nota_psd', 'string',length=10 ),
    Field('motivo', 'string'),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'))

#####

# log_emails_colaborador #

db.define_table('log_emails_colaborador',
    Field('login', 'string', length=15),
    Field('cpf_colaborador', 'string', length=15),
    Field('edicao_colaborador', 'integer'),
    Field('id_atividade', 'integer'),
    Field('id_concentracao', 'integer'),
    Field('email', 'string', length=255),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'),migrate=True)

#####

# log_lancamento_presenca #

db.define_table('log_lancamento_presenca',
    Field('login', 'string', length=15),
    Field('id_insc_pessoa', 'integer'),
    Field('presenca', 'string', length=255),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'),migrate=True)

#####

# log_termino_presenca #

db.define_table('log_termino_presenca',
    Field('login', 'string', length=15),
    Field('edicao_col', 'integer'),
    Field('ip_origem', 'string', length=15),
    Field('data_hora', 'datetime'),migrate=True)
