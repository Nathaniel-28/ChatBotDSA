from spellchecker import SpellChecker
from deep_translator import GoogleTranslator

def validation(sentence: str)->str: # To suggest the most simillar word to the wrongly spelt word
    spell = SpellChecker()
    words = sentence.split()
    corrected_words = [spell.correction(word) for word in words]
    return " ".join(corrected_words)

def main_introduction()->str:
    print("City of Santa Rosa Tourist HelpDesk Chatbot")
    language: str = input("chatbot name: Pumili ng wika na nais | Choose your preferred language: Filipino or English: ").upper()
    functions: dict = {"FILIPINO": fil_introuction, "ENGLISH": en_introduction}
    while language not in functions:
        print("Ang wikang pinili ay wala sa aming system | The language you pick is not available in our system")
        language = input("Ilagay muli ang nais na wika | Enter again your preferred language: ").upper()

    functions[language]()  # Call the corresponding introduction
    return language  # Return the selected language
        
def en_introduction()->None:
    print("chatbot name: Hi my name is -----")
    print("chatbot name: You can ask me anything about the city of Santa Rosa")
    print("chatbot name: Enter 'exit' to exit the program")

def fil_introuction()->None:
    print("\nchatbot name: Kamusta ang pangalan ko ay -----")
    print("chatbot name: Pwede mo kong tanungin ng tungkol sa bayan ng Santa Rosa")
    print("chatbot name: I-type lamang ang 'exit' upang matapos ang program")

def user_input_EN()->str:
    question: str = input("user: ").upper().strip()
    if question == 'EXIT':
        return 'EXIT'
    return validation(question)

def user_input_fil()->str:
    question: str = input("user: ").upper().strip()
    if question == 'EXIT':
        return 'EXIT'
    while True:
        try:
            translation = GoogleTranslator(source='tl', target='en').translate(question)
            translation.upper().strip()
            return validation(translation)
        except Exception as e:
            print(f"Nagkaroon ng error sa pag-translate: {e}")
            question = input("Ilagay muli ang tanong: ").upper()

def en_data()->dict:
    data = {
       "HOW ARE YOU": "Fine, Thank you for asking!"
        #We can add more reply and question 
    }
    return data

