letter = '''Dear <|Name|>,
            You are selected !
            <|Date|>'''

print(letter.replace("<|Name|>", "Nayan").replace("<|Date|>", "7th July 2029"))
