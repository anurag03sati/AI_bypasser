import tkinter as tk
from tkinter import messagebox
from random import SystemRandom ## Lets make this truely random!
from collections import Counter
from random import choices, SystemRandom  ## For synonym replacement and true randomness

## (C) IDoUseLinux, MIT License, 2023

def synonym_replacement(text, synonyms, threshold=0.1):
  """
  Replaces words with synonyms if they occur frequently in the text.

  Args:
      text: The text to process.
      synonyms: A dictionary where keys are words and values are lists of synonyms.
      threshold: The minimum frequency of a word (as a proportion of total words)
                 to be considered for replacement (default: 0.1).

  Returns:
      The text with synonyms replaced, with each word potentially having a different synonym.
  """
  word_counts = Counter(text.lower().split())  # Count word occurrences (lowercase)
  total_words = sum(word_counts.values())

  # Find words that meet the frequency threshold
  frequent_words = [word for word, count in word_counts.items()
                     if count / total_words >= threshold]

  # Replace frequent words with synonyms, choosing a random synonym for each instance
  new_text = []
  for word in text.split():
    if word.lower() in frequent_words and word.lower() in synonyms:
      replacement = choices(synonyms[word.lower()], k=1)[0]  # Choose a random synonym
      new_text.append(replacement)
    else:
      new_text.append(word)
  return ' '.join(new_text)

## (C) IDoUseLinux, MIT License, 2023

def spoof_text(ai_text, scramble_aggresiveness,synonyms) :
    spoofed_text = ''
    for letter in ai_text :
        ## We take the original string and start scrambling it with look-alikes
        if letter == "a" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "а"
        elif letter == "c" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "с"
        elif letter == "d" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "ԁ"
        elif letter == "h" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "һ"
        elif letter == "i" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "і"
        elif letter == "j" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "ј"
        elif letter == "n" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "ո"
        elif letter == "o" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = ["о", "ο", "օ" ][SystemRandom().randint(0,2)]
        elif letter == "q" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "р"
        elif letter == "v" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "ν"
        elif letter == "x" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "х"
        elif letter == "y" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "у"
        elif letter == ";" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = ";"
        elif letter == "." and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "․"
        elif letter == "," and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "‚"

        ## The invisible characters
        if SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter += "‎"*SystemRandom().randrange(0,5)
        if SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter += "‍"*SystemRandom().randrange(0,5)
        spoofed_text += letter

    spoofed_text = synonym_replacement(spoofed_text, synonyms)
    return spoofed_text

