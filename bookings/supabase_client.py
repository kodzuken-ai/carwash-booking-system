"""
Supabase client configuration for authentication
"""
from supabase import create_client, Client
from django.conf import settings

# Initialize Supabase client
supabase: Client = None
supabase_admin: Client = None

try:
    if settings.SUPABASE_URL and settings.SUPABASE_ANON_KEY:
        # Regular client with anon key
        supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)
        
        # Admin client with service role key (for admin operations)
        if settings.SUPABASE_SERVICE_ROLE_KEY:
            supabase_admin = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_ROLE_KEY)
        
        print('[SUCCESS] Supabase clients initialized successfully')
    else:
        print('[WARNING] Supabase credentials not configured')
except Exception as e:
    print(f'[ERROR] Error initializing Supabase: {e}')


def get_supabase_client():
    """Get the Supabase client instance"""
    return supabase


def get_supabase_admin():
    """Get the Supabase admin client instance"""
    return supabase_admin
