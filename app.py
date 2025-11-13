# app.py
from app import create_app

app = create_app()

# Debug: lihat semua route yang terdaftar
if __name__ == '__main__':
    with app.app_context():
        print("✅ Routes registered:")
        for r in app.url_map.iter_rules():
            print(f"  {r.rule} → {r.endpoint}")
    app.run(debug=True)