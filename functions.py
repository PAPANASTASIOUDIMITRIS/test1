def number_to_words_el(number):
    units = ["", "ένα", "δύο", "τρία", "τέσσερα", "πέντε", "έξι", "επτά", "οκτώ", "εννέα"]
    teens = ["δέκα", "έντεκα", "δώδεκα", "δεκατρία", "δεκατέσσερα", "δεκαπέντε", "δεκαέξι", "δεκαεπτά", "δεκαοκτώ", "δεκαεννέα"]
    tens = ["", "δέκα", "είκοσι", "τριάντα", "σαράντα", "πενήντα", "εξήντα", "εβδομήντα", "ογδόντα", "ενενήντα"]
    hundreds = ["", "εκατό", "διακόσια", "τριακόσια", "τετρακόσια", "πεντακόσια", "εξακόσια", "επτακόσια", "οκτακόσια", "εννιακόσια"]

    if number == 0:
        return "μηδέν"

    words = []

    # Εκατομμύρια
    if number >= 1_000_000:
        million = number // 1_000_000
        words.append(number_to_words_el(million) + " εκατομμύριο" if million == 1 else number_to_words_el(million) + " εκατομμύρια")
        number %= 1_000_000

    # Χιλιάδες
    if number >= 1000:
        thousand = number // 1000
        if thousand == 1:
            words.append("χίλια")
        elif thousand == 4:
            words.append("τέσσερις χιλιάδες")  # Ειδική περίπτωση για το 4
        else:
            words.append(number_to_words_el(thousand) + " χιλιάδες")
        number %= 1000

    # Εκατοντάδες
    if number >= 100:
        hundred = number // 100
        words.append(hundreds[hundred])
        number %= 100

    # Δεκάδες και μονάδες
    if number >= 20:
        ten = number // 10
        words.append(tens[ten])
        number %= 10

    if 10 <= number < 20:
        words.append(teens[number - 10])
        number = 0

    if number < 10 and number > 0:
        words.append(units[number])

    return " ".join(words)

def convert_currency_to_words(number):
    euros = int(number)
    cents = int(round((number - euros) * 100))

    euros_in_words = number_to_words_el(euros) + " ευρώ"
    cents_in_words = number_to_words_el(cents) + " λεπτά"

    return f"{euros_in_words} και {cents_in_words}"

# Παράδειγμα χρήσης
number = 4234567.89
result = convert_currency_to_words(number)
print(result)