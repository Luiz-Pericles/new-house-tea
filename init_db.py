import random
from app import db, Gift

# Dados extraídos do CSV
data = [
    {"ambiente": "Cozinha", "categoria": "Utensílios e Eletrodomésticos", "item": "Conjunto de panelas (antiaderentes ou inox)", "reserved_by": None},
    {"ambiente": "Cozinha", "categoria": "Utensílios e Eletrodomésticos", "item": "Cooktop de indução", "reserved_by": "Ana (Vó de Helô)"},
    {"ambiente": "Cozinha", "categoria": "Utensílios e Eletrodomésticos", "item": "Geladeira Eletrolux 371l", "reserved_by": "Luciano (Pai de Helô)"},
    {"ambiente": "Cozinha", "categoria": "Utensílios e Eletrodomésticos", "item": "Jogo de facas de chef e tábuas de corte", "reserved_by": None},
    {"ambiente": "Cozinha", "categoria": "Utensílios e Eletrodomésticos", "item": "Lava e Seca Samsung 11kg", "reserved_by": "Léo (Tio de Helô)"},
    {"ambiente": "Cozinha", "categoria": "Utensílios e Eletrodomésticos", "item": "Utensílios básicos (espátulas, colheres, conchas, ralador)", "reserved_by": None},
    {"ambiente": "Cozinha", "categoria": "Utensílios e Eletrodomésticos", "item": "Purificador de água pequeno", "reserved_by": None},
    {"ambiente": "Cozinha", "categoria": "Utensílios e Eletrodomésticos", "item": "SUGGAR", "reserved_by": None},
    {"ambiente": "Cozinha", "categoria": "Utensílios e Eletrodomésticos", "item": "Liquidificador e Processador", "reserved_by": None},
    {"ambiente": "Cozinha", "categoria": "Utensílios e Eletrodomésticos", "item": "Sanduicheira (Grill)", "reserved_by": None},
    {"ambiente": "Cozinha", "categoria": "Utensílios e Eletrodomésticos", "item": "Aparelhos de jantar (pratos, copos, talheres)", "reserved_by": None},
    {"ambiente": "Cozinha", "categoria": "Organização", "item": "Potes herméticos e organizadores de armário para mantimentos", "reserved_by": None},
    {"ambiente": "Cozinha", "categoria": "Utensílios e Eletrodomésticos", "item": "Airfrye Eletrolux Ritalobo", "reserved_by": "Dona Fátima"},
    {"ambiente": "Sala de Estar", "categoria": "Móveis e Decoração", "item": "Sofá até 180cm de largura", "reserved_by": None},
    {"ambiente": "Sala de Estar", "categoria": "Móveis e Decoração", "item": "Mesa de centro ou lateral", "reserved_by": None},
    {"ambiente": "Sala de Estar", "categoria": "Móveis e Decoração", "item": "Estante, rack para TV ou suportes para mídia", "reserved_by": None},
    {"ambiente": "Sala de Estar", "categoria": "Iluminação", "item": "Luminárias e abajures", "reserved_by": None},
    {"ambiente": "Quartos", "categoria": "Móveis e Conforto", "item": "Cama completa (estrutura, colchão e travesseiros)", "reserved_by": "Valéria mãe de Helô"},
    {"ambiente": "Quartos", "categoria": "Móveis e Conforto", "item": "Criados-mudos", "reserved_by": None},
    {"ambiente": "Quartos", "categoria": "Móveis e Conforto", "item": "Guarda-roupa 2 portas 2 unidades.", "reserved_by": None},
    {"ambiente": "Quartos", "categoria": "Roupas de Cama", "item": "Jogos de lençóis, edredons e cobertores", "reserved_by": None},
    {"ambiente": "Quartos", "categoria": "Roupas de Cama", "item": "Cortinas e tapetes que ajudem na ambientação", "reserved_by": None},
    {"ambiente": "Banheiros", "categoria": "Itens Básicos", "item": "Conjuntos de toalhas (banho, rosto e mão)", "reserved_by": None},
    {"ambiente": "Banheiros", "categoria": "Itens Básicos", "item": "Tapetes antiderrapantes para o banheiro (tapete de pedra) 2 unidades", "reserved_by": None},
    {"ambiente": "Banheiros", "categoria": "Acessórios e Organização", "item": "Acessórios de banheiro (Porta-toalhas, saboneteira e porta-escova, etc.)", "reserved_by": None},
    {"ambiente": "Itens Gerais", "categoria": "Decoração e Funcionalidade", "item": "Quadros, espelhos e objetos decorativos para personalizar os ambientes", "reserved_by": None},
    {"ambiente": "Itens Gerais", "categoria": "Decoração e Funcionalidade", "item": "Plantas de interior", "reserved_by": None},
    {"ambiente": "Itens Gerais", "categoria": "Decoração e Funcionalidade", "item": "Organizador de prateleiras e caixas para armazenamento extra", "reserved_by": None},
    {"ambiente": "Itens Gerais", "categoria": "Itens para o Dia a Dia", "item": "Kit básico de ferramentas (martelo, chaves de fenda, etc.)", "reserved_by": None},
    {"ambiente": "Itens Gerais", "categoria": "Itens para o Dia a Dia", "item": "Robô aspirador de pó", "reserved_by": None}
]

def init_db(app):
    with app.app_context():
        db.create_all()
        # Se não houver registros, insere os dados
        if Gift.query.count() == 0:
            for row in data:
                # Gera um preço aleatório entre R$50,00 e R$300,00
                random_price = round(random.uniform(50, 300), 2)
                gift = Gift(
                    ambiente=row["ambiente"],
                    categoria=row["categoria"],
                    item=row["item"],
                    reserved_by=row["reserved_by"],
                    price=random_price
                )
                db.session.add(gift)
            db.session.commit()
            print("Banco de dados inicializado com os dados e preços!")
        else:
            print("Banco de dados já possui registros. Nenhuma ação foi tomada.")

if __name__ == "__main__":
    from app import app  # Importa a instância do Flask
    init_db(app)
