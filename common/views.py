import os
from django.conf import settings
from django.http import JsonResponse
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser  # nebo jiná permission třída

# === původní funkce: changelog ===
def changelog(request):
    """
    Načte obsah CHANGELOG.md a přidá aktuální datum a čas k odpovědi.
    """
    changelog_path = os.path.join(settings.BASE_DIR, 'CHANGELOG.md')
    try:
        with open(changelog_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except IOError:
        content = "Changelog nebyl nalezen nebo se nepodařilo načíst."
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content += f"\n\n---\nAktuální čas: {current_time}"
    
    return JsonResponse({"changelog": content})


# === nová utilitní funkce ===
def generate_file_snapshot(start_path='.', exclude_hidden=True):
    """
    Prochází projektový adresář a vrací seznam cest ke všem souborům (bez obsahu).
    """
    file_list = []
    for dirpath, _, filenames in os.walk(start_path):
        for filename in filenames:
            rel_path = os.path.relpath(os.path.join(dirpath, filename), start_path)
            if exclude_hidden and any(part.startswith('.') for part in rel_path.split(os.sep)):
                continue
            file_list.append(rel_path.replace("\\", "/"))  # Windows-friendly
    return sorted(file_list)


# === nový endpoint přes DRF ===
class SnapshotView(APIView):
    permission_classes = [IsAdminUser]  # nebo změň dle potřeby (např. IsAuthenticated)

    def get(self, request):
        start_path = settings.BASE_DIR
        snapshot = generate_file_snapshot(start_path=start_path)
        return Response({"file_structure": snapshot})
