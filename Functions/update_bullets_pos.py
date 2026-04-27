from Functions.initialize_variables import bullet_speed

def update_bullets_pos_func(bullet_list):
    
    try:
        for i in range(len(bullet_list)):
            
            bullet_list[i][0] += bullet_speed
    
    except:
        pass
    return bullet_list