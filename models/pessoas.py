# coding=utf-8


db.define_table('pessoa',
    Field('nome', 'string', length=255, notnull=True, label='Nome Completo*'),
    Field('data_nascimento', 'date', label='Data de Nascimento*'),
    Field('id_sexo', db.sexo, label='Sexo*'),
    Field('nome_mae', 'string', length=255, label='Nome da mãe*'),
    Field('nome_pai', 'string', length=255, label='Nome do pai'),
    Field('id_nacionalidade', db.nacionalidade, label='Nacionalidade*'),
    Field('naturalidade', 'string', length=255, label='Naturalidade*'),
    Field('cpf', 'string', length=14, notnull=True, label='CPF*'),
    Field('rg', 'string', length=50, label='RG*'),
    Field('rg_expedidor', 'string', length=10, label='Órgão Expedidor*'),
    Field('id_uf', db.uf, label='RG UF'),
    Field('nis', 'string', length=50, label='NIS (PIS/PASEP/NIT)*'),
    Field('endereco_logradouro', 'string', length=255, label='Logradouro*'),
    Field('endereco_numero', 'string', length=10, label='Número*'),
    Field('endereco_complemento', 'string', length=50, label='Complemento'),
    Field('endereco_bairro', 'string', length=255, label='Bairro*'),
    Field('endereco_cep', 'string', length=9, label='CEP*'),
    Field('id_cidade', db.cidade, label='Cidade*'),
    Field('telefone1', 'string', length=15, label='Telefone1*'),
    Field('telefone2', 'string', length=15),
    Field('email', 'string', length=255),
    Field('id_escolaridade', db.escolaridade, label='Escolaridade*'),
    Field('id_necessidade_especial', db.necessidade_especial, label='Necessidade Especial*'),
    Field('banco', 'string', length=100),
    Field('agencia', 'string', length=50, label='Agência'),
    Field('conta_corrente', 'string', length=50),migrate=False,fake_migrate=True)

db.pessoa.nome.requires = [IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio')),
                           IS_UPPER(),
                           IS_LENGTH(maxsize=255, error_message='O campo aceita no máximo 255 caracter(es)')]
db.pessoa.data_nascimento.requires = [IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio')),
                                      IS_DATE(format='%d/%m/%Y', error_message='precisa ser no formato DD/MM/AAAA')]
db.pessoa.id_sexo.requires = IS_IN_DB(db, db.sexo.id, '%(genero)s', error_message=T('required field'))
db.pessoa.nome_mae.requires = [IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio')),
                               IS_LENGTH(maxsize=255, error_message='O campo aceita no máximo 255 caracter(es)'),
                               IS_UPPER()]
db.pessoa.nome_pai.requires = [IS_EMPTY_OR(IS_LENGTH(maxsize=255, error_message='O campo aceita no máximo 255 caracter(es)')),
                                IS_EMPTY_OR(IS_UPPER())]
db.pessoa.id_nacionalidade.requires = IS_IN_DB(db, db.nacionalidade.id, '%(nome)s', error_message=T('required field'))
db.pessoa.naturalidade.requires = [IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio')),
                                   IS_UPPER(),
                                   IS_LENGTH(maxsize=255, error_message='O campo aceita no máximo 255 caracter(es)')]
db.pessoa.cpf.requires = [IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio')),
                          IS_MATCH('^[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}$', error_message='CPF deve estar no formato 999.999.999-99'),
                          customValidators.IS_CPF()]
db.pessoa.rg.requires = [IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio')),
                         IS_LENGTH(maxsize=50, error_message='O campo aceita no máximo 50 caracter(es)')]
db.pessoa.rg_expedidor.requires = [IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio')),
                                   IS_UPPER(),
                                   IS_LENGTH(maxsize=10, error_message='O campo aceita no máximo 10 caracter(es)')]
db.pessoa.id_uf.requires = IS_EMPTY_OR(IS_IN_DB(db, db.uf.id, '%(sigla)s'))
db.pessoa.nis.requires = IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio'))
db.pessoa.endereco_logradouro.requires = [IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio')),
                                          IS_UPPER(),
                                          IS_LENGTH(maxsize=255, error_message='O campo aceita no máximo 255 caracter(es)')]
db.pessoa.endereco_numero.requires = [IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio')),
                                      IS_UPPER(),
                                      IS_LENGTH(maxsize=10, error_message='O campo aceita no máximo 10 caracter(es)')]
db.pessoa.endereco_complemento.requires = [IS_EMPTY_OR(IS_UPPER()),
                                           IS_EMPTY_OR(IS_LENGTH(maxsize=50, error_message='O campo aceita no máximo 50 caracter(es)'))]
