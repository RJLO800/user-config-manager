test_settings={
    "theme" : "dark",
    "hello" : 99

}

# add settings
def add_setting(settings, add):
    #define key and value pairs
    key = add[0].lower()
    value = add[1].lower() if isinstance(add[1],str) else add[1]

    
    if key in settings.keys():
        return(f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    else:
        settings[key] = value
        return (f"Setting '{key}' added with value '{value}' successfully!")

#update settings
def update_setting(settings,update):

    key = update[0].lower()
    value = update[1].lower() if isinstance(update[1],str) else update[1]

    if key in settings.keys():
        settings[key]= value
        return(f"Setting '{key}' updated to '{value}' successfully!")
    else:
        return (f"Setting '{key}' does not exist! Cannot update a non-existing setting.")

#delete settings
def delete_setting(settings,keyDel):
    
    key = keyDel[0].lower()

    if key in settings.keys():
        del settings[key]
        return(f"Setting '{key}' deleted successfully!")
    else:
        return (f"Setting not found!")

#view the current settings
def view_settings(settings):
    viewSett = ""
    if not settings:
        return(f"No settings available.")
    else:
        for key, value in settings.items():
            viewSett += f"\n'{key}' : {value}"
        return(f"Current User Settings:{viewSett}")


