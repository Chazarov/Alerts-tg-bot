from Bot.models import MatchingStrings
from asgiref.sync import sync_to_async

@sync_to_async
def getMatching(text:str) -> list[int]:
    strings = MatchingStrings.objects.all()
    tickets = {}

    for string in strings:
        if string.string in text:
            tickets[string.ticket] = True


    return [x.user_telegram_id for x in tickets.keys()]


        

