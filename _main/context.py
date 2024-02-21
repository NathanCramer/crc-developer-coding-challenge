def global_context(request):
    return {
        'open_ai_api_key': "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",  # Use environment variable in prod
        'weather_api_key': "4ff3544f148691def0dc09dcb61d5c67",  # Use environment variable in prod
    }