def fil_data()->dict:
    data = {
        "HOW ARE YOU": "Mabuti, Salamat sa pagtanong!"
        "BARANGAYS IN SANTA ROSA, LAGUNA": "\nThere are eighteen (18) baranggays that can be found in Santa Rosa, Laguna. The following are the eighteen (18) baranggays:\nAplaya \nBalibago \nCaingin \nDila \nDita \nDon Jose \nIbaba \nKanluran \nLabas \nMacabling \nMalitlit \nMalusak \nMarket Area \nPooc \nPulong Santa Cruz \nSanto Domingo \nSinalhan \nTagapo"
        "ATTRACTIONS IN SANTA ROSA, LAGUNA": "\nSanta Rosa City have many attractions that can surely bring happiness not just to tourists, but also to its citizens. These are the attractions, that the Lion City of the South — Santa Rosa, Laguna, can offer:\n\nTheme Park\nEnchanted Kingdom\n\nShopping Centers\nSM City Santa Rosa\nRobinson's Mall\nAyala Malls (Solenad, Solenad 1, Solenad 3, Solenad 4)\nWalterMart\nVictory Mall\nTarget Mall\nWest Borrough Town Center\nPaseo de Santa Rosa\nEton City Square\n\nFarms\nFun Farm at Sta. Elena\nHoly Carabao\n\nParks\nNuvali Park\nSanta Rosa's City Plaza\n\nResorts and Events Place\nDictado 1\nDictado 2\nDictado 3\nSouthpick Resort\nCalypso Resort Hotel\nCarvill Private Resort\nCesar's Cabin Private Resort\nCriselda Private Resort\nPopong's Bukid Private Resort\nOlive's Private Resort\nBayani Resort\nKyler and Kean Private Resort\nCasa Vallejo Events Place and Private Resort\nNMV Resort Farmview\nLas Asturias\nVilla Gilda Resort\nSherinai Events Place\nSouth Country Garden\nLouLyn's Resort\nPablo's Events Place\nMarigold's Farm Resort\nTAR's Family and  Private Resort\nBay View Resort\n\nHotels / Motels\nSeda Nuvali\nPaseo Premiere Hotel\nAsiatel Inn\nTechopark Hotel\nMicrotel\nEl Cielito Hotel\nCasa Emerita\nCandy Motel\nHotel Sogo\nMariposa Hotel\n\nOthers(Sta. Elena's Golf and Country Club)"
        "SHOPPING MALLS IN SANTA ROSA, LAGUNA": "\nThese are the list of Santa Rosa's thriving Shopping Centers:\nSM City Santa Rosa\nRobinson's Mall\nAyala Malls (Solenad, Solenad 1, Solenad 3, Solenad 4)\nWalterMart\nVictory Mall\nTarget Mall\nWest Borrough Town Center\nPaseo de Santa Rosa\nEton City Square"
        "RESORTS AND EVENTS PLACE IN SANTA ROSA, LAGUNA": "\nThere are numerous private, and public resorts, and events place in Santa Rosa, and these includes:\nSouthpick Resort\nDictado 1\nDictado 2\nDictado 3\nCalypso Resort Hotel\nCarvill Private Resort\nCesar's Cabin Private Resort\nCriselda Private Resort\nPopong's Bukid Private Resort\nOlive's Private Resort\nKyler and Kean Private Resort\nCasa Vallejo Events Place and Private Resort\nNMV Resort Farmview\nLas Asturias\nVilla Gilda Resort\nBayani Resort\nSherinai Events Place\nSouth Country Garden\nLouLyn's Resort\nPablo's Events Place\nMarigold's Farm Resort\nTAR's Family and  Private Resort\nBay View Resort"
        "PARKS IN SANTA ROSA, LAGUNA": "\nCurrently, there are two (2) available parks in Santa Rosa, and these are what follows:\nNuvali Park\nSanta Rosa's City Plaza"
        "PLACES WITH WIDE, AND GREEN SCENERIES": "\nCurrently, there are two (2) available parks in Santa Rosa, and these are what follows:\nNuvali Park\nSanta Rosa's City Plaza"
        "PLACES WITH OPEN SPACES": "\nCurrently, there are two (2) available parks in Santa Rosa, and these are what follows:\nNuvali Park\nSanta Rosa's City Plaza"
        "THEME PARK IN SANTA ROSA": "Enchanted Kingdom, also known as EK, is the only theme park that can be found in Santa Rosa, it is known for numerous fun and nerve-wracking rides it can offer, as well as the developed lot spaces it occupies."
        "HOTELS OR MOTELS IN SANTA ROSA": "\nThese are some of the Hotels, or Motels, that are famous, in the City:\nSeda Nuvali\nPaseo Premiere Hotel\nAsiatel Inn\nTechopark Hotel\nMicrotel\nEl Cielito Hotel\nCasa Emerita\nCandy Motel\nHotel Sogo\nMariposa Hotel"
        "RESORTS THAT CAN BE FOUND IN BARANGAY POOC": "\nIn total, there are five (5) resorts located in Barangay Pooc, and these are what follows:\nCarvill Private Resort\nCriselda Private Resort\nPopong's Bukid Private Resort\nOlive's Private Resort\nKyler and Kean Private Resort\n\nThe mentioned resorts, are all located in  Caramay Compound, La Concordia, Barangay Pooc, City of Santa Rosa, Laguna."
        "RESORTS THAT CAN BE FOUND IN BARANGAY MARKET AREA": "\nBarangay Market Area have five(5) resorts can offer, and these are:\nSouthpick Resort\nPablo's Events Place\nDictado 1\nDictado 2\nDictado 3"
        "RESORTS THAT CAN BE FOUND IN BARANGAY SINALHAN": "\nCurrently, There are no resorts that can be found in Barangay Sinalhan"
        "RESORTS THAT CAN BE FOUND IN BARANGAY TAGAPO": "\nThese are the resort Barangay Tagapo can offer:\nLouLyn's Resort\nTAR's Family and Private Resort\nNMV Resort\nSherinai Events Place\nMarigold's Farm Resort"
        "RESORTS THAT CAN BE FOUND IN BARANGAY IBABA": "\nThese is the only resort Barangay Ibaba can offer:\nCasa Vallejo Events Place and Private Resort"
        "RESORTS THAT CAN FOUND IN BARANGAY CAINGIN": "\nThese are the only resorts Barangay Caingin can offer:\nVilla Gilda Resort\nBayani Resort"
        "RESORTS THAT CAN BE FOUND IN BARANGAY DITA": "\nThese is the only resort that can be found in Barangay Dita:\nSouth Country Garden"
        "RESORTS THAT CAN BE FOUND IN BARANGAY MACABLING": "\nThe only resort that can be found in Barangay Macabling is:\nCalypso Resort"
        "EMERGENCY SERVICES": "\nSt. James Hospital\nSanta Rosa Community Hospital\nNew Sinai MD Hospital\nThe Medical City South Luzon\nUnihealth Santa Rosa Hospital and Medical Center\nMarian Hospital\nCity Medic Emergency Hospital\nBalibago Polyclinic and Hospital, Inc.\nSanta Rosa Hospital and Medical Center\nHealthway QualiMed Hospital Santa Rosa\nThe Medical City, South Luzon"
        "WHERE CAN I FIND A TERMINAL": "\nSta. Rosa Complex Central Terminal\nSanta Rosa Integrated\nTerminal (SRIT)\n\nBBL Bus Terminal\nBalibago - Sta. Cruz Van Terminal\nBalibago\nTransport Terminal - Sta. Rosa\nAlabang Express Jeepney Terminal\nShuttle Service Terminal\n\nVan terminal\nJAM Bus Terminal\nPaseo De StaRosa\nUBE Express - Robinsons Sta. Rosa\nJam Liner Bus Stop\n\nTodap Terminal\nBBPL Transport Terminal\nBalibago (Sta Rosa) - (Ulat)Tagaytay City Jeepney Terminal\nPaseo de Sta Rosa - Calamba Jeepney Terminal\nJam Transit Inc. Terminal - Penta\n\nTricycle terminal\nHM Terminal-Target\nNuvali Transport Terminal"
        "WHERE CAN I FIND A JEEPNEY TERMINAL": "\nSta. Rosa Complex Central Terminal\nBalibago\nTransport Terminal - Sta. Rosa\nAlabang Express Jeepney Terminal\nPaseo De StaRosa\nBalibago (Sta Rosa) - (Ulat)Tagaytay City Jeepney Terminal\nPaseo de Sta Rosa - Calamba Jeepney Terminal"
        "WHERE CAN I FIND A BUS TERMINAL": "\nSta. Rosa Complex Central Terminal\nSanta Rosa Integrated Terminal (SRIT)\nBBL Bus Terminal\nShuttle Service Terminal\nJAM Bus Terminal\nUBE Express - Robinsons Sta. Rosa\nJam Liner Bus Stop\nBBPL Transport Terminal\nJam Transit Inc. Terminal - Penta\nHM Terminal-Target\nNuvali Transport Terminal"
        "WHERE CAN I FIND A VAN TERMINAL": "\nSta. Rosa Complex Central Terminal\nSanta Rosa Integrated Terminal (SRIT)\nBalibago - Sta. Cruz Van Terminal\nBalibago Transport Terminal - Sta. Rosa\nShuttle Service Terminal\nVan terminal"
        "WHERE CAN I FIND A TRICYCLE TERMINAL": "\nPaseo De StaRosa\nTodap Terminal\nTricycle terminal"


        # Add english question for the key and fil answer for the value
    }
    return data

