class luxury_watch:
    __watches_created = 0

    def __init__(self):
        print('creating watch')
        luxury_watch.__watches_created += 1

    @classmethod
    def engraved_watch(cls, engraving):
        if luxury_watch.validate_engraving(engraving) == True:
             _luxury_watch = cls()
             _luxury_watch.engraving = engraving
             return _luxury_watch
        else:
             print(luxury_watch.validate_engraving(engraving))


    @classmethod
    def get_number_of_watches_created(cls):
        return cls.__watches_created

    @staticmethod
    def validate_engraving(engraving):
        if len(engraving) > 40:
            return "Engraving to long"
        elif not engraving.isalnum():
            return "No Symbols allowed"
        else:
            return True


watch1 = luxury_watch()
print(luxury_watch.get_number_of_watches_created())

watch2 = luxury_watch.engraved_watch('testtext')
print(luxury_watch.get_number_of_watches_created())

watch2 = luxury_watch.engraved_watch('test text')
print(luxury_watch.get_number_of_watches_created())
