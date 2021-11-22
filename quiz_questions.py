quiz = {
    1 : {
        'question' : 'What is the first name of Iron Man ?',
        'answer' : ['Tony', 'Iron'],
        'options' : ['Tony','Stark','Peter','Steve']
    },
    2 : {
        'question' : 'Who is called the god of lightning in Avengers ?',
        'answer' : 'Thor',
        'options' : ['Hulk','Thor','Black Panther','Vision']
    },
    3 : {
        'question' : 'Who carries a shield of American flag theme in Avengers ?',
        'answer' : ['Captain America', 'Capt America'],
        'options' : ['Hulk', 'Thor','Captain America','Wasp']
    },
    4 : {
        'question' : 'Which avenger is green in color ?',
        'answer' : 'Hulk',
        'options' : ['Black Widow','Wasp','Hawkeye','Hulk']
    },
    5 : {
        'question' : 'Which avenger can change it\'s size ?',
        'answer' : ['Antman', 'Ant man'],
        'options' : ['Black Widow','Thor','Iron Man','Ant Man']
    }
}

def check_answer(question, answer):
    
    if type(quiz[question]['answer']) == list:
        for i in quiz[question]['answer']:
            if answer.lower() == i.lower():
                return True
    elif type(quiz[question]['answer']) == str:
        if quiz[question]['answer'].lower() == answer.lower():
            return True
    else:
        return False
