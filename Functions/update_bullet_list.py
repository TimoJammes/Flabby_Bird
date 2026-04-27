
from Functions.initialize_variables import WIDTH

def update_bullet_list_func(bullet_list):
    
    try:
        for i in range(len(bullet_list)):
            
            if bullet_list[i][0] >= WIDTH:
                del bullet_list[i]
                break
    except:
        pass
    return bullet_list