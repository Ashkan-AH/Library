from django.conf import settings

def cloudflare_keys(request):
    return {
        'CLOUDFLARE_TURNSTILE_SITE_KEY': settings.CLOUDFLARE_TURNSTILE_SITE_KEY,
    }