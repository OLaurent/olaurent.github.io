from app import app, db

# Créez un contexte d'application
with app.app_context():
    # Supprimez toutes les tables de la base de données
    db.drop_all()
    print("Toutes les tables ont été supprimées de la base de données.")