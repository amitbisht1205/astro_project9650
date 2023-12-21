def selected_language(request):
    selected_lang = request.session.get("selected_lang", "hin")  # Default to Hindi if not set
    return {"selected_lang": selected_lang}