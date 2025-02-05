from spellchecker import SpellChecker
from deep_translator import GoogleTranslator

def validation(sentence: str)->str: # To suggest the most simillar word to the wrongly spelt word
    spell = SpellChecker()
    words = sentence.split()
    corrected_words = [spell.correction(word) for word in words]
    return " ".join(corrected_words)

def main_introduction()->str:
    print("Chatbot Name")
    language: str = input("chatbot name: Pumili ng wika na nais | Choose your preferred language: Filipino or English: ").upper()
    functions: dict = {"FILIPINO": fil_introuction, "ENGLISH": en_introduction}
    while language not in functions:
        print("Ang wikang pinili ay wala sa aming system | The language you pick is not available in our system")
        language = input("Ilagay muli ang nais na wika | Enter again your preferred language: ").upper()

    functions[language]()  # Call the corresponding introduction
    return language  # Return the selected language
        
def en_introduction()->None:
    print("chatbot name: Hi my name is -----")
    print("chatbot name: You can ask me anything about the province of Laguna")
    print("chatbot name: Enter 'exit' to exit the program")

def fil_introuction()->None:
    print("\nchatbot name: Kamusta ang pangalan ay -----")
    print("chatbot name: Pwede mo kong tanungin ng tungkol sa lalawigan Laguna")
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

