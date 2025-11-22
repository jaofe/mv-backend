"""
Seeder for Brazilian fish species.
This script populates the species table with common Brazilian fish.
"""

from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.species.model import Species


BRAZILIAN_FISH = [
    {
        "name": "Tilápia",
        "description": "Peixe de água doce muito popular na aquicultura brasileira. Carne branca e sabor suave, ideal para diversos preparos culinários."
    },
    {
        "name": "Tambaqui",
        "description": "Peixe de escamas nativo da Amazônia. Um dos peixes mais consumidos no Norte do Brasil, conhecido por sua carne saborosa e rica em ômega-3."
    },
    {
        "name": "Pirarucu",
        "description": "Considerado o bacalhau da Amazônia, é um dos maiores peixes de água doce do mundo. Carne firme e sabor suave, muito apreciado na culinária regional."
    },
    {
        "name": "Tambaqui",
        "description": "Peixe redondo de água doce, nativo da Bacia Amazônica. Possui carne saborosa e é muito utilizado em pratos típicos do Norte."
    },
    {
        "name": "Pacu",
        "description": "Peixe de água doce da família dos Characídeos. Carne clara e saborosa, muito apreciado na pesca esportiva e na culinária."
    },
    {
        "name": "Dourado",
        "description": "Peixe de couro encontrado nas bacias hidrográficas brasileiras. Considerado um dos melhores peixes de água doce para consumo."
    },
    {
        "name": "Pintado",
        "description": "Também conhecido como surubim, é um peixe de couro de água doce. Carne branca, firme e muito saborosa, sem espinhas."
    },
    {
        "name": "Traíra",
        "description": "Peixe de água doce encontrado em todo o Brasil. Carne firme e saborosa, muito utilizado na culinária tradicional."
    },
    {
        "name": "Tucunaré",
        "description": "Peixe de água doce nativo da Amazônia. Muito apreciado na pesca esportiva e possui carne branca e saborosa."
    },
    {
        "name": "Robalo",
        "description": "Peixe de água salgada e salobra muito valorizado. Carne branca, firme e delicada, considerado um peixe nobre."
    },
    {
        "name": "Corvina",
        "description": "Peixe de água salgada encontrado no litoral brasileiro. Carne clara e macia, muito versátil na cozinha."
    },
    {
        "name": "Pescada",
        "description": "Peixe marinho muito consumido no Brasil. Carne branca e macia, ideal para diversos preparos."
    },
    {
        "name": "Sardinha",
        "description": "Peixe marinho pequeno e rico em ômega-3. Muito popular e acessível, tradicionalmente consumido grelhado ou em conserva."
    },
    {
        "name": "Atum",
        "description": "Peixe marinho de grande porte. Carne vermelha rica em proteínas e ômega-3, consumido fresco ou em conserva."
    },
    {
        "name": "Salmão",
        "description": "Peixe de água fria, geralmente importado. Carne rosada rica em ômega-3, muito valorizado na culinária."
    },
    {
        "name": "Merluza",
        "description": "Peixe marinho de carne branca e macia. Muito utilizado na indústria de processamento e em preparos culinários."
    },
    {
        "name": "Badejo",
        "description": "Peixe marinho considerado nobre. Carne branca, firme e saborosa, muito apreciado na alta gastronomia."
    },
    {
        "name": "Garoupa",
        "description": "Peixe marinho de grande porte e alta qualidade. Carne firme e saborosa, muito valorizado comercialmente."
    },
    {
        "name": "Namorado",
        "description": "Peixe marinho de águas profundas. Carne clara, firme e muito saborosa, considerado um peixe premium."
    },
    {
        "name": "Linguado",
        "description": "Peixe marinho achatado de carne branca e delicada. Muito apreciado na culinária refinada."
    },
    {
        "name": "Tainha",
        "description": "Peixe encontrado em águas costeiras e estuários. Muito consumido na região Sul, especialmente no inverno."
    },
    {
        "name": "Bagre",
        "description": "Peixe de couro de água doce. Carne firme e saborosa, muito utilizado na culinária popular."
    },
    {
        "name": "Cação",
        "description": "Pequeno tubarão consumido como peixe. Carne firme sem espinhas, tradicionalmente usado em postas e ensopados."
    },
    {
        "name": "Anchova",
        "description": "Peixe marinho de sabor marcante. Utilizado fresco ou em conserva, muito apreciado na culinária mediterrânea."
    },
    {
        "name": "Pargo",
        "description": "Peixe marinho de carne rosada e saborosa. Muito valorizado na gastronomia e na pesca."
    }
]


def seed_species(db: Session):
    """
    Seed the database with Brazilian fish species.
    
    Args:
        db: Database session
    """
    print("Starting species seeding...")
    
    # Check if species already exist
    existing_count = db.query(Species).count()
    if existing_count > 0:
        print(f"Database already has {existing_count} species. Skipping seeding.")
        return
    
    # Add all species
    species_added = 0
    for fish_data in BRAZILIAN_FISH:
        # Check if this specific species already exists
        existing_species = db.query(Species).filter(Species.name == fish_data["name"]).first()
        if not existing_species:
            species = Species(
                name=fish_data["name"],
                description=fish_data["description"]
            )
            db.add(species)
            species_added += 1
    
    db.commit()
    print(f"Successfully added {species_added} fish species to the database!")


def run_seeder():
    db = SessionLocal()
    try:
        seed_species(db)
    except Exception as e:
        print(f"Error seeding species: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    run_seeder()
