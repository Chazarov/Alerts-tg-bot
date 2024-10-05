from Bot.models import MatchingStrings

def getMatching(text:str) -> list[int]:
    strings = MatchingStrings.models.all()
    tickets = {}

    for string in strings:
        if string.string in text:
            tickets[string.ticket] = True


    return [x.user_telegram_id for x in tickets.keys()]
        

