import pandas as pd
def csv_to_kml(csv_file_path, output_kml_path):
    # Lire le fichier CSV
    data = pd.read_csv(csv_file_path)

    # Vérifier si les colonnes requises sont présentes
    required_columns = {'name', 'address', 'city', 'zip', 'lat', 'lng', 'email', 'url'}
    if not required_columns.issubset(data.columns):
        missing = required_columns - set(data.columns)
        raise ValueError(f"Colonnes requises manquantes: {missing}")

    # Créer le fichier KML ou l'écrase s'il existe déjà
    with open(output_kml_path, 'w', encoding='utf-8') as f:
        # en-tête KML
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        f.write('  <Document>\n')

        # Boucle sur chaque ligne et créer un Placemark pour chaque entrée
        for _, row in data.iterrows():
            f.write('    <Placemark>\n')
            f.write(f'      <name>{row["name"]}</name>\n')
            f.write('      <description><![CDATA[\n')
            f.write(f'        Adresse: {row["address"]}, {row["city"]}, {row["zip"]}<br>\n')
            f.write(f'        Email: {row["email"]}<br>\n')
            f.write(f'        Site web: <a href="{row["url"]}">{row["url"]}</a><br>\n')
            f.write(f'        Coordonnées: {row["lat"]}, {row["lng"]}\n')
            f.write('      ]]></description>\n')
            f.write('      <Point>\n')
            f.write(f'        <coordinates>{row["lng"]},{row["lat"]}</coordinates>\n')
            f.write('      </Point>\n')
            f.write('    </Placemark>\n')

        # pied de page KML
        f.write('  </Document>\n')
        f.write('</kml>\n')

    print(f"Fichier KML généré: {output_kml_path}")

# Définir le fichier CSV d'entrée et le nom du fichier KML de sortie
csv_file_path = 'carte_nous_trouver/wp_storelocator.csv'  # Chemin vers votre fichier .csv
output_kml_path = 'upload_in_goodbarber.kml'  # Nom du fichier KML de sortie .kml

# Appel de la fonction
csv_to_kml(csv_file_path, output_kml_path)