def reply(sentence: str)->None:
    data = {
        "HOW ARE YOU": "Fine, Thank you for asking!"
        "INDUSTRIAL ESTATE WITHIN SANTA ROSA, LAGUNA": "\nLaguna Technopark Inc\nGreenfield Automotive Park\nToyota Special Economic Zone\nLakeside Evozone Nuvali\nDaystar Santa Rosa Industrial Park\nSanta Rosa Commercial Complex\nMeridian Industrial Complex"
        "SCHOOLS WITHIN SANTA ROSA, LAGUNA": "\nColegio de Santa Rosa de Lima\nThe Canossa School, Inc. City of Santa Rosa, Laguna\nQueen Anne School of Sta. Rosa\nBlessed Christian School de Sta. Rosa\nHoly Rosary College of Santa Rosa, Laguna, Inc\nMaranatha Living Hope Academy\nDila Elementary School\nFaithful Grace Christian School\nSanta Rosa Science and Technology High School\nDominican College of Santa Rosa\nBalibago Integrated High School\nSaint Ruiz Montessori School\nGreen Fields Integrated School of Laguna, Inc.\nOur Lady of Fatima University Sta. Rosa, Laguna\nSts. Paul & Mark School Inc\nMarie Margarette School\nSouthville 4 National High School\nJesus The Exalted Name School\nSanta Rosa Elementary School Central I HACIENDA DOMINICANO\nPolytechnic University of Philippines\nJose Zavalla Memorial Elamentary School"
        "WHAT IS SIKHAYAN FESTIVAL": "Sikhayan Festival is a yearly cultural celebration in Santa Rosa City, Laguna, Philippines. It's a celebration of the city's founding and a way to honor the community's traditions and pride."
        "WHAT IS SIKHAYAN MEANS": "Sikhayan is a Filipino word that means \"diligence\" and \"livelihood\". It is also the name of an annual festival in Santa Rosa, Laguna, Philippines. The festival celebrates the people of Santa Rosa, their entrepreneurial spirit, and their resilience."
        "WHAT IS SIKHAYAN MEANS": "Sikhayan Festival comes from sikap (hardwork) and kabuhayan (livelihood)."
        "HISTORY OF SIKHAYAN FESTIVAL": "It was launched in 2000 by Mayor Leon Arcillas to celebrate the historic beginning of Santa Rosa City every year and a way to give recognition to it people, their resilience, and their entrepreneurial spirit that drive the city's continuous economic prosperity and growth."
        "SANTA ROSA, LAGUNA IS KNOWN FOR": "Santa Rosa, Laguna is known for its industrial estates, theme park, and the Santa Rosa Arch."
        "SANTA ROSA, LAGUNA IS KNOWN FOR": "One of the two largest municipalities in Laguna, Santa Rosa City, also known as the Lion City of the South, is located west of Laguna de Bay."
        "SANTA ROSA, LAGUNA IS KNOWN FOR": "Sta Rosa was mainly known for the Coca-Cola and Toyota manufacturing plants in its industrial estates. More recently it has also become famous for being the site of Enchanted Kingdom, a local theme park, as well as several housing developments. Santa Rosa is also the exit travellers take along the South Luzon Expressway to go to Tagaytay and Taal Volcano. This city contains the 3rd largest complex in Laguna, Paseo de Santa Rosa."
        "WHY IS SANTA ROSA CITY CALLED THE LION CITY OF THE SOUTH": "It is one of the Philippines’ fastest-growing economies. On March 10, 2004, the Philippine Congress approved Republic Act No. 9264, which made the city of Santa Rosa the first-class municipality from a fourth-class municipality. On July 10, 2004, Santa Rosa was proclaimed the country’s 101st city.\n\nThe city of Santa Rosa has made a name for itself in just three short years after it was transformed into a city and is now known for several economic triumphs. To put the City in the Billionaire’s Club among Philippine local government entities, the City’s 2007 income surpassed the one billion mark, from less than Php 600 million in 2003. Moreover, the flood of foreign and local investors interested in Santa Rosa has helped it treble its annual income during the last decade. Thus, making Santa Rosa the \"Lion City of the South.\""
"WHEN DID SANTA ROSA, LAGUNA BECOME A CITY": "July 10, 2004"
"WHEN DID SANTA ROSA, LAGUNA BECOME A CITY": "From a 4th class municipality in 1986, Santa Rosa became a first class municipality in 1993. Through Republic Act No. 9264 signed by President Gloria Macapagal – Arroyo, Santa Rosa became a component City on July 10, 2004. Presently, the City has been recognized as a fast rising investment capital of South Luzon next to Metro Manila."
"TOTAL POPULATION OF SANTA ROSA, LAGUNA": "Its population as determined by the 2020 Census was 414,812. This represented 12.26% of the total population of Laguna province, or 2.56% of the overall population of the CALABARZON region."
"WHAT SIGNIFIES THE PLAZA IN SANTA ROSA, LAGUNA": "Ang plaza sa Santa Rosa, Laguna, Pilipinas, ay sumisimbolo sa kasaysayan, kultura, at pamana ng lungsod. Tampok sa plaza ang monumento ni Jose Rizal, na kumakatawan sa mga martir ng lungsod at sa kanilang pakikipaglaban para sa kalayaan.\n\nKasaysayan: Ang plaza ay ang lugar ng pagbitay ng mga lokal na gerilya.\nKultura: Ang plaza ay bahagi ng Spanish-era city center ng lungsod, na ginagawang isang \"heritage square\".\nPamana: Ang plaza ay tahanan ng mga heritage house at opisina ng gobyerno.\nKalayaan: Ang monumento ni Jose Rizal ay sumisimbolo sa mga martir ng lungsod at sa kanilang pakikipaglaban para sa kalayaan."
"JOSE RIZA MONUMENT": "\nMartyrdom: The monument symbolizes the sacrifice of life for freedom.\nWisdom: The monument symbolizes the wisdom and bravery of the people of Santa Rosa.\nLight over darkness: The monument symbolizes the idea that light will always triumph over darkness."
"WHO ESTABLISHED THE POLYTECHNIC UNIVERSITY OF THE PHILIPPINE-SANTA ROSA CAMPUS": "The Polytechnic University of the Philippines (PUP) Santa Rosa Campus was established by the Senate and House of Representatives of the Philippines through Republic Act No. 11784. This act is also known as the PUP-Santa Rosa Campus Act."
"WHO REQUESTED TO BUILD A BRANCH CAMPUS OF THE POLYTECHNIC UNIVERSITY OF THE PHILIPPINES IN SANTA ROSA, LAGUNA": "\nThe late mayor of Santa Rosa, Laguna, Hon. Leon C. Arcillas, requested the construction of the Polytechnic University of the Philippines (PUP) Santa Rosa Campus. The campus opened in 2003 and is considered a legacy of Arcillas's efforts to provide quality education to the residents of Santa Rosa and nearby towns.\nThe Polytechnic University of the Philippines was originally established as the Manila Business School in 1904. In 1978, the Philippine College of Commerce (PCC) was renamed PUP through Presidential Decree (PD) 1341."
"CHURCH LOCATED BEHIND THE PLAZA OF SANTA ROSA, LAGUNA": "Santa Rosa de Lima Parish Church"
"WHEN WAS THE SANTA ROSA DE LIMA PARISH CHURCH BUILT": "The Santa Rosa de Lima Parish Church in Santa Rosa, Laguna, Philippines was established in 1792. The church was built by Spanish Catholic priest Francisco Favie."
"THE HISTORY OF THE SANTA ROSA DE LIMA PARISH CHURCH": "The Santa Rosa de Lima Parish Church in Santa Rosa, Laguna, Philippines was built in 1792 by Spanish Catholic priest Francisco Favie. The church was named after Saint Rose of Lima, the patron saint of the Philippines, America, and the East Indies.\n\nConstruction:\nThe church and convent were built within 12 years\nThe present church building was constructed in 1796 by Spanish friars with help from Chinese laborers\nThe church was blessed on August 4, 1812\nThe first Mass was held on August 30, 1812\n\nHistory:\nBefore the church was built, the area was called \"Bucol\"\nThe residents changed the name of the area to \"Santa Rosa\" in honor of the patron saint\nThe original structure still stands and is now known as Museo de Santa Rosa\n\nSaint Rose of Lima\nSaint Rose of Lima was born Isabel Flores de Oliva in Lima, Peru in 1586\nShe was known for helping the sick and hungry in her community\nShe was given the name Rose by a housemaid who said she was \"as lovely as a rose\""
"HISTORICAL TIMELINE OF SANTA ROSA, LAGUNA": "\nThe historical timeline of Santa Rosa, Laguna, Philippines includes the Spanish colonization, the Philippine Revolution, and the post-war era.\n1571: Spanish Conquistador Juan de Salcedo discovers Biñan and annexes it to Tabuco\n1688: Barrio Bukol separates from Cabuyao\n1792: Barrio Bukol becomes the municipality of Santa Rosa\n1812: The Saint Rose of Lima Parish Church is blessed\n1859–1860: The Santa Rosa Arch is built to replace a Spanish guard tower\n1898: Santa Rosa plays a key role in the Philippine Revolution against Spain and signs the Act of Independence\n1945: Santa Rosa is liberated from Japanese occupation during World War II\n1970s: The economy of Santa Rosa is based on agriculture and family-owned businesses\n1980s: Industrialization and foreign investment transform Santa Rosa's economy and society\n2004: Santa Rosa becomes a city"
"HISTORICAL BACKGROUND OF SANTA ROSA, LAGUNA": "\nSanta Rosa, Laguna, Philippines has a rich history that includes its role in the Philippine Revolution, its time under Japanese occupation, and its development from an agricultural town to a modern city.\n\nEarly history\nBarrio Bukol\nIn 1688, Barrio Bukol separated from Cabuyao and became part of Biñan.\n\nSaint Rose of Lima Parish Church\nIn 1792, the Spanish Catholic priest Francisco Favie built the Saint Rose of Lima Parish Church.\n\nMunicipality of Santa Rosa\nIn 1792, Barrio Bukol became its own municipality and was named after Saint Rose of Lima.\n\nSanta Rosa's role in the Philippine Revolution\nSanta Rosa was a key site in the Philippine Revolution against the Spanish. In 1898, Santa Rosa signed the Act of Independence, which proclaimed Philippine Independence from Spain.\n\nWorld War II\nJapanese occupation: During World War II, the Japanese briefly occupied Santa Rosa.\nFilipino guerilla resistance: On February 5, 1945, members of the Filipino guerilla resistance movement liberated Santa Rosa.\n\nPost-war era\nAgriculture and family-owned businesses\nAfter World War II, Santa Rosa's economy was largely dependent on agriculture and family-owned businesses."
"WHAT CALABARZON MEANS": "Calabarzon is the name of an administrative region in the Philippines that's made up of five provinces: Cavite, Laguna, Batangas, Rizal, and Quezon. The name is an acronym of the first letter of each province."
"WHY IS IT CALLED CALABARZON": "\nThe region was created to integrate the social and economic development of the five provinces.\nIt's also known as Region IV-A."
"IN WHAT ASPECT IS CALABARZON KNOWN": "\nCalabarzon is known as the industrial powerhouse of the Philippines.\nIt's home to many of the country's most densely populated provinces.\nIt's the birthplace of Philippine independence from Spain in 1898.\nIt's the birthplace of national heroes like Jose Rizal.\nIt's home to many cultural traditions, including wood carving and taka (papier-mâche)."
"WHAT IS THE RANKING POSITION OF SANTA ROSA, LAGUNA WHEN IT COMES TO ITS RANKING AMONG NEARBY CITIES IN THE ENTIRE COUNTRY": "\nSanta Rosa, Laguna is a prominent city in the Philippines, and is considered the richest city in Luzon outside of Metro Manila. It is also one of the fastest-growing economies in the country.\n\nRanking:\nIn 2019, Santa Rosa was ranked third in the country for its collection efficiency of locally sourced revenues.\nIn 2022, Santa Rosa had the highest revenue of any local government unit (LGU) in Laguna."
"WHERE WAS DR. JOSE RIZAL BORN": "Calamba, Laguna"
"WHEN WAS DR. JOSE RIZAL BORN": "June 19, 1861"
"WHAT IS THE FULL NAME OF DR. JOSE RIZAL": "Jose Protacio Rizal Mercado y Alonso Realonda"
"WHO ARE THE PARENTS OF DR. JOSE RIZAL": "Francisco Mercado and Teodora Alonso Realonda"
"WHO IS THE FATHER OF DR. JOSE RIZAL": "Francisco Mercado"
"WHO IS THE MOTHER OF DR. JOSE RIZAL": "Teodora Alonso Realonda"
"NATURE ATTRACTION IN LAGUNA": "\nPagsanjan Falls\nHulugan Falls\nHidden Valley Falls\nTaytay Falls\nLake Pandin\nMount Makiling\nSampaloc Lake\nMt. Banahaw\nLake Yambo\nBangking Kahoy Valley\nLake Caliraya\nMakiling Botanic Gardens\nBukal Falls\nJapanese Garden\nDalitiwan River\nPanguil River Eco Park\nMount Kalisungan\nCavinti Underground River and Caves Complex\nTayak Hill\nBunga Falls\nMt. Romelo\nBuntot Palos Falls\nKalayaan Twin Falls\nBuruwisan Falls\nPueblo El Salvador Nature’s Park and Picnic Grove\nMagdalena White Water River\nLake Palakpakin\nLake Calibato\nLake Bunot\nLake Muhikap\nHilabaan Island"
"HISTORICAL PLACES IN SANTA ROSA, LAGUNA": "\nCuartel De Sto. Domingo\nSanta Rosa De Lima Parish Church\nMuseo De Santa Rosa\nCity Plaza\nSanta Rosa Arch"
"LOCAL HERITAGE IN BIÑAN, LAGUNA": "\nSite of Historic Alberto Mansion\nSentrong Pangkultura ng Biñan (Old Municipal Building)\nSchool of Rizal Site and Museum\nSan Isidro Labrador Catholic Church\nVicente Ocampo House\nJose Rizal Monument\nLos Maduros Bandstand\nFrancisco Almeda House\nCasa Biñanese – Jacobo Gonzales House\nJacinto Francisco House\nFilomena Belizario Hernandez House\nAlberto Yaptinchay House\nPedro-Isidro Cariño Isidro House\nIluminado Valencia House\nBiñan Roman Catholic Cemetery Camposanto\nCasa Paroquial-Biñan Cursillo House\nGabaldon Building of Biñan Elementary School\nCapilla De San Jose\nOld Binyang PNR Station including its Office and Railway\nBiñan Municipal Cemetery\nFrancisco Baylon House\nFrancisco Guico House\nTeodora Velasco House\nLaureano Cariño House\nIsisdro Gonzalez House\nSoro-soro Prinza Dam\nHistoric Alberto Mansion"



        #We can add more reply and question
    }
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
        else:
            sentence = user_input_EN()
        if sentence == 'EXIT':
            print("chatbot name: Thank you for chatting with me!")
            break
        reply(sentence)

if __name__ == '__main__':
    main()
