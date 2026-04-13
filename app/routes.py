from flask import Blueprint, request, jsonify
from app import db
from app.models import Usuario, Categoria, Item, Avaliacao

bp = Blueprint('main', __name__)

# ===== USUÁRIOS =====

@bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{'id': u.id, 'nome': u.nome, 'email': u.email} for u in usuarios])

@bp.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    novo = Usuario(nome=dados['nome'], email=dados['email'])
    db.session.add(novo)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário criado!', 'id': novo.id}), 201

@bp.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    dados = request.get_json()
    usuario.nome = dados.get('nome', usuario.nome)
    usuario.email = dados.get('email', usuario.email)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário atualizado!'})

@bp.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário deletado!'})

# ===== CATEGORIAS =====

@bp.route('/categorias', methods=['GET'])
def listar_categorias():
    categorias = Categoria.query.all()
    return jsonify([{'id': c.id, 'nome': c.nome} for c in categorias])

@bp.route('/categorias', methods=['POST'])
def criar_categoria():
    dados = request.get_json()
    nova = Categoria(nome=dados['nome'])
    db.session.add(nova)
    db.session.commit()
    return jsonify({'mensagem': 'Categoria criada!', 'id': nova.id}), 201

@bp.route('/categorias/<int:id>', methods=['PUT'])
def atualizar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    dados = request.get_json()
    categoria.nome = dados.get('nome', categoria.nome)
    db.session.commit()
    return jsonify({'mensagem': 'Categoria atualizada!'})

@bp.route('/categorias/<int:id>', methods=['DELETE'])
def deletar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({'mensagem': 'Categoria deletada!'})

# ===== ITENS =====

@bp.route('/itens', methods=['GET'])
def listar_itens():
    itens = Item.query.all()
    return jsonify([{'id': i.id, 'nome': i.nome, 'categoria_id': i.categoria_id} for i in itens])

@bp.route('/itens', methods=['POST'])
def criar_item():
    dados = request.get_json()
    novo = Item(nome=dados['nome'], categoria_id=dados['categoria_id'])
    db.session.add(novo)
    db.session.commit()
    return jsonify({'mensagem': 'Item criado!', 'id': novo.id}), 201

@bp.route('/itens/<int:id>', methods=['PUT'])
def atualizar_item(id):
    item = Item.query.get_or_404(id)
    dados = request.get_json()
    item.nome = dados.get('nome', item.nome)
    item.categoria_id = dados.get('categoria_id', item.categoria_id)
    db.session.commit()
    return jsonify({'mensagem': 'Item atualizado!'})

@bp.route('/itens/<int:id>', methods=['DELETE'])
def deletar_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'mensagem': 'Item deletado!'})

# ===== AVALIAÇÕES =====

@bp.route('/avaliacoes', methods=['GET'])
def listar_avaliacoes():
    avaliacoes = Avaliacao.query.all()
    return jsonify([{
        'id': a.id,
        'nota': a.nota,
        'comentario': a.comentario,
        'usuario_id': a.usuario_id,
        'item_id': a.item_id
    } for a in avaliacoes])

@bp.route('/avaliacoes', methods=['POST'])
def criar_avaliacao():
    dados = request.get_json()

    # Valida nota entre 1 e 5
    if not 1 <= dados['nota'] <= 5:
        return jsonify({'erro': 'A nota deve ser entre 1 e 5!'}), 400

    # Verifica duplicidade
    ja_existe = Avaliacao.query.filter_by(
        usuario_id=dados['usuario_id'],
        item_id=dados['item_id']
    ).first()

    if ja_existe:
        return jsonify({'erro': 'Usuário já avaliou esse item!'}), 409

    nova = Avaliacao(
        nota=dados['nota'],
        comentario=dados.get('comentario', ''),
        usuario_id=dados['usuario_id'],
        item_id=dados['item_id']
    )
    db.session.add(nova)
    db.session.commit()
    return jsonify({'mensagem': 'Avaliação registrada!', 'id': nova.id}), 201

@bp.route('/avaliacoes/<int:id>', methods=['PUT'])
def atualizar_avaliacao(id):
    avaliacao = Avaliacao.query.get_or_404(id)
    dados = request.get_json()
    if 'nota' in dados:
        if not 1 <= dados['nota'] <= 5:
            return jsonify({'erro': 'A nota deve ser entre 1 e 5!'}), 400
        avaliacao.nota = dados['nota']
    avaliacao.comentario = dados.get('comentario', avaliacao.comentario)
    db.session.commit()
    return jsonify({'mensagem': 'Avaliação atualizada!'})

@bp.route('/avaliacoes/<int:id>', methods=['DELETE'])
def deletar_avaliacao(id):
    avaliacao = Avaliacao.query.get_or_404(id)
    db.session.delete(avaliacao)
    db.session.commit()
    return jsonify({'mensagem': 'Avaliação deletada!'})