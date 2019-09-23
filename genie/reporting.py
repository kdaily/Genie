"""Error, warning, and message reporting.

"""

def send_validation_error_email(syn, filenames, message, file_users):
    '''
    Sends validation error email

    Args:
        syn: Synapse object
        filenames: invalid filenames
        message: error message
        file_users: List of unique synapse user profiles of
                    users that created and most recently
                    modified the file
    '''
    # Send email the first time the file is invalid
    incorrect_files = ", ".join(filenames)
    usernames = ", ".join([
        syn.getUserProfile(user)['userName']
        for user in file_users])
    email_message = (
        "Dear {username},\n\n"
        "Your files ({filenames}) are invalid! "
        "Here are the reasons why:\n\n{error_message}".format(
            username=usernames,
            filenames=incorrect_files,
            error_message=message))
    syn.sendMessage(
        file_users, "GENIE Validation Error", email_message)


def send_email_duplication_error(syn, duplicated_filesdf):
    '''
    Sends an email if there is a duplication error

    Args:
        syn: Synapse object
        duplicated_filesdf: dataframe with 'id', 'name' column
    '''
    if not duplicated_filesdf.empty:
        incorrect_files = [
            name for synId, name in zip(duplicated_filesdf['id'],
                                        duplicated_filesdf['name'])]
        incorrect_filenames = ", ".join(incorrect_files)
        incorrect_ent = syn.get(duplicated_filesdf['id'].iloc[0])
        send_to_users = set([incorrect_ent.modifiedBy,
                             incorrect_ent.createdBy])
        usernames = ", ".join(
            [syn.getUserProfile(user)['userName'] for user in send_to_users])
        error_email = (
            "Dear {},\n\n"
            "Your files ({}) are duplicated!  FILES SHOULD BE UPLOADED AS "
            "NEW VERSIONS AND THE ENTIRE DATASET SHOULD BE "
            "UPLOADED EVERYTIME".format(usernames, incorrect_filenames))
        syn.sendMessage(
            list(send_to_users), "GENIE Validation Error", error_email)
