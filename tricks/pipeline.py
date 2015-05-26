from .models import Profile

def get_profile_picture(backend, user, response, details, *args, **kwargs):
    img_url = None
    profile = Profile.objects.get_or_create(user = user)[0]
    if backend.name == 'facebook':
        img_url  = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
    elif backend.name == "twitter":
        if response['profile_image_url'] != '':
            if not response.get('default_profile_image'):
                img_url = response.get('profile_image_url_https')
                if img_url:
                    img_url = img_url.replace('_normal.', '_bigger.')
    elif backend.name == "google-oauth2":
        if response['image'].get('url') is not None:
            img_url  = response['image'].get('url')
    elif backend.name == "github":
        if response['image'].get('url') is not None:
            img_url = response['image'].get('url')


    profile.image_url = img_url
    profile.save()

# def save_profile_details(backend, user, response, *args, **kwargs):
#     profile = Profile.objects.get_or_create(email = user)[0]

#     if backend.name == 'facebook':
#         img_url  = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
#     elif backend.name == "twitter":
#         if response['profile_image_url'] != '':
#             if not response.get('default_profile_image'):
#                 img_url = response.get('profile_image_url_https')
#                 if img_url:
#                     img_url = img_url.replace('_normal.', '_bigger.')
#     elif backend.name == "google-oauth2":
#         profile = user.get_profile()
#         if profile is None:

#         if response['image'].get('url') is not None:
#             img_url  = response['image'].get('url')