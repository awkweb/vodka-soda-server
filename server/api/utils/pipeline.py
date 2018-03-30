def save_profile(backend, user, response, *args, **kwargs):
    """
    Adds data to user during social auth pipeline.
    """

    if backend.name == 'facebook':
        print(user, response, user.first_name)
        user.display_name = user.first_name
        age_range = response.get('age_range')
        age_range_min = age_range.get('min')
        age_range_max = age_range.get('max')
        if age_range_min == age_range_max or age_range_max is None:
            user.age = age_range_min
        else:
            user.age = (age_range_max + age_range_min) / 2
        user.save()
        return {
            'user': user
        }
