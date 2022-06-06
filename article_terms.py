### Different lists per personality source
list_personality_traits_1 = ['analytical', 'logical', 'technical', 'strong communication',
                             'creativity skills', 'mathematical', 'business savy']
# conversion: 'mathematically agile' -> 'mathematical'
list_personality_traits_2 = ['rational', 'artisan', 'guardian', 'idealist']
list_personality_traits_3 = ['risk-averse', 'skeptical', 'pragmatic']  # 'matter-of-fact', ]  # I think useless junk
list_personality_traits_4 = ['Curiosity', 'Creativity', 'Critical Thinking',
                             'Intuition']  # is for engineering in general

all_personality_traits = list_personality_traits_1 + list_personality_traits_2 + list_personality_traits_3 + list_personality_traits_4
all_personality_traits = list(map(lambda x: x.lower(), all_personality_traits))

### List for traits employers seek
list_seeked_traits = ['software skills', 'operational skills']
list_seeked_traits_soft = ['management', 'critical thinking', 'mentoring', 'risk management',
                           'communication', 'time management', 'cooperation',
                           'presentation skills', 'team player']

all_seeked_traits = list_seeked_traits + list_seeked_traits_soft

### Lists for different skills per skills article source
list_soft_skills_1 = ['communication', 'curiosity', 'business acumen', 'storytelling',
                      'adaptability', 'critical thinking', 'product understanding',
                      'team player']
list_soft_skills_2 = ['verbal and written communication skills', 'communication skills', 'work ethic',
                      'adaptability', 'critical thinking', 'business acumen',
                      'collaboration']
list_soft_skills_3 = ['business knowledge', 'problem-solving', 'curiosity', 'critical thinking', 'communication',
                      'collaboration']

all_soft_skills = list_soft_skills_1 + list_soft_skills_2 + list_soft_skills_3

list_hard_skills_1 = ['statistics', 'calculus', 'linear algebra',
                      'programming', 'coding', 'predictive modeling', 'machine learning',
                      'deep learning', 'data wrangling', 'data preparation',
                      'model deployment', 'model production', 'data visualization']
# conversions: 'multivariable calculus' -> 'calculus'


all_traits_skills = all_personality_traits + all_seeked_traits + all_soft_skills + list_hard_skills_1
all_traits_skills = list(set(all_traits_skills))