def reply(sentence: str, data: dict)->None:
    compare: dict = {key: 0 for key in data.keys()} # Will start at 0 and For every key/question in data
        
    input_words = set(sentence.split()) # Converted to set to efficiently handles matching, and split keys in the data
                                        # input_words is a set of word per word from self.sentence/from the input of the user
    for key, responses in data.items():
        key_words = set(key.split()) # key_word is a set of word per word from each key in data
        compare[key] = len(input_words & key_words)  # This will match how many words match in input_words & key_words using &/ intersection operator

    highest_value = max(compare.values())

    if highest_value == 0: # No match, highest matches does not have any element and is equal to 0
        print("chatbot name: I'm sorry, I don't understand that.")
        return

    matching_keys = [k for k, v in compare.items() if v == highest_value] # Will look for the keys in compare that will match the value of highest_matches
    if len(matching_keys) == 1: # If it is only 1 match
        print(f"chatbot name: {data[matching_keys[0]]}")
    else:
        # If their is a tie, the first match will be picked
        print(f"chatbot name: {data[matching_keys[0]]}")

def main()->None:
    language = main_introduction()
    while True:
        if language == "FILIPINO" :
            sentence = user_input_fil()
            data = fil_data()
        else:
            sentence = user_input_EN()
            data = en_data()
        if sentence == 'EXIT':
            print("chatbot name: Thank you for chatting with me!")
            break
        reply(sentence, data)

if __name__ == '__main__':
    main()