class GUI :
    APP_BG_COLOR = "#192e45"
    BAR_COLOR = "#346191"
    ENTRY_COLOR = "#15283c"
    TEXT_COLOR="#ffffff"
    all_screen_obj = []

    def __init__(self, app) :
        self.app = app
        self.app.geometry("600x500")
        self.app.title("Ain't (Ai Ain't)")
        self.app.configure(bg=self.APP_BG_COLOR)
        self.spawn_screen()
        self.app.mainloop()

    def clear_screen(self) :
        while self.all_screen_obj:
            self.all_screen_obj[0].destroy()
            del self.all_screen_obj[0]

    def spawn_screen(self) :
        frame = tk.Frame(self.app, bg=self.BAR_COLOR, width=600, height=0, padx=0, pady=0)
        frame.pack(padx=0, pady=0, fill="both")

        program_name = tk.Label(frame, text="Ain't (Ai Ain't, great name, I know...)", font=("Segoe UI", 20), fg=self.TEXT_COLOR, bg=self.BAR_COLOR)
        program_name.pack(side=tk.TOP, padx=0, pady=(20,20))

        instruction = tk.Label(self.app, text="Enter the AI-tagged text: ", font=("Segoe UI", 20),fg=self.TEXT_COLOR, bg=self.APP_BG_COLOR)
        instruction.pack(side=tk.TOP, pady=10)

        self.text_entry = tk.Text(self.app, bg=self.ENTRY_COLOR, fg=self.TEXT_COLOR, width=200, height=8, font=("Segoe UI", 15), insertbackground="#ffffff", border=5 ) ## For some dumb reason, the height is measured by how many lines it is, not actually how many pixels.
        self.text_entry.pack(anchor=tk.CENTER, padx=30, pady=30)

        sumbit_button = tk.Button(self.app, bg="red", fg=self.TEXT_COLOR, text="Spoof", command=self.__spoof_text__)
        sumbit_button.pack(side=tk.TOP, pady=10)

        self.all_screen_obj.append(program_name)
        self.all_screen_obj.append(frame)
        self.all_screen_obj.append(self.text_entry)

    ## We are going to add the about later.
    def spawn_about(self) :
        pass

    def __spoof_text__(self) :
        text = self.text_entry.get("1.0", tk.END)
        self.text_entry.delete("1.0", tk.END)
        synonyms = {
            'good': ['excellent', 'great', 'wonderful'], 'bad': ['terrible', 'horrible', 'awful'], 'honesty': ['truthfulness', 'integrity', 'sincerity'], 'kindness': ['benevolence', 'gentleness', 'compassion'], 'compassion': ['empathy', 'understanding', 'sympathy'], 'patience': ['forbearance', 'endurance', 'tolerance'], 'integrity': ['honesty', 'uprightness', 'moral rectitude'], 'courage': ['bravery', 'valor', 'boldness'], 'generosity': ['charity', 'benevolence', 'kindness'], 'humility': ['modesty', 'meekness', 'humbleness'], 'perseverance': ['tenacity', 'steadfastness', 'persistence'], 'responsibility': ['accountability', 'dependability', 'reliability'], 'optimism': ['hopefulness', 'positivity', 'cheerfulness'], 'gratitude': ['thankfulness', 'appreciation'], 'respect': ['deference', 'reverence', 'admiration'], 'cooperation': ['collaboration', 'teamwork'], 'humor': ['wit', 'funniness', 'joviality'], 'creativity': ['inventiveness', 'imagination', 'resourcefulness'], 'adaptability': ['versatility', 'flexibility'], 'resourcefulness': ['ingenuity', 'inventiveness', 'cunning'], 'confidence': ['self-assurance', 'belief', 'conviction'], 'love': ['affection', 'fondness', 'devotion'], 'forgiveness': ['pardon', 'absolution', 'clemency'], 'strength': ['power', 'vigor', 'fortitude'], 'wisdom': ['knowledge', 'insight', 'sagacity'], 'peace': ['tranquility', 'calm', 'serenity'], 'learning': ['acquisition of knowledge', 'education', 'scholarship'], 'adventure': ['exploration', 'journey', 'quest'], 'mystery': ['enigma', 'riddle', 'puzzle'], 'danger': ['risk', 'hazard', 'peril'], 'friendship': ['companionship', 'amity', 'camaraderie'], 'victory': ['triumph', 'win', 'conquest'], 'defeat': ['loss', 'failure', 'downfall'], 'hero': ['savior', 'protector', 'champion'], 'villain': ['antagonist', 'fiend', 'scoundrel'], 'magic': ['sorcery', 'wizardry', 'enchantment'], 'curse': ['hex', 'jinx', 'spell'], 'treasure': ['riches', 'booty', 'loot'], 'battle': ['conflict', 'struggle', 'war'], 'journey': ['expedition', 'voyage', 'trek'], 'discovery': ['revelation', 'finding', 'uncovering'], 'freedom': ['liberty', 'independence', 'autonomy'], 'justice': ['fairness', 'equity', 'impartiality'], 'revenge': ['vengeance', 'retribution', 'retaliation'], 'sacrifice': ['offering', 'self-denial', 'forfeiture'], 'loyalty': ['faithfulness', 'fidelity', 'allegiance'], 'betrayal': ['treachery', 'disloyalty', 'deception'], 'truth': ['reality', 'verity', 'fact'], 'lie': ['falsehood', 'deception', 'untruth'], 'hope': ['expectation', 'aspiration', 'desire'], 'despair': ['hopelessness', 'misery', 'despondency'], 'bravery': ['courage', 'valor', 'heroism'], 'fear': ['terror', 'fright', 'dread'], 'knowledge': ['understanding', 'awareness', 'information'], 'hate': ['hatred', 'loathing', 'detestation'], 'war': ['conflict', 'battle', 'strife'], 'joy': ['happiness', 'delight', 'pleasure'], 'sadness': ['sorrow', 'misery', 'unhappiness'], 'anger': ['rage', 'fury', 'wrath'], 'envy': ['jealousy', 'covetousness', 'resentment'], 'pride': ['arrogance', 'hubris', 'self-esteem'], 'greed': ['avarice', 'covetousness', 'cupidity'], 'trust': ['confidence', 'faith', 'reliance'], 'doubt': ['uncertainty', 'skepticism', 'suspicion'], 'beauty': ['attractiveness', 'loveliness', 'charm'], 'ugliness': ['hideousness', 'repulsiveness', 'unsightliness'], 'weakness': ['frailty', 'infirmity', 'feebleness'], 'wealth': ['riches', 'affluence', 'prosperity'], 'poverty': ['destitution', 'neediness', 'impoverishment'], 'captivity': ['imprisonment', 'confinement', 'incarceration'], 'honor': ['dignity', 'glory', 'prestige'], 'shame': ['disgrace', 'humiliation', 'embarrassment'], 'calm': ['serenity', 'peace', 'tranquility'], 'chaos': ['disorder', 'confusion', 'turmoil'], 'ignorance': ['naivety', 'unawareness', 'stupidity'], 'faith': ['belief', 'trust', 'confidence'], 'skepticism': ['doubt', 'disbelief', 'cynicism'], 'leader': ['chief', 'commander', 'head'], 'follower': ['disciple', 'adherent', 'supporter'], 'advice': ['guidance', 'counsel', 'recommendation'], 'attack': ['assault', 'offensive', 'strike'], 'defense': ['protection', 'guard', 'shield'], 'pain': ['suffering', 'agony', 'ache'], 'relief': ['comfort', 'alleviation', 'ease'], 'disaster': ['catastrophe', 'calamity', 'tragedy'], 'rescue': ['salvation', 'recovery', 'retrieval'], 'fame': ['renown', 'celebrity', 'stardom'], 'obscurity': ['ambiguity', 'vagueness', 'uncertainty'], 'innocence': ['purity', 'naivety', 'blamelessness'], 'guilt': ['culpability', 'blame', 'fault'], 'disguise': ['camouflage', 'mask', 'concealment'], 'reveal': ['disclose', 'unveil', 'expose'], 'confusion': ['bewilderment', 'perplexity', 'uncertainty'], 'clarity': ['clearness', 'lucidity', 'transparency'], 'suspicion': ['distrust', 'doubt', 'wariness'], 'celebration': ['festivity', 'jubilation', 'rejoicing'], 'mourning': ['grieving', 'lamentation', 'sorrow'], 'disrespect': ['contempt', 'scorn', 'disdain'], 'agreement': ['accord', 'harmony', 'consensus'], 'disagreement': ['conflict', 'dispute', 'discord'], 'rich': ['wealthy', 'affluent', 'prosperous'], 'poor': ['impoverished', 'needy', 'destitute'], 'beginning': ['start', 'inception', 'commencement'], 'end': ['conclusion', 'termination', 'finish'], 'darkness': ['gloom', 'obscurity', 'shadow'], 'light': ['brightness', 'illumination', 'radiance'], 'cowardice': ['timidity', 'fearfulness', 'pusillanimity'], 'treachery': ['betrayal', 'disloyalty', 'perfidy'], 'happiness': ['joy', 'delight', 'contentment'], 'safety': ['security', 'protection', 'shelter'], 'clean': ['pure', 'spotless', 'immaculate'], 'dirty': ['unclean', 'filthy', 'grimy'], 'build': ['construct', 'create', 'erect'], 'destroy': ['annihilate', 'wreck', 'demolish'], 'storm': ['tempest', 'gale', 'hurricane'], 'acceptance': ['approval', 'embrace', 'acknowledgment'], 'rejection': ['dismissal', 'refusal', 'denial'], 'harmony': ['unity', 'accord', 'agreement'], 'conflict': ['discord', 'dispute', 'strife'], 'help': ['assist', 'aid', 'support'], 'hinder': ['obstruct', 'impede', 'hamper'], 'grief': ['sorrow', 'sadness', 'misery'], 'create': ['invent', 'design', 'develop'], 'energy': ['vitality', 'vigor', 'liveliness'], 'fatigue': ['tiredness', 'exhaustion', 'weariness'], 'order': ['sequence', 'arrangement', 'organization'], 'falsehood': ['lie', 'deception', 'untruth'], 'gain': ['acquire', 'obtain', 'attain'], 'loss': ['deprivation', 'deficit', 'decline'], 'praise': ['commendation', 'accolade', 'applause'], 'criticism': ['disapproval', 'condemnation', 'censure'], 'violence': ['aggression', 'brutality', 'hostility'], 'coward': ['weakling', 'craven', 'timid person'], 'life': ['existence', 'being', 'livelihood'], 'death': ['demise', 'end', 'expiration'], 'fortune': ['luck', 'destiny', 'fate'], 'misfortune': ['bad luck', 'adversity', 'tragedy'], 'growth': ['development', 'expansion', 'progress'], 'decline': ['deterioration', 'decrease', 'reduction'], 'timidity': ['fearfulness', 'shyness', 'bashfulness'], 'achievement': ['accomplishment', 'attainment', 'success'], 'failure': ['defeat', 'collapse', 'flop'], 'glory': ['fame', 'honor', 'renown'], 'disgrace': ['shame', 'dishonor', 'humiliation'], 'prosperity': ['wealth', 'success', 'affluence'], 'hardship': ['difficulty', 'adversity', 'misfortune'], 'vision': ['sight', 'perception', 'foresight'], 'blindness': ['sightlessness', 'invisibility', 'obscurity'], 'zeal': ['enthusiasm', 'passion', 'fervor'], 'apathy': ['indifference', 'unconcern', 'disinterest'], 'disloyalty': ['betrayal', 'treachery', 'infidelity'], 'mistrust': ['suspicion', 'doubt', 'wariness'], 'deceit': ['fraud', 'trickery', 'dishonesty'], 'virtue': ['morality', 'goodness', 'righteousness'], 'vice': ['immorality', 'wickedness', 'corruption'], 'slavery': ['bondage', 'servitude', 'oppression'], 'sorrow': ['grief', 'sadness', 'misery'], 'stinginess': ['miserliness', 'parsimony', 'meanness'], 'discord': ['conflict', 'disagreement', 'disharmony'], 'health': ['well-being', 'fitness', 'vitality'], 'sickness': ['illness', 'disease', 'ailment'], 'injustice': ['inequity', 'unfairness', 'wrongdoing'], 'abundance': ['plenty', 'profusion', 'wealth'], 'scarcity': ['shortage', 'lack', 'deficiency'], 'cleanliness': ['purity', 'neatness', 'tidiness'], 'dirtiness': ['filthiness', 'uncleanness', 'grubbiness'], 'disorder': ['chaos', 'confusion', 'turmoil'], 'success': ['achievement', 'triumph', 'victory'], 'impatience': ['restlessness', 'eagerness', 'irritability'], 'pessimism': ['negativity', 'gloom', 'despair']
        }

        spoofed_text = spoof_text(text, scramble_aggresiveness=10, synonyms=synonyms)
        self.text_entry.insert("1.0", spoofed_text)

if __name__ == "__main__" :
    ## Tkinter genuinely sucks
    ## CustomTKinter is much better
    app = tk.Tk()
    GUI(app)

#He is a good boy, he is very GOOD in maths. Also he has a very good nature