db.pessoa.endereco_bairro.requires = [IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio')),
                                      IS_UPPER(),
                                      IS_LENGTH(maxsize=255, error_message='O campo aceita no máximo 255 caracter(es)')]
db.pessoa.endereco_cep.requires = [IS_NOT_EMPTY(error_message=T('required field')),
                                   IS_MATCH('^[0-9]{5}-[0-9]{3}$', error_message='Digite o CEP no formato 99999-999')]
#db.pessoa.id_cidade.requires = IS_IN_DB(db, db.cidade.id, '%(nome)s', error_message=T('required field'))
#db.pessoa.telefone1.requires = [IS_NOT_EMPTY(error_message=T('required field')),
                                #IS_MATCH('^\([0-9]{2}\) [0-9]{4}-[0-9]{4}|\([1]{2}\) 9[0-9]{4}-[0-9]{4}$', error_message='Digite o telefone no formato (99) 9999-9999')]
#db.pessoa.telefone2.requires = IS_EMPTY_OR(IS_MATCH('^\([0-9]{2}\) [0-9]{4}-[0-9]{4}|\([1]{2}\) 9[0-9]{4}-[0-9]{4}$', error_message='Digite o telefone no formato (99) 9999-9999'))
db.pessoa.email.requires = [IS_EMPTY_OR(IS_EMAIL(error_message=T('enter a valid email address'))),
                            IS_EMPTY_OR(IS_LOWER())]
db.pessoa.id_escolaridade.requires = IS_IN_DB(db, db.escolaridade.id, '%(nome)s', error_message=T('Campo não pode estar vazio'))
nes = db.executesql(""" SELECT *
                        FROM necessidade_especial
                        ORDER BY id;""", as_dict=True)
listaNes = []
for ne in nes:
    listaNes.append((ne['id'],ne['tipo']))
db.pessoa.id_necessidade_especial.requires = IS_IN_SET(listaNes, error_message=T('required field'))
db.pessoa.banco.requires = [IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio')),IS_LENGTH(maxsize=100, error_message='O campo aceita no máximo 100 caracter(es)'),
                           IS_UPPER()]
db.pessoa.agencia.requires = [IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio')),IS_LENGTH(maxsize=50, error_message='O campo aceita no máximo 50 caracter(es)'),
                              IS_UPPER()]
db.pessoa.conta_corrente.requires = [IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio')),IS_LENGTH(maxsize=50, error_message='O campo aceita no máximo 50 caracter(es)'),
                                    IS_UPPER()]
#db.pessoa.responsavel_instituicao.requires = IS_IN_DB(db, db.instituicao.id, '%(sigla)s')


db.define_table('inscricao_pessoa',
    Field('obs_ne', 'string', length=200, label="Observações relacionadas à necessidade especial"),
    Field('id_pessoa', db.pessoa),
    Field('inscricao', 'string', length=10, unique=True),
    Field('servidor_siape', 'string', length=7, label="Matrícula SIAPE"),
    Field('servidor_setor', 'string', length=255, label="Lotação"),
    Field('servidor_cargo', 'string', length=255, label="Cargo*"),
    Field('indicacao_siape_responsavel', 'string', length=7, label="Matrícula SIAPE (Responsável)*"),
    Field('indicacao_cpf_responsavel', 'string', length=14, label="CPF (Responsável)*"),
    Field('indicacao_setor_responsavel', 'string', length=255, label="SETOR (Responsável)*"),
    Field('indicacao_cargo_responsavel', 'string', length=255, label="CARGO (Responsável)*"),
    Field('indicacao_nome_responsavel', 'string', length=255, label="NOME (Responsável)*"),
    Field('indicacao_ocupacao_principal', 'string', length=255, label="Ocupação Principal do indicado*"),
    Field('trabalhou_unirio', 'boolean', label='Declaro que já trabalhei em qualquer concurso da UNIRIO'),
    Field('trabalhou_outros', 'boolean', label='Declaro que já trabalhei em qualquer concurso de qualquer outra instituição'),
    Field('aluno_matricula', 'string', length=50, label="Matrícula*"),
    Field('aluno_curso', 'string', length=255, label="Curso*"),
    Field('aluno_instituicao', 'string', length=255, label="Instituição de Origem*"),
    Field('aluno_enem', 'string', length=12, label="Inscrição Enem"),

    Field('aluno_cra', 'double', label="Coeficiente de Rendimento Acumulado (CRA)*"),
    Field('id_instituicao', db.instituicao, label="Instituição*"),
    Field('nota_final', 'double', label="Nota Final"),
    Field('isento', 'boolean', default='F'),
    Field('deferida', 'boolean', label="Deferida"),
    Field('motivo', 'string', label="Motivo"),
    Field('ultima_inscricao_paga', 'boolean', default='F'),
    Field('concorre_vaga_pne', 'boolean', default='F', label='Declaro que desejo concorrer às vagas reservadas a portadores de necessidades especiais'),
    Field('concordou_termos', 'boolean', label='Declaro que todas as informações e opções estão corretas e tenho ciência e concordância com as condições expostas no Edital e respectivos aditamentos'),
    Field('id_area', db.area_local, label="Área de Preferência"),migrate=True)

