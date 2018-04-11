def save_profile(backend, user, response, *args, **kwargs):
    """
    Adds data to user during social auth pipeline.
    """

    if backend.name == 'facebook':
        user.display_name = user.first_name
        age_range = response.get('age_range')
        age_range_min = age_range.get('min')  # for verifying user is older than 18
        user_birthday = response.get('user_birthday')  # for auto-populating user birth_date field
        user.save()
        return {
            'user': user
        }