db.inscricao_pessoa.obs_ne.requires = [IS_EMPTY_OR(IS_LENGTH(maxsize=200, error_message='O campo aceita no máximo 200 caracter(es)')),
                                        IS_EMPTY_OR(IS_UPPER())]
db.inscricao_pessoa.id_pessoa.writable = db.inscricao_pessoa.id_pessoa.readable = False
db.inscricao_pessoa.inscricao.writable = db.inscricao_pessoa.inscricao.readable = False
db.inscricao_pessoa.aluno_matricula.requires = [IS_EMPTY_OR(IS_UPPER()),
                                                IS_EMPTY_OR(IS_MATCH('^[012E][0-9ES][0-36-9PDA][0-9E ][1-9DEGOP]+$', error_message='matrícula inválida'))]
db.inscricao_pessoa.aluno_curso.requires = IS_EMPTY_OR(IS_UPPER())
db.inscricao_pessoa.servidor_siape.requires = IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio'))
db.inscricao_pessoa.servidor_setor.requires = IS_NOT_EMPTY(error_message=T('Campo não pode estar vazio'))
#db.inscricao_pessoa.servidor_setor.writable = db.inscricao_pessoa.servidor_setor.readable = False
#db.inscricao_pessoa.servidor_cargo.requires = IS_EMPTY_OR(IS_UPPER())
db.inscricao_pessoa.servidor_cargo.writable = db.inscricao_pessoa.servidor_cargo.readable = False
db.inscricao_pessoa.indicacao_siape_responsavel.requires = IS_EMPTY_OR(IS_MATCH('^[0-9]{7}$', error_message='Somente números com 7 dígitos'))
#db.inscricao_pessoa.indicacao_setor_responsavel.requires = IS_EMPTY_OR(IS_UPPER())
db.inscricao_pessoa.indicacao_setor_responsavel.writable = db.inscricao_pessoa.indicacao_setor_responsavel.readable = False
#db.inscricao_pessoa.indicacao_cargo_responsavel.requires = IS_EMPTY_OR(IS_UPPER())
db.inscricao_pessoa.indicacao_cargo_responsavel.writable = db.inscricao_pessoa.indicacao_cargo_responsavel.readable = False
db.inscricao_pessoa.indicacao_nome_responsavel.requires = IS_EMPTY_OR(IS_UPPER())
#db.inscricao_pessoa.indicacao_ocupacao_principal.requires = IS_EMPTY_OR(IS_UPPER())
db.inscricao_pessoa.indicacao_ocupacao_principal.writable = db.inscricao_pessoa.indicacao_ocupacao_principal.readable = False
db.inscricao_pessoa.isento.writable = db.inscricao_pessoa.isento.readable = False
db.inscricao_pessoa.concordou_termos.requires = IS_NOT_EMPTY(error_message=T('Você precisa concordar com os termos e condições'))
db.inscricao_pessoa.ultima_inscricao_paga.writable = db.inscricao_pessoa.ultima_inscricao_paga.readable = False
db.inscricao_pessoa.deferida.writable = db.inscricao_pessoa.deferida.readable = False
db.inscricao_pessoa.motivo.writable = db.inscricao_pessoa.motivo.readable = False
db.inscricao_pessoa.nota_psd.writable = db.inscricao_pessoa.nota_psd.readable = False
db.inscricao_pessoa.nota_final.writable = db.inscricao_pessoa.nota_final.readable = False
db.inscricao_pessoa.indicacao_cpf_responsavel.writable = db.inscricao_pessoa.indicacao_cpf_responsavel.readable = False
db.inscricao_pessoa.id_area.requires = IS_IN_DB(db, db.area_local.id, '%(nome)s', error_message=T('required field'))
db.inscricao_pessoa.id_area.writable = db.inscricao_pessoa.id_area.readable = False

db.define_table('inscricao_candidato',
                Field('id_vaga', db.vaga),
                Field('nota_psd', 'decimal(6,2)', label="Nota PSD"),

                )

db.define_table('inscricao_colaborador',
    Field('id_atividade', db.atividade, label="Atividade desejada*"),
    Field('id_categoria', db.categoria, label="Categoria*"),
                